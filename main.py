import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while (capture.isOpened) :
  frame, image = capture.read()

  image = cv2.resize(image, (640, 480))
  frame = cv2.resize(frame, (640, 480))

  lBlack = np.array([30, 30, 0])
  uBlack = np.array([104, 153, 70])

  mask = cv2.inRange(image, lBlack, uBlack)
  video = cv2.bitwise_and(frame, frame, mask=mask)

  f = frame - video
  f = np.where(f==0, frame, f)

  cv2.imshow("real", image)
  cv2.imshow("mask", f)
  cv2.waitKey(1)
  if cv2.waitKey(1) & 0xFF == ord('q') :
    break

capture.release()
cv2.destroyAllWindows()