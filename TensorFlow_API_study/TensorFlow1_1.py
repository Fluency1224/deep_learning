import numpy as np
import tensorflow as tf

# numpy set phony data
x_data = np.float32(np.random.rand(2,100))
y_data = np.dot([0.100, 0.200], x_data) + 0.300

#strut line demo

b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 300):
    sess.run(train)
    if step % 20 == 0:
        print (step, sess.run(W), sess.run(b))