import base64
from PIL import Image
import io
import numpy as np
# 

def decodeImage(imgstring, fileName):
    # Remove data:image/... prefix if exists
    if ',' in imgstring:
        imgstring = imgstring.split(',')[1]

    # Add padding if missing
    imgstring += "=" * ((4 - len(imgstring) % 4) % 4)

    # Decode base64 to bytes
    imgdata = base64.b64decode(imgstring)

    # Save to file (optional)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

    # Convert to RGB image and resize
    img = Image.open(io.BytesIO(imgdata)).convert('RGB')
    img = img.resize((64, 64))

    # Convert to numpy array
    img_array = np.array(img) / 255.0  # normalize
    return np.expand_dims(img_array, axis=0)  # shape (1, 64, 64, 3)


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
