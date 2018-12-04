import numpy as np
import tensorflow as tf 

coefficient = np.array([[1.], [-20.], [100.]])

w = tf.Variable(0, dtype = tf.float32)
x = tf.placeholder(tf.float32, [3, 1])
# cost = tf.add(tf.add(w ** 2, tf.multiply(-10., w)), 25)
# cost = w ** 2 - 10 * w + 25
cost = x[0][0] * w ** 2 + x[1][0] * w + x[2][0]
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
train = tf.train.AdamOptimizer(0.091).minimize(cost)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(w))
    sess.run(train, feed_dict = {x:coefficient})
    print(sess.run(w))
    for i in range(1000):
        sess.run(train, feed_dict = {x:coefficient})
    print(sess.run(w))
