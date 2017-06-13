# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys
import os

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
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")

    compare_output(s)

    # show the images
    plt.show()


def compare_output(s):
    global correct_counter
    if(s > .40):
        sys.stdout.write("same person | ")
        correct_counter = correct_counter + 1
    print correct_counter



# load the images -- the zero, the zero + one,
# and the zero + photoshop
zero = cv2.imread("images/margot1.jpg")
one = cv2.imread("images/margot2.jpg")
two = cv2.imread("images/jesse2.jpg")

# convert the images to grayscale
zero = cv2.cvtColor(zero, cv2.COLOR_BGR2GRAY)
one = cv2.cvtColor(one, cv2.COLOR_BGR2GRAY)
two = cv2.cvtColor(two, cv2.COLOR_BGR2GRAY)
three = cv2.cvtColor(three, cv2.COLOR_BGR2GRAY)
four = cv2.cvtColor(four, cv2.COLOR_BGR2GRAY)
five = cv2.cvtColor(five, cv2.COLOR_BGR2GRAY)
six = cv2.cvtColor(six, cv2.COLOR_BGR2GRAY)
seven = cv2.cvtColor(seven, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("zero", zero), ("first", one), ("second", two), ("third", three), ("fouth", four), ("five", five), ("six", six), ("seven", seven),


# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the images
compare_images(zero, zero, "Original vs. Original")
compare_images(zero, one, "Original vs. Contrast")
compare_images(zero, two, "Original vs. Phototwo")


#def many_pictures():
#    for filename in os.listdir(images):
#        if filename.endswith(".jpg") or filename.endswith(".png"):
#            print(os.path.join(images, filename))
#            continue
#        else:
#            continue





#many_pictures()
