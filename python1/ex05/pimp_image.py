from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def invert(array):
    result = array.copy()
    result = 255 - result
    return result


def red(array):
    result = array.copy()

    result[:, :, 0] = result[:, :, 0] * 1
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0

    return result


def green(array):
    result = array.copy()

    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]

    return result


def blue(array):
    result = array.copy()

    result[:, :, 0] = 0
    result[:, :, 1] = 0

    return result


def grey(array):	
    result = array.copy()

    result[:, :, 0] = result[:, :, 0] / 5
    result[:, :, 1] = result[:, :, 1] / 5
    result[:, :, 2] = result[:, :, 2] / 5

    return result


def show_filter(array, title):
    plt.imshow(array.astype(np.uint8))
    plt.title(title)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    try:
        img = ft_load("animal.jpeg")

        print("Original shape:", img.shape)

        red_img = red(img)
        green_img = green(img)
        blue_img = blue(img)
        grey_img = grey(img)
        inverted_img = invert(img)

        print("Red shape:", red_img.shape)
        print("Green shape:", green_img.shape)
        print("Blue shape:", blue_img.shape)
        print("Grey shape:", grey_img.shape)
        print("Invert shape:", inverted_img.shape)

        show_filter(red_img, "Red filter")
        show_filter(green_img, "Green filter")
        show_filter(blue_img, "Blue filter")
        show_filter(grey_img, "Grey filter")
        show_filter(inverted_img, "Invert filter")

    except FileNotFoundError:
        print("Error: file 'animal.jpeg' not found")
    except Exception as e:
        print(f"Error: unexpected error - {e}")