from screenshot import Screenshot
from itertools import permutations
import cv2
import pytesseract
import json
import numpy as np

def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def get_all_words(string):
    string = string.lower()
    words = {
        6: [],
        5: [],
        4: [],
        3: []
    }

    def get_threes(string): #works because string is never larger than 6
        ret = []
        for i in range(len(string)):
            for j in range(len(string)):
                for k in range(len(string)):
                    comb = string[i] + string[j] + string[k]
                    if comb not in ret:
                        ret.append(comb)
        return ret

    def get_fours(string):
        ret = []
        for i in range(len(string)):
            for j in range(len(string)):
                for k in range(len(string)):
                    for g in range(len(string)):
                        comb = string[i] + string[j] + string[k] + string[g]
                        if comb not in ret:
                            ret.append(comb)
        return ret

    def get_fives(string):
        ret, d = [], []
        for l in list(string):
            if l not in d:
                on = string.replace(l, "")
                d.append(l)
            ret += list(map(''.join, permutations(on)))
        return ret

    with open("engl_dict.json") as file:
        dict = json.load(file)

    possibs = list(map(''.join, permutations(string))) #largest
    possibs += get_fives(string)
    possibs += get_fours(string)
    possibs += get_threes(string)

    for p in possibs:
        try:
            if dict[p] == 1:
                dict[p] = 2  # already used
                words[len(p)].append(p)
        except KeyError:
            # not a word
            continue
    return words


capture = Screenshot("LonelyScreen AirPlay Receiver")
print("Press 's' when you are on the screen with the letters visible:")

while True:
    frame = capture.get_frame()
    cv2.imshow("Screen", frame)

    if cv2.waitKey(1) == ord('s'):
        cv2.destroyAllWindows()
        break

frame = cv2.cvtColor(capture.crop(frame), cv2.COLOR_BGR2GRAY)
frame = threshold(frame)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Moez\AppData\Local\Tesseract-OCR\tesseract.exe'

config = r'--oem 3 --psm 6'
letters = "".join(list(pytesseract.image_to_string(frame, config=config))[:-2])
all_words = get_all_words(letters)
#['C', 'S', 'L', 'O', 'A', 'E', '\n', '\x0c']

#show image after done
while True:
    cv2.imshow("swgg", frame)
    if cv2.waitKey(1) == ord('s'):
        cv2.destroyAllWindows()
        break


