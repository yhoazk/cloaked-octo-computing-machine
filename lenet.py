"""
LeNet Architecture

HINTS for layers:

    Convolutional layers:

    tf.nn.conv2d
    tf.nn.max_pool

    For preparing the convolutional layer output for the
    fully connected layers.

    tf.contrib.flatten
"""
import tensorflow as tf
from tensorflow.contrib.layers import flatten
import pickle
import numpy as np

#EPOCHS = 35
EPOCHS = 50
BATCH_SIZE = 1200
KEEP_PROB = 0.5
X_data = np.array([])
y_labels = np.array([])

num_examples = int()


def find_diff(correct, predicted):
    """
    Returns a list of tuples containing index, predicted, correct information
    """
    differences = []
    if len(correct) != len(predicted):
        print("the lists must have the same length")
    else:
        for i in range(len(predicted)):
            if correct[i] != predicted[i]:
                differences.append((i, predicted[i], correct[i]))

        return differences




def getDataset():
    global X_data
    global y_labels
    global num_examples

    X_data = pickle.load(open("../extended_bw_data.p","rb"))
    y_labels = pickle.load(open("../extended_bw_labels.p","rb"))
    num_examples = len(X_data)
    print("Num_Examples: " + str(num_examples))

# LeNet architecture:
# INPUT -> CONV -> ACT -> POOL -> CONV -> ACT -> POOL -> FLATTEN -> FC -> ACT -> FC
#
# Don't worry about anything else in the file too much, all you have to do is
# create the LeNet and return the result of the last fully connected layer.
def LeNet(x):
    # Reshape from 2D to 4D. This prepares the data for
    # convolutional and pooling layers.
    #x = tf.reshape(x, (-1, 32, 32, 1))
    # Pad 0s to 32x32. Centers the digit further.
    # Add 2 rows/columns on each side for height and width dimensions.
    #x = tf.pad(x, [[0, 0], [2, 2], [2, 2], [0, 0]], mode="CONSTANT")
    global KEEP_PROB
    # Hyperparameters
    mu = 0
    sigma = 0.1

    # SOLUTION: Convolution Layer 1. Input = 32x32x3. Output = 28x28x6.
    conv1_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 1, 6), mean = mu, stddev = sigma))
    conv1_b = tf.Variable(tf.zeros(6))
    conv1   = tf.nn.conv2d(x, conv1_W, strides=[1, 1, 1, 1], padding='VALID') + conv1_b

    # SOLUTION: Activation 1.
    conv1 = tf.nn.relu(conv1)
    #conv1 = tf.nn.elu(conv1)
    conv1 = tf.nn.dropout(conv1, KEEP_PROB)
    # SOLUTION: Pooling Layer 1. Input = 28x28x6. Output = 14x14x6.
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # SOLUTION: Convolution Layer 2. Output = 10x10x16.
    conv2_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 6, 16), mean = mu, stddev = sigma))
    conv2_b = tf.Variable(tf.zeros(16))
    conv2   = tf.nn.conv2d(conv1, conv2_W, strides=[1, 1, 1, 1], padding='VALID') + conv2_b

    # SOLUTION: Activation 2.
    conv2 = tf.nn.relu(conv2)
    #conv2 = tf.nn.elu(conv2)

    conv2 = tf.nn.dropout(conv2, KEEP_PROB)
    # SOLUTION: Pooling Layer 2. Input = 10x10x16. Output = 5x5x16.
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # SOLUTION: Flatten Layer.
    fc1 = flatten(conv2)
    fc1_shape = (fc1.get_shape().as_list()[-1], 120)

    # SOLUTION: Fully Connected Layer 1. Input = 5x5x16. Output = 120.
    fc1_W     = tf.Variable(tf.truncated_normal(shape=(fc1_shape), mean = mu, stddev = sigma))
    fc1_b     = tf.Variable(tf.zeros(120))
    fc1       = tf.matmul(fc1, fc1_W) + fc1_b

    # SOLUTION: Activation 3.
    fc1 = tf.nn.relu(fc1)
    #fc1 = tf.nn.elu(fc1)

    # SOLUTION: Fully Connected Layer 2. Input = 120. Output = 10.
    fc2_W  = tf.Variable(tf.truncated_normal(shape=(120, 43), mean = mu, stddev = sigma))
    fc2_b  = tf.Variable(tf.zeros(43))
    logits = tf.matmul(fc1, fc2_W) + fc2_b

    return logits

# MNIST consists of 28x28x1, grayscale images
x = tf.placeholder(tf.float32, [None, 32,32,1])
# Classify over 10 digits 0-9
y = tf.placeholder(tf.float32, [None, 43])
fc2 = LeNet(x)

loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(fc2, y))
#opt = tf.train.AdamOptimizer(learning_rate=0.001)
opt = tf.train.AdamOptimizer(learning_rate=0.001)
train_op = opt.minimize(loss_op)
correct_prediction = tf.equal(tf.argmax(fc2, 1), tf.argmax(y, 1))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


