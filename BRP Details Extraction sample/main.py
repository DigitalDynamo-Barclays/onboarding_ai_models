import cv2
import pytesseract
import json

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# use sharp
img = cv2.imread('Sherlock-BRP.jpg')


text = pytesseract.image_to_string(img)


x, y, w, h = (375, 5, 90, 20)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('image', img)
roi = img[y:y+h, x:x+w]
name = pytesseract.image_to_string(roi)
print("Unique BRP Number", name.split())


x, y, w, h = (150, 52, 120, 30)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('image', img)
roi = img[y:y+h, x:x+w]
name = pytesseract.image_to_string(roi)
print("Name", name.split())


x, y, w, h = (150, 90, 100, 20)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('image', img)
roi = img[y:y+h, x:x+w]
name = pytesseract.image_to_string(roi)
print("Name", name.split())


cv2.waitKey(0)
cv2.destroyAllWindows()
