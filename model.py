import tensorflow as tf
import os


def get_ready_for_model(directory):
    ensemble_models = []
    root_path = []
    for path in os.listdir(directory):
        full_path = os.path.join(directory, path)
        root_path.append(full_path)
    for root in root_path:
        model_inference = tf.keras.models.load_model(root)
        ensemble_models.append(model_inference)
    return ensemble_models


