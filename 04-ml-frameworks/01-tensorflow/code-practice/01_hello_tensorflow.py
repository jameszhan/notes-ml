# -*- coding: utf-8 -*-
import tensorflow as tf

if __name__ == '__main__':
    hello = tf.constant('Hello, Tensorflow!')
    with tf.Session() as sess:
        ret = sess.run(hello)
        print(ret)
