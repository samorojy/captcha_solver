from PIL import Image


def cut_letters(image_file_name):
    image = Image.open(image_file_name)
    image = image.convert("RGB")

    clear_noise(image)
    letters_list = []
    for i in range(0, 4):
        box = (i * 30, 0, (i * 30 + 30), 40)
        letters_list.append(image.crop(box))
    return letters_list


# Clean the background noise, if color != white, then set to black.
def clear_noise(image, threshold=200):
    pixdata = image.load()
    for y_coordinate in range(image.size[1]):
        for x_coordinate in range(image.size[0]):
            if (pixdata[x_coordinate, y_coordinate][0] > threshold) \
                    and (pixdata[x_coordinate, y_coordinate][1] > threshold) \
                    and (pixdata[x_coordinate, y_coordinate][2] > threshold):

                pixdata[x_coordinate, y_coordinate] = (255, 255, 255)
            else:
                pixdata[x_coordinate, y_coordinate] = (0, 0, 0, 255)
