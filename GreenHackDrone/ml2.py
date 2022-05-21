

import tensorflow
import keras

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "1273c149b0fb45058cbe04a905596ae8"
endpoint = "https://greenhack.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
g_drive_test_url="https://drive.google.com/uc?id=187CXrRIM01QYGWurVhDRctE3nNZYm6p0"

remote_image_features = ["categories","brands","adult","color","description","faces","image_type","objects","tags"]
remote_image_features = None
remote_image_details = ["landmarks"]

# Call API with URL and features
results_remote = computervision_client.analyze_image(remote_image_url, ["objects"]) #(remote_image_url , remote_image_features, remote_image_details)

# Print results with confidence score
print("Categories from remote image: ")
if (len(results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in results_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))
print()

# Detect faces
# Print the results with gender, age, and bounding box
#print("Faces in the remote image: ")
#if (len(results_remote.faces) == 0):
#    print("No faces detected.")
#else:
#    for face in results_remote.faces:
#        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
#        face.face_rectangle.left, face.face_rectangle.top, \
#        face.face_rectangle.left + face.face_rectangle.width, \
#        face.face_rectangle.top + face.face_rectangle.height))
#
## Adult content
## Print results with adult/racy score
#print("Analyzing remote image for adult or racy content ... ")
#print("Is adult content: {} with confidence {:.2f}".format(results_remote.adult.is_adult_content, results_remote.adult.adult_score * 100))
#print("Has racy content: {} with confidence {:.2f}".format(results_remote.adult.is_racy_content, results_remote.adult.racy_score * 100))
#print()
#
## Detect colors
## Print results of color scheme
#print("Getting color scheme of the remote image: ")
#print("Is black and white: {}".format(results_remote.color.is_bw_img))
#print("Accent color: {}".format(results_remote.color.accent_color))
#print("Dominant background color: {}".format(results_remote.color.dominant_color_background))
#print("Dominant foreground color: {}".format(results_remote.color.dominant_color_foreground))
#print("Dominant colors: {}".format(results_remote.color.dominant_colors))
#print()
#
## Detect image type
## Prints type results with degree of accuracy
#print("Type of remote image:")
#if results_remote.image_type.clip_art_type == 0:
#    print("Image is not clip art.")
#elif results_remote.image_type.line_drawing_type == 1:
#    print("Image is ambiguously clip art.")
#elif results_remote.image_type.line_drawing_type == 2:
#    print("Image is normal clip art.")
#else:
#    print("Image is good clip art.")
#
#if results_remote.image_type.line_drawing_type == 0:
#    print("Image is not a line drawing.")
#else:
#    print("Image is a line drawing")

## Detect brands
#print("Detecting brands in remote image: ")
#if len(results_remote.brands) == 0:
#    print("No brands detected.")
#else:
#    for brand in results_remote.brands:
#        print("'{}' brand detected with confidence {:.1f}% at location {}, {}, {}, {}".format( \
#        brand.name, brand.confidence * 100, brand.rectangle.x, brand.rectangle.x + brand.rectangle.w, \
#        brand.rectangle.y, brand.rectangle.y + brand.rectangle.h))

# Detect objects
# Print detected objects results with bounding boxes
print("Detecting objects in remote image:")
if len(results_remote.objects) == 0:
    print("No objects detected.")
else:
    for object in results_remote.objects:
        print("object at location {}, {}, {}, {}".format( \
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))


# Describe image
# Get the captions (descriptions) from the response, with confidence level
print("Description of remote image: ")
if (len(results_remote.description) == 0):
    print("No description detected.")
else:
    for caption in results_remote.description:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()

# Return tags
# Print results with confidence score
print("Tags in the remote image: ")
if (len(results_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in results_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

# Detect celebrities
print("Celebrities in the remote image:")
if (len(results_remote.categories.detail.celebrities) == 0):
    print("No celebrities detected.")
else:
    for celeb in results_remote.categories.detail.celebrities:
        print(celeb["name"])

# Detect landmarks
print("Landmarks in the remote image:")
if len(results_remote.categories.detail.landmarks) == 0:
    print("No landmarks detected.")
else:
    for landmark in results_remote.categories.detail.landmarks:
        print(landmark["name"])
