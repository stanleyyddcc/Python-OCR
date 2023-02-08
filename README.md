# Python OCR to extract data from Grabfood receipts
## Background
Business team want to analyze consumers behavior in Grabfood application, but they have to manually input consumers spending by inputting consumer spending from Grabfood receipt to Excel. There are estimated 3,000 Grabfood receipts, so it takes too long and prone to human error in inputting data.
## Solution
1. Create scrape system that get selected data from image using OCR and Python Tesseract.
2. Export all the data into csv files.
## Installation
1. Download Tesseract [download](https://github.com/tesseract-ocr/tessdoc#binaries) <br>
2. Install Python OCR library
````
pip install pytesseract
````
