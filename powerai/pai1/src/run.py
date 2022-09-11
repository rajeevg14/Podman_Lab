import tensorflow as tf
# bellow two rows are for TF1.x compatibility mode in TF2.x - don't use them with TF1.x
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
hello = tf.constant('Hello, TensorFlow!')
# Start tf session
sess = tf.Session()
# Run the op
print(sess.run(hello))
print("GPU IS: " + tf.test.gpu_device_name())
print(tf.__version__)
