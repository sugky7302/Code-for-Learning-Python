import tensorflow as tf 
tf.enable_eager_execution() # 將tensorflow改成命令式編程，使tensorflow函數會直接執行

a = tf.constant(1)
b = tf.constant(1)
c = a + b # 也可以寫 tf.add(a, b)

print(c)

A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])
C = tf.matmul(A, B) # matmul = matrix multiple

print(C)