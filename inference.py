import tensorflow as tf
import numpy as np
import json
import requests

SIZE = 128
MODEL_URI ='http://localhost:8501/v1/models/pets:predict'
CLASSES = ['Cat','Dog']

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size = (SIZE, SIZE)
    )
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis = 0)

    data = json.dumps({
    'instances': image.tolist()
    })
    response = requests.post(MODEL_URI, data =data.encode())
    result = json.loads(response.text)
    predictions = np.squeeze(result['predictions'][0])
    class_name = CLASSES[int(predictions > 0.5)]
    print(class_name)
    return class_name
    

get_prediction('dog.jpg')
