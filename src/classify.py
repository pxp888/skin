import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing import image as image_utils

from skimage.transform import resize


def classifyImage(im):
    try:
        image = image_utils.load_img(im, target_size=(224, 224))
        image = image_utils.img_to_array(image)
    except:
        image = resize(im, (224, 224))
    

    image = np.expand_dims(image, axis=0)

    model = load_model('assets/model.keras')
    out = model.predict(image)
    return out