def eval_data():
    """
    Given a dataset as input returns the loss and accuracy.
    """
    global num_examples
    global X_data
    global y_labels
    # If dataset.num_examples is not divisible by BATCH_SIZE
    # the remainder will be discarded.
    # Ex: If BATCH_SIZE is 64 and training set has 55000 examples
    # steps_per_epoch = 55000 // 64 = 859
    # num_examples = 859 * 64 = 54976
    #
    # So in that case we go over 54976 examples instead of 55000.
    steps_per_epoch = num_examples // BATCH_SIZE
    num_examples_l = steps_per_epoch * BATCH_SIZE
    total_acc, total_loss = 0, 0
    sess = tf.get_default_session()
    for step in range(steps_per_epoch):
        batch_x, batch_y = X_data[step*BATCH_SIZE: (step+1)* BATCH_SIZE], y_labels[step*BATCH_SIZE: (step+1)*BATCH_SIZE]
        loss, acc = sess.run([loss_op, accuracy_op], feed_dict={x: batch_x, y: batch_y})
        total_acc += (acc * batch_x.shape[0])
        total_loss += (loss * batch_x.shape[0])
    #print("Total loss: " + str(step * BATCH_SIZE) + " : "+ str((step+1)*BATCH_SIZE))
    #print( sess.run(tf.Print(fc2, [fc2], "fcs: "),feed_dict={x: batch_x}))
    #print( sess.run(tf.argmax(fc2,1),feed_dict={x: batch_x}))
    #print("-------------------")
    #print(np.argmax(batch_y, 1))
    return total_loss/num_examples_l, total_acc/num_examples_l


def eval_test():
    """
    Given a dataset as input returns the loss and accuracy.
    """
    # If dataset.num_examples is not divisible by BATCH_SIZE
    # the remainder will be discarded.
    # Ex: If BATCH_SIZE is 64 and training set has 55000 examples
    # steps_per_epoch = 55000 // 64 = 859
    # num_examples = 859 * 64 = 54976
    #
    # So in that case we go over 54976 examples instead of 55000.
    global KEEP_PROB
    KEEP_PROB = 1
    # pickle the test data
    data = pickle.load(open("../pp_test_gray.p","rb"))
    labels = pickle.load(open("../pp_test_labels_gray.p","rb"))

    X_test = data
    y_test = labels
    num_test = len(X_test)

    steps_per_epoch = num_test // BATCH_SIZE
    num_examples_l = steps_per_epoch * BATCH_SIZE
    total_acc, total_loss = 0, 0
    sess = tf.get_default_session()
    for step in range(steps_per_epoch):
        batch_x, batch_y = X_test[step*BATCH_SIZE: (step+1)* BATCH_SIZE], y_test[step*BATCH_SIZE: (step+1)*BATCH_SIZE]
        loss, acc = sess.run([loss_op, accuracy_op], feed_dict={x: batch_x, y: batch_y})
        total_acc += (acc * batch_x.shape[0])
        total_loss += (loss * batch_x.shape[0])
        #print("num_examples: " + str(loss))
        pred =  sess.run(tf.argmax(fc2,1),feed_dict={x: batch_x})
        actual = np.argmax(batch_y, 1)
        #diff = set(pred).intersection(actual)
        #print(diff)
        diff = find_diff(actual, pred)
        print("----------------------------<pred----------------------------------------------------")
        print(pred)
        print("-----------------------------pred>---------------------------------------------------")
        print("----------------------------<actual----------------------------------------------------")
        print(actual)
        print("-----------------------------actual>---------------------------------------------------")
        print(diff)
        print("-----------------------------<diff>---------------------------------------------------")
    #print("Total loss: " + str(step * BATCH_SIZE) + " : "+ str((step+1)*BATCH_SIZE))
    return total_loss/num_examples_l, total_acc/num_examples_l





if __name__ == '__main__':
    # Load data
    #mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    getDataset()
    print("Num Ex: " + str(num_examples))
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        steps_per_epoch = num_examples // BATCH_SIZE
        num_examples_l = steps_per_epoch * BATCH_SIZE
        print(steps_per_epoch)
        # Train model
        for i in range(EPOCHS):
            for step in range(steps_per_epoch):
                batch_x, batch_y = (X_data[i*BATCH_SIZE: (i+1)* BATCH_SIZE], y_labels[i*BATCH_SIZE: (i+1)*BATCH_SIZE])
                loss = sess.run(train_op, feed_dict={x: batch_x, y: batch_y})

            val_loss, val_acc = eval_data()
            print("EPOCH {} ...".format(i+1))
            print("Validation loss = {:.3f}".format(val_loss))
            print("Validation accuracy = {:.3f}".format(val_acc))
            print()

        # Evaluate on the test data
        test_loss, test_acc = eval_test()
        print("Test loss = {:.3f}".format(test_loss))
        print("Test accuracy = {:.3f}".format(test_acc))


