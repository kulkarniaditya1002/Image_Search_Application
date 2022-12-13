#Testing_image_match_algo.py
import fitz
import io
from PIL import Image
from numpy import asarray

# Open the PDF file using fitz.open()
file_in_pdf_format = fitz.open("sample_data/image_search_app/5283010215159332.pdf")

for page_number in range(len(file_in_pdf_format)):
    page = file_in_pdf_format[page_number]
    img_list = page.get_images()
    if len(img_list) == 0:
        print("There is no image on page ", page_number)
        pass
    for img_index, img in enumerate(page.get_images(), start=1):
        xref = img[0]
        base_img = file_in_pdf_format.extract_image(xref)
        img_bytes = base_img["image"]
        img_ext = base_img["ext"]
        image = Image.open(io.BytesIO(img_bytes))
        image.save(open(f"image{page_number + 1}_{img_index}.{img_ext}", "wb"))

image = Image.open('/content/sample_data/image_search_app/IMG_20221207_195812.jpg')
input_image = asarray(image)

# Using Inception V3
import tensorflow as tf
from keras.applications import InceptionV3

# Load the Inception V3 model
model = InceptionV3(weights='imagenet')

# Use the Inception V3 model to predict the class of the input image
predictions = model.predict(input_image)

# Find the image in the PDF document that most closely matches the input image
# using the predicted class and the Inception V3 model's feature vector
matching_image = find_matching_image(predictions, preprocess_input.pdf_file)

# Print the file path of the matching image
print(matching_image)