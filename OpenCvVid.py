import numpy as np
import cv2

count=0
array=[]

vid='/vol/vssp/smile/chewing/MEET/108_1130/MVI_0023.MP4'
cap = cv2.VideoCapture(vid)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)

    count+=1

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break
    if cv2.waitKey(15) & 0xFF == ord(' '):
        array.append(count)

cap.release()
cv2.destroyAllWindows()


name = vid[-12:-4]
f = open(name, 'w+')
#map int array to str array
map(str, array)
f.write(" \n".join(str (elem) for elem in array) + "\n")
