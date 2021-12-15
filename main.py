import cv2
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
easy = cv2.imread('images/text.png', 3)
surf = cv2.imread('images/surf.jpg', 0)
view = cv2.imread('images/view.jpg', 3)


print(pytesseract.image_to_string(easy))
print()
print(pytesseract.image_to_string(surf))
print()
print(pytesseract.image_to_string(view))
