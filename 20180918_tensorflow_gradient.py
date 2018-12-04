import tensorflow as tf 
tf.enable_eager_execution() 

x = tf.get_variable('x', shape=[1], initializer = tf.constant_initializer(3.))
with tf.GradientTape() as tape:
    y = tf.square(x)

y_grad = tape.gradient(y, x)
print([y.numpy(), y_grad.numpy()])

X = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
w = tf.get_variable('w', shape=[2, 1], initializer = tf.constant_initializer([[1.], [2.]]))
b = tf.get_variable('b', shape = [1], initializer = tf.constant_initializer([1.]))
with tf.GradientTape() as tape:
    L = 0.5 * tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))

w_grad, b_grad = tape.gradient(L, [w, b]) # 計算L(w, b) 關於w, b的偏導數
print([L.numpy(), w_grad.numpy(), b_grad.numpy()])
