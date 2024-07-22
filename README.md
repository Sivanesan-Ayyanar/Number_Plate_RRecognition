# Number Plate Recognition Project

This project captures images from a webcam, performs Optical Character Recognition (OCR) using Tesseract to extract number plate details, and saves the information in an Excel file.

## Prerequisites

Make sure you have the following software and libraries installed:

- Python 3.x
- OpenCV
- Pillow
- pytesseract
- openpyxl
- Tesseract OCR (Download from [here](https://github.com/tesseract-ocr/tesseract))

Install the necessary Python libraries using pip:

```bash
pip install opencv-python Pillow pytesseract openpyxl
```

## Usage

1. **Clone the repository**:

2. **Run the script**:
   
3. **Interact with the application**:
    - The webcam feed will open in a window.
    - Press 's' to capture an image and process the number plate.

4. **Output**:
    - The detected number plate details along with the state information will be printed.
    - The information will be saved in `number_plates.xlsx`.

## Script Overview

### `tesseract(image_path)`
Converts an image to a PIL image and performs OCR using Tesseract to extract text.

### `get_state_code(number_plate)`
Maps the number plate's state code to the corresponding state name.

### `clean_number_plate(number_plate)`
Cleans the number plate text by removing special characters and brackets.

### Main Script
- Captures images from the webcam.
- Performs OCR on the captured image.
- Cleans the detected number plate text.
- Maps the number plate to the corresponding state.
- Saves the details in an Excel file.

## Dependencies

- [OpenCV](https://opencv.org/)
- [Pillow](https://python-pillow.org/)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [openpyxl](https://openpyxl.readthedocs.io/)

