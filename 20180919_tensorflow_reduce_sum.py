import tensorflow as tf 
tf.enable_eager_execution()

x = tf.constant([[[[1, 2], [3, 4]]], [[[3, 4], [5, 6]]]]) # 維度為2x1x2x2
ans1 = tf.reduce_sum(x, axis = 0)
ans2 = tf.reduce_sum(x, axis = 1)
ans3 = tf.reduce_sum(x, axis = 2)
ans4 = tf.reduce_sum(x, axis = 3)
print([ans1.numpy(), ans2.numpy(), ans3.numpy(), ans4.numpy()])