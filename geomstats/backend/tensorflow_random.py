"""Tensorflow based random backend."""

import tensorflow as tf


def randint(low, high=None, size=None):
    if size is None:
        size = (1,)
    maxval = high
    minval = low
    if high is None:
        maxval = low - 1
        minval = 0
    return tf.random_uniform(
            shape=size,
            minval=minval,
            maxval=maxval, dtype=tf.int32, seed=None, name=None)


def rand(*args):
    return tf.random_uniform(shape=args)


def seed(*args):
    return tf.set_random_seed(*args)
