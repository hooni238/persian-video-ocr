from inspect import currentframe
import cv2
import pytesseract
import sys
rer = ""


def ocr(frame):
    global rer
    text = pytesseract.image_to_string(frame, lang='fas') # if you are using another language change lang part
    if (rer != text):
        f.write(text)
        rer = text
    
if len(sys.argv) == 2:
    inp_file = sys.argv[1]
else:
    print('You need to include a video.')
    exit(2)
f = open("output.txt", "w", encoding="utf-8")
vidcap = cv2.VideoCapture(inp_file)
success,image = vidcap.read()
currentframe = 0
while success:
    ocr(image)    
    success,image = vidcap.read()
    currentframe += 30 # i.e. at 30 fps, this advances one second
    vidcap.set(1, currentframe)
f.close()
print("done")
