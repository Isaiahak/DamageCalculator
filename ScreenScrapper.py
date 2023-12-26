import pytesseract

from PIL import Image



def main():
    image = 'damageValues.png'
    text = pytesseract.image_to_string(image,lang='eng')
    print(text)
    
main()