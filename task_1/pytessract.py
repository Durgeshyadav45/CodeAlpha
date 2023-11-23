import pytesseract 
import pyttsx3
from PIL import Image
from googletrans import Translator
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

a=int(input('enter your choice from 1 to 3'))

if a==1:
    img1=Image.open('im1.png')
    print(img1)
    result=pytesseract.image_to_string(img1)
    with open('abc.text',mode='w') as file:
        file.write(result)
        print(result)
    tts = gTTS(result)
    tts.save("output.mp3")
    os.system("start output.mp3")

elif a==2:
    img2=Image.open('im2.png')
    print(img2)
    result=pytesseract.image_to_string(img2)
    with open('abc.text',mode='w') as file:
        file.write(result)
        print(result)
    tts = gTTS(result)
    tts.save("output.mp3")
    os.system("start output.mp3")

elif a==3:
    img3=Image.open('img3.jpg')
    print(img3)
    result=pytesseract.image_to_string(img3)
    with open('abc.text',mode='w') as file:
        file.write(result)
        print(result)
    tts = gTTS(result)
    tts.save("output.mp3")
    os.system("start output.mp3")

else:
    print("wrong choice")


