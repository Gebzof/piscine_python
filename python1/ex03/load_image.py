from PIL import Image
import numpy as np

def ft_load(path: str) -> array:
    try:
        img = Image.open(path, 'r')
        arr = np.array(img)
        assert img.format == "JPEG" or img.format == "JPG", "Handles JPG/JPEG format only"
        pix_val = list(img.getdata())
        pix_val_arr = np.array(pix_val)
        print(f"the shape of the image is: {arr.shape} ")
        print(f"The format is {img.format}")
        return arr
    except OSError:
        return ["image not here"]
