import serial
from itertools import permutations
from time import sleep
s = serial.Serial(
        port='COM5',
        baudrate=9600
        )

coords = {}
letters = "irenns"
for i in range(6):
    if letters[i] not in coords:
        coords[letters[i]] = i*20
    else:
        coords[f'{letters[i]}2'] = i*20
print(coords)

words = ["nsreni"]
curr = 0
track = []
for word in words:
    for letter in word:
        if letter not in track:
            s.write(str(coords[letter] - curr).encode())
            curr = coords[letter]
        else:
            s.write(str(coords[f'{letter}2'] - curr).encode())
            curr = coords[f'{letter}2']
        track.append(letter)
        sleep(2)
    curr = 0
    track = []
    s.write('5'.encode())