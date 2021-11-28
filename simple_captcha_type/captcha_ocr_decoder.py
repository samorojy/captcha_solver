from PIL import Image
import pytesseract
import captcha_letters_cutter

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def ocr_method_decoder(image_path):
    image = Image.open(image_path)
    captcha_letters_cutter.clear_noise(image)
    text = pytesseract.image_to_string(image, lang='eng')
    return "".join(filter(str.isalpha, text))
