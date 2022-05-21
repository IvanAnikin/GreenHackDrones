
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

images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
g_drive_test_url="https://drive.google.com/uc?id=187CXrRIM01QYGWurVhDRctE3nNZYm6p0"
g_drive_test_url2="https://drive.google.com/uc?id=1SJ4NpofgKb0R-JdGcukldbkaZQG4iRVv"


remote_image_url = g_drive_test_url2
print("===== Tag an image - remote =====")
tags_result_remote = computervision_client.tag_image(remote_image_url)
# Print results with confidence score
print("Tags in the remote image: ")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()
print("End of TAGGING")

print(VisualFeatureTypes.tags)
results_remote = computervision_client.analyze_image(remote_image_url, visual_features=[VisualFeatureTypes.tags])# "Objects")
print(results_remote)
for tag in results_remote.tags:
    print(tag)

detect_objects_response = computervision_client.detect_objects(remote_image_url)
print(detect_objects_response)
for detected_object in detect_objects_response.objects:
    print(detected_object)
    print(f"Detected object: {detected_object.object_property}")
    print(f"{detected_object.rectangle.h} {detected_object.rectangle.w} {detected_object.rectangle.x} {detected_object.rectangle.y}")

