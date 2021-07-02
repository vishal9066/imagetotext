import cv2
import pytesseract
import Image_Location

class Extract_data:
    def return_string(self,location):
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
        img = cv2.imread(location)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img).strip()


