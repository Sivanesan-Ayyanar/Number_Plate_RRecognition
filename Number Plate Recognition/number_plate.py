import cv2
from PIL import Image
from pytesseract import pytesseract
import openpyxl
from openpyxl import Workbook
import re


def get_state_code(number_plate):
    state_codes = {
        'AN': 'Andaman and Nicobar Islands',
        'AP': 'Andhra Pradesh',
        'AR': 'Arunachal Pradesh',
        'AS': 'Assam',
        'BH': 'Bharat (For pan-India registration)',
        'BR': 'Bihar',
        'CH': 'Chandigarh',
        'CG': 'Chhattisgarh',
        'DD': 'Dadra and Nagar Haveli and Daman and Diu',
        'DL': 'Delhi',
        'GA': 'Goa',
        'GJ': 'Gujarat',
        'HR': 'Haryana',
        'HP': 'Himachal Pradesh',
        'JK': 'Jammu and Kashmir',
        'JH': 'Jharkhand',
        'KA': 'Karnataka',
        'KL': 'Kerala',
        'LA': 'Ladakh',
        'LD': 'Lakshadweep',
        'MP': 'Madhya Pradesh',
        'MH': 'Maharashtra',
        'MN': 'Manipur',
        'ML': 'Meghalaya',
        'MZ': 'Mizoram',
        'NL': 'Nagaland',
        'OD': 'Odisha',
        'PY': 'Puducherry',
        'PB': 'Punjab',
        'RJ': 'Rajasthan',
        'SK': 'Sikkim',
        'TN': 'Tamil Nadu',
        'TS': 'Telangana',
        'TR': 'Tripura',
        'UP': 'Uttar Pradesh',
        'UK': 'Uttarakhand',
        'WB': 'West Bengal',
    }

    state_code = number_plate[:2]
    state = state_codes.get(state_code, 'Unknown')
    return state


def tesseract(image_path):
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Convert the OpenCV image to PIL Image
    pil_image = Image.fromarray(cv2.cvtColor(image_path, cv2.COLOR_BGR2RGB))

    # Use pytesseract to do OCR on the PIL Image
    text = pytesseract.image_to_string(pil_image)
    return text.strip()


def clean_number_plate(number_plate):
    # Remove special characters and brackets (excluding spaces) using regular expressions
    cleaned_plate = re.sub(r'[^\w\s]', '', number_plate)
    return cleaned_plate


# Initialize the camera
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Create a new Excel workbook and add a sheet
wb = Workbook()
sheet = wb.active
sheet.title = 'Number Plates'
sheet['A1'] = 'S.No'
sheet['B1'] = 'Number Plate'
sheet['C1'] = 'State'

# Counter for Serial Number
serial_number = 1

while True:
    # Read a frame from the camera
    _, image = camera.read()

    # Display the frame
    cv2.imshow('Number Plate Recognition', image)

    # Break the loop if 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the captured image as 'test1.jpg'
        cv2.imwrite('test1.jpg', image)

        # Call the tesseract function after capturing and saving the image
        detected_plate = tesseract(cv2.imread('test1.jpg'))

        # Clean the detected number plate (remove special characters and brackets, excluding spaces)
        cleaned_plate = clean_number_plate(detected_plate)

        # Get the state information based on the cleaned number plate
        state = get_state_code(cleaned_plate)

        # Print the detected text
        print(
            f"S.No: {serial_number}, Number Plate Details: {cleaned_plate}, State: {state}")

        # Add the cleaned number plate, serial number, and state to the Excel sheet
        sheet.append([serial_number, cleaned_plate, state])

        # Increment the serial number
        serial_number += 1

        # Save the Excel workbook
        wb.save('number_plates.xlsx')

        break

# Release the camera
camera.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
