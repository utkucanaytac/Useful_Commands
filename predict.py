import tensorflow as tf
import pandas as pd
import numpy as np
from data_extract import data_read
from model import get_ready_for_model
from input_pipeline import y_degiscek

liste = []
WINDOW_SIZE = 15
HORIZON = 1
directory = "/Users/uca/PycharmProjects/MIS/ensemble_models"
input_data = data_read("s3://misbucket-uca/habbo.csv")

habbo = data_read("s3://misbucket-uca/habbo.csv")
y = y_degiscek(input_data,15)

ensemble_models = get_ready_for_model(directory)
print(ensemble_models)

def make_ensemble_preds(ensemble_models, last_window):
    for model in ensemble_models:
        # make predictions with current ensemble model
        preds = model.predict(tf.expand_dims(last_window, axis=0))
        # print(preds)
        liste.append(preds)

    return np.mean(liste,axis=0)  ####### can be taken as the mean of the point predictions from ensemble members to calculate upper lower bounds soon


# 1. Create function to make predictions into the future
def make_future_forecast(values, model, into_future, window_size=WINDOW_SIZE) -> list:
    """

  Returns future forecasts as list of floats.
  """
    # 2. Make an empty list for future forecasts/prepare data to forecast on
    future_forecast = []

    last_window = values[-WINDOW_SIZE:]  # only want preds from the last window (this will get updated)
    # print("last window is {}" .format(last_window))

    # 3. Make INTO_FUTURE number of predictions, altering the data which gets predicted on each time
    for _ in range(into_future):
        # Predict on last window then append it again, again, again (model starts to make forecasts on its own forecasts)
        future_pred = make_ensemble_preds(ensemble_models, last_window)
        future_pred = np.median(future_pred, axis=0)

        # print("future preds are {}" .format(future_pred))
        # print(f"Predicting on: \n {last_window} -> Prediction: {tf.squeeze(future_pred).numpy()}\n")

        # Append predictions to future_forecast
        future_forecast.append(tf.squeeze(future_pred).numpy())
        # print(future_forecast)

        # Update last window with new pred and get WINDOW_SIZE most recent preds (model was trained on WINDOW_SIZE windows)
        last_window = np.append(last_window, future_pred)[-WINDOW_SIZE:]

    return future_forecast


INTO_FUTURE = 7
future_forecast = make_future_forecast(values=y,
                                       model=ensemble_models,
                                       into_future=INTO_FUTURE,
                                       window_size=WINDOW_SIZE)


def get_future_dates(start_date, into_future, offset=1):
    """
  Returns array of datetime values from ranging from start_date to start_date+horizon.

  start_date: date to start range (np.datetime64)
  into_future: number of days to add onto start date for range (int)
  offset: number of days to offset start_date by (default 1)
  """
    start_date = start_date + np.timedelta64(offset, "D")  # specify start date, "D" stands for day
    end_date = start_date + np.timedelta64(into_future, "D")  # specify end date
    return np.arange(start_date, end_date, dtype="datetime64[D]")  # return a date range between start date and end date


# Last timestep of timesteps (currently in np.datetime64 format)
last_timestep = habbo.index[-1]


next_time_steps = get_future_dates(start_date=last_timestep,
                                   into_future=INTO_FUTURE)

dict(zip(next_time_steps, future_forecast))

preds_last = np.reshape(liste, (7, 9))


# Find upper and lower bounds of ensemble predictions
def get_upper_lower(preds):  # 1. Take the predictions of multiple randomly initialized deep learning neural networks

    # 2. Measure the standard deviation of the predictions
    std = tf.math.reduce_std(preds_last, axis=1)

    # 3. Multiply the standard deviation by 1.96
    interval = 1.96 * std  # https://en.wikipedia.org/wiki/1.96
    # print(interval)

    # 4. Get the prediction interval upper and lower bounds

    preds_mean = tf.reduce_mean(preds_last, axis=1)
    # print(preds_mean)
    lower, upper = tf.maximum(0, preds_mean - interval), preds_mean + interval
    return lower, upper


# Get the upper and lower bounds of the 95%
lower, upper = get_upper_lower(preds=preds_last)

d = {'Timestamp': next_time_steps, 'Future_Forecast': future_forecast, 'Lower_Bound': lower, 'Upper_Bound': upper}
habbo_futured = pd.DataFrame(data=d)
print(habbo_futured)