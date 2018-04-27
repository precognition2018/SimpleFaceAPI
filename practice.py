import tensorflow as tf

x = tf.placeholder(tf.float32, [None,3])

x_data = [[1,2,3],[4,5,6]]

w = tf.Variable(tf.random_normal([3,2]))
b = tf.Variable(tf.random_normal([2,1]))

expr = tf.matmul(x,w) + b

sess = tf.Session()
sess.run(tf.global_variables_initializer())


print(x_data)
print(sess.run(w))
print(sess.run(b))
