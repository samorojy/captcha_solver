from PIL import Image


def cut_letters(image_file_name):
    image = Image.open(image_file_name)
    image = image.convert("RGB")

    clear_noise(image)
    letters_list = []
    for i in range(0, 4):
        box = (i * 30, 0, (i * 30 + 30), 40)
        letters_list.append(image.crop(box))
        #image.crop(box).save(f"letters/{i}.png")
    return letters_list

# Clean the background noise, if color != white, then set to black.
def clear_noise(image, threshold=200):
    pixdata = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if (pixdata[x, y][0] > threshold) \
                    and (pixdata[x, y][1] > threshold) \
                    and (pixdata[x, y][2] > threshold):

                pixdata[x, y] = (255, 255, 255)
            else:
                pixdata[x, y] = (0, 0, 0, 255)
