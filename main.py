from PIL import Image
import pytesseract
import os
from os import listdir
import csv
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# get the path or directory
folder_dir = "images"
header = ['Total', 'Subtotal', 'Delivery Fee', 'Order Fee']
finalList = []
for images in os.listdir(folder_dir):
    # check if the image ends with png or jpg or jpeg or jfif
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg") or images.endswith(".jfif")):
        # Simple image to string
        text = pytesseract.image_to_string(Image.open('images/'+images))
        without_empty_lines = os.linesep.join([
            line for line in text.splitlines()
            if line.strip() != ''
        ])
        text_array = without_empty_lines.splitlines()
        matchesTotal = []
        matchesSubtotal = []
        matchesDelivery = []
        matchesOrder = []
        currentList = []
        for match in text_array:
            if "Total" in match:
                matchesTotal.append(match)
        finalString = ' '.join(matchesTotal)
        lastWord = finalString.split()
        currentList.append(lastWord[-1])
        for match in text_array:
            if "Subtotal" in match:
                matchesSubtotal.append(match)
        finalString = ' '.join(matchesSubtotal)
        lastWord = finalString.split()
        currentList.append(lastWord[-1])
        for match in text_array:
            if "Delivery" in match:
                matchesDelivery.append(match)
        finalString = ' '.join(matchesDelivery)
        lastWord = finalString.split()
        currentList.append(lastWord[-1])
        for match in text_array:
            if "Order" in match:
                matchesOrder.append(match)
        finalString = ' '.join(matchesOrder)
        lastWord = finalString.split()
        currentList.append(lastWord[-1])
        finalList.append(currentList)

with open('grabfoodreceipt.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(finalList)
