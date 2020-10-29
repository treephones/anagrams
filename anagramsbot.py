import cv2
from screenshot import Screenshot
import pytesseract
import numpy as np

def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

capture = Screenshot("LonelyScreen AirPlay Receiver")
print("Press 's' when you are on the screen with the letters visible:")

while True:
    frame = capture.get_frame();
    cv2.imshow("Screen", frame)

    if cv2.waitKey(1) == ord('s'):
        cv2.destroyAllWindows()
        break

frame = cv2.cvtColor(capture.crop(frame), cv2.COLOR_BGR2GRAY)
frame = threshold(frame)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Moez\AppData\Local\Tesseract-OCR\tesseract.exe'

config = r'--oem 3 --psm 6'
letters = pytesseract.image_to_string(frame, config=config)
print(letters)

#show image after done
while True:
    cv2.imshow("swgg", frame)
    if cv2.waitKey(1) == ord('s'):
        cv2.destroyAllWindows()
        break


