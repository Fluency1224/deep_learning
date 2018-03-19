# /usr/bin/env python
# coding:utf-8
import tensorflow as tf
import tensorboard
import numpy as np


# 神经层
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name+'/weights',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
            #tf.histogtam_summary(lay_name + '/Wx_plus_b', Wx_plus_b)

        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs', outputs)
        return outputs


# 创建数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(1, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], 'x_inputs')
    ys = tf.placeholder(tf.float32, [None, 1], 'y_inputs')

# layer
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.softplus)
predition = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

# 预测
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition),
                                        reduction_indices=[1]))
    tf.summary.scalar('loss',loss)

# train
with tf.name_scope('train_step'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初始所有变量

sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("logs/", sess.graph)

sess.run(tf.initialize_all_variables())

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50 == 0:
        result = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(result,i)