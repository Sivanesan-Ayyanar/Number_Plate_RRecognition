import cv2
from PIL import Image
from pytesseract import pytesseract

def tesseract(image_path):
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


    # Convert the OpenCV image to PIL Image
    pil_image = Image.fromarray(cv2.cvtColor(image_path, cv2.COLOR_BGR2RGB))

    # Use pytesseract to do OCR on the PIL Image
    text = pytesseract.image_to_string(pil_image)
    print(text[:-1])

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    _, image = camera.read()
    cv2.imshow('Text detection', image)

    # Break the loop if 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test1.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()

# Call tesseract function after capturing and saving the image
tesseract(image)
