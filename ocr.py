from PIL import Image
import pytesseract


def image_to_text(img):
    text  = pytesseract.image_to_string(img)
    text = text.replace('\n', ' ').replace("/\s\s+/g", ' ').strip()

    return text