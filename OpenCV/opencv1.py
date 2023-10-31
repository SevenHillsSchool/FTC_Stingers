import cv2
img_test = cv2.imread('assets/test_img.png', -1)
img_test = cv2.resize(img_test, (0,0), fx=0.5, fy=0.5)
img_test = cv2.rotate(img_test, cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite('new_img.png', test_img
cv2.imshow('image', img_test)
cv2.waitKey(0)
cv2.destroyAllWindows()
