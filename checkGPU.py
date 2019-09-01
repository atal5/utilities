import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
with tf.Session() as sess:
  devices = sess.list_devices()
print(devices)
print('If GPU not visible try activating the python environment for Tensorflow-GPU')
