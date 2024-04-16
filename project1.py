import pytesseract
import numpy
from PIL import Image
#import cv2
from PIL import ImageEnhance
from fpdf import FPDF
import PyPDF2
pdf = FPDF()
import os 
#correct guesses:1,19
# Path to the tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\anant_l1e8kp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
image_list=[]
unit=[]

def extract_page_number(image_path):
    # Open the image file
    image = Image.open(image_path)
    image = image.convert('L')

    #image preprocessing
    original_width, original_height = image.size
    image = image.resize((original_width, original_height))

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    # Perform OCR to extract the text from the image
    extracted_text = pytesseract.image_to_string(image)#to_data
    image = image.convert('L')
    
    # Search for the page number within the extracted text
    page_number = None
    for word in extracted_text.split():
        if word.isdigit():
            page_number = int(word)
            break
    
    return page_number

# Provide the path to your uploaded image
image_files = list(sorted(os.listdir('images')))
# Call the function to extract the page number

for i in image_files:
    page_number = extract_page_number("images/" + str(i))
    if page_number is not None:
       unit=[i,page_number]
       image_list.append(unit)
       pass
sorted_list = sorted(image_list, key=lambda x:x[1])
sorted_images=numpy.take(sorted_list,0,axis=1)
print(sorted_list)
for z in sorted_images:
 pdf.add_page()
 i="images\\"+z
 pdf.image(i)
pdf.output("output.pdf") 









"""import os
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the directory path containing the images
image_dir ='images'

# Get a list of image file names in the directory
image_files = sorted(os.listdir(image_dir))
print(image_files)
# Define a regular expression pattern to extract page numbers from image file names
page_number_pattern = r'\d+'

# Create a list to store tuples of (page number, image file name)
image_pages = []

# Iterate over the image files and extract the page numbers
for image_file in image_files:
    page_number = re.findall(page_number_pattern, image_file)
    if page_number:
        page_number = int(page_number[0])
        image_pages.append((page_number, image_file))

# Sort the list of image pages based on the page number
image_pages = sorted(image_pages, key=lambda x: x[0])
print(image_pages)
# Create a figure to display the arranged images
fig = plt.figure()

# Iterate over the sorted image pages and display the images
for idx, (page_number, image_file) in enumerate(image_pages):
    # Read the image
    image_path = os.path.join(image_dir, image_file)
    image = cv2.imread(image_path)
    
    # Display the image in a subplot
    subplot = fig.add_subplot(len(image_pages), 1, idx+1)
    subplot.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    subplot.set_title(f'Page {page_number}')
    subplot.axis('off')

# Adjust the spacing between subplots
fig.tight_layout()

# Show the arranged images
plt.show()
"""