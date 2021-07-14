from quickdraw import QuickDrawData
import cv2
import numpy as np

def draw_raccoon():
   for x in range(5):
        qd = QuickDrawData()
        racoon = qd.get_drawing("raccoon")
        racoon.image.save("raccoon" + str(x) + ".png")

     #img = cv2.imread('my_cake6.png', cv2.IMREAD_UNCHANGED)

     # convert img to grey
    # img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # set a thresh
    # thresh = 100
    # # get threshold image
    # ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
    # # find contours
    # contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #
    # # create an empty image for contours
    # img_contours = np.zeros(img.shape)
    # # draw the contours on the empty image
    # cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 3)
    # # save image
    # cv2.imwrite('contourCake6.png', img_contours)

        print(racoon)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    draw_raccoon()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
