import tensorflow as tf
import pandas as pd

SHUFFLE_BUFFER = 500
BATCH_SIZE = 2
csv_file = tf.keras.utils.get_file('heart.csv', 'https://storage.googleapis.com/download.tensorflow.org/data/heart.csv')

df = pd.read_csv(csv_file)
print(df.head())

numeric_feature_names = ['age', 'thalach', 'trestbps', 'chol', 'oldpeak']
numeric_features = df[numeric_feature_names]
print(numeric_features.head())

tensor = tf.convert_to_tensor(numeric_features)
print(tensor)
