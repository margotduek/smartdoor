# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
import os
from PIL import Image

correct_counter = 0


def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)


    # setup the figure
    # fig = plt.figure(title)
    # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    # ax = fig.add_subplot(1, 2, 1)
    # plt.imshow(imageA, cmap = plt.cm.gray)
    # plt.axis("off")

    # show the second image
    # ax = fig.add_subplot(1, 2, 2)
    # plt.imshow(imageB, cmap = plt.cm.gray)
    # plt.axis("off")

    compare_output(s)

    # show the images
    # plt.show()


def compare_output(s):
    global correct_counter
    if(s > .45):
        correct_counter = correct_counter + 1


def each_owner():
    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    max_accuracy = 0
    name = ''
    for fn in os.listdir('./images/new/'):
        if fn[-3:] == 'jpg':
            num_pics = 0
            for old_photo in os.listdir('./images/jesse/'):
                if old_photo[-3:] == 'jpg':
                    original = cv2.imread("images/jesse/" + old_photo)
                    new = cv2.imread("images/new/" + fn)
                    # loop over the images

                    # convert the images to grayscale
                    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                    new = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)

                    # initialize the figure
                    fig = plt.figure("Images")
                    images = ("Original", original), ("New", new)
                    num_pics += 1

                    compare_images(original, new, "Original vs. New")
            if float(correct_counter / num_pics) > .5:
                if float(correct_counter / num_pics) > max_accuracy:
                    max_accuracy = float(correct_counter / num_pics)
                    name = "Jesse"

    for fn in os.listdir('./images/new/'):
        if fn[-3:] == 'jpg':
            num_pics = 0
            for old_photo in os.listdir('./images/margot/'):
                if old_photo[-3:] == 'jpg':
                    original = cv2.imread("images/margot/" + old_photo)
                    new = cv2.imread("images/new/" + fn)
                    # loop over the images

                    # convert the images to grayscale
                    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                    new = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)

                    # initialize the figure
                    fig = plt.figure("Images")
                    images = ("Original", original), ("New", new)
                    num_pics += 1

                    compare_images(original, new, "Original vs. New")
            if float(correct_counter / num_pics) > .5:
                if float(correct_counter / num_pics) > max_accuracy:
                    max_accuracy = float(correct_counter / num_pics)
                    name = "Margot"


    # load the images -- the original, the original + contrast,
    # and the original + photoshop
    for fn in os.listdir('./images/new/'):
        if fn[-3:] == 'jpg':
            num_pics = 0
            for old_photo in os.listdir('./images/saul/'):
                if old_photo[-3:] == 'jpg':
                    original = cv2.imread("images/saul/" + old_photo)
                    new = cv2.imread("images/new/" + fn)
                    # loop over the images

                    # convert the images to grayscale
                    original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                    new = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)

                    # initialize the figure
                    fig = plt.figure("Images")
                    images = ("Original", original), ("New", new)
                    num_pics += 1

                    compare_images(original, new, "Original vs. New")
            if float(correct_counter / num_pics) > .5:
                if float(correct_counter / num_pics) > max_accuracy:
                    max_accuracy = float(correct_counter / num_pics)
                    name = "Saul"

    # load the images -- the original, the original + contrast,
    # and the original + photoshop
	return name




print each_owner()
# show the figure
#plt.show()
