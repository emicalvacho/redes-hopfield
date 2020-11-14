import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob

from interface.plotter import showPattern, showPatterns
from operations.hopfield import learn, searchPattern

def main():
    pattern_width = 5
    pattern_height = 5

    images = [cv2.imread(file) for file in glob.glob("images/alphabet/*.png")]
    vectors = []

    for i in images:
        img = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        img = cv2.bitwise_not(img)
        image = img.flatten()
        image = image/255
        vectors.append(image)

    for j in vectors:
        for i in range(j.shape[0]):
            if j[i] == 0:
                j[i] = -1

    patterns = np.array(vectors)   
    showPatterns(pattern_width,pattern_height,patterns)

    generalWeightMatrix = learn(pattern_width, pattern_height, patterns)

    print(generalWeightMatrix)

    test = cv2.imread('images/test/test04.png')
    img = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    img = cv2.bitwise_not(img)
    imgTest = img.flatten()
    imgTest = imgTest/255

    for i in range(imgTest.shape[0]):
        if imgTest[i] == 0:
            imgTest[i] = -1

    showPattern(pattern_width, pattern_height, imgTest, "incompleto")

    patronAsociado = searchPattern(imgTest, generalWeightMatrix)
    showPattern(pattern_width, pattern_height, patronAsociado, "asociado")


if __name__ == "__main__":
    main()