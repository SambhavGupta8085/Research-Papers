import tensorflow as tf

# Check if GPU is detected
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))

# Show GPU details
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
