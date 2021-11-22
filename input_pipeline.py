import tensorflow as tf
from data_extract import data_read

input_data = data_read("s3://misbucket-uca/habbo.csv")


def input_pipeline(input_data,WINDOW_SIZE):
    for i in range(WINDOW_SIZE):
        input_data[f"value+{i + 1}"] = input_data["value"].shift(periods=i + 1)

    # Make features and labels
    x = input_data.dropna().drop("value", axis=1).to_numpy()
    y = input_data.dropna()["value"].to_numpy()

    # 1. Turn train into tensor Datasets
    train_features_dataset = tf.data.Dataset.from_tensor_slices(x)
    train_labels_dataset = tf.data.Dataset.from_tensor_slices(y)

    # 2. Combine features & labels
    train_dataset = tf.data.Dataset.zip((train_features_dataset, train_labels_dataset))

    # 3. Batch and prefetch for optimal performance
    BATCH_SIZE = 1024
    train_dataset = train_dataset.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
    return train_dataset

#input_pipeline(input_data,15)


def y_degiscek(input_data,WINDOW_SIZE):
    for i in range(WINDOW_SIZE):
        input_data[f"value+{i + 1}"] = input_data["value"].shift(periods=i + 1)
    y = input_data.dropna()["value"].to_numpy()
    return y
