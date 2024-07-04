import os 
import json
from PIL import Image
import google.generativeai as genai

working_directory = os.path.dirname(os.path.abspath(__file__))
config_path = f"{working_directory}/config.json"

config_data = json.load(open(config_path))

GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configuring the google.generativeai with API
genai.configure(api_key=GOOGLE_API_KEY)

def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel('gemini-pro')
    return gemini_pro_model

def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result



image = Image.open('jurasic_park.jpg')  # Corrected typo in image filename

prompt = "Write a short caption for the image"

output = gemini_pro_vision_response(prompt, image)

print(output)
