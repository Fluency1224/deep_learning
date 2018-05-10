import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("C:/Users/fluency/Desktop/workspace/python3.6/Deep-Learning/TensorFlow_API_study/MNIST_data/", one_hot=True)

print(mnist)

x = tf.placeholder("float", [None, 784])
#权重  bias偏置量
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,10])
#计算交叉熵:
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#用梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#初始化变量
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
  
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))