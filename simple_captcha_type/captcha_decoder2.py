import os

from PIL import Image

import captcha_letters_cutter


def decoder(image_file_name):
    image = Image.open(image_file_name)
    image = image.convert("RGB")
    captcha_letters_cutter.clear_noise(image)
    answer = ""
    letter_width = 0
    for x in range(0, 4):
        box = (letter_width, 0, 150, 40)
        detekt_result = detekt_letter(image.crop(box))
        letter_width = letter_width + detekt_result[2]
        answer = answer + detekt_result[0]
    return answer


def detekt_letter(image):
    alphabet_list_with_weight = [('A', 230, 26), ('B', 270, 22), ('C', 190, 26), ('D', 282, 28), ('E', 208, 21),
                                 ('F', 166, 20), ('G', 224, 27), ('H', 260, 28),
                                 ('I', 112, 11), ('J', 131, 12), ('K', 228, 25), ('L', 148, 20), ('M', 368, 33),
                                 ('N', 268, 28), ('O', 265, 30), ('P', 211, 21),
                                 ('Q', 297, 30), ('R', 263, 24), ('S', 185, 20), ('T', 172, 24), ('U', 217, 26),
                                 ('V', 197, 25), ('W', 354, 33), ('X', 216, 24),
                                 ('Y', 165, 24), ('Z', 211, 23)]
    pixel_data = image.load()
    letter_similarity_list = []
    for letter in alphabet_list_with_weight:
        letter_image = Image.open(f"alphabet/{letter[0]}.png")
        letter_image_pixel_data = letter_image.load()
        letter_similarity_counter = 0
        for y_coordinate in range(letter_image.size[1]):
            for x_coordinate in range(letter_image.size[0]):
                if letter_image_pixel_data[x_coordinate, y_coordinate] == (0, 0, 0) \
                        and pixel_data[x_coordinate, y_coordinate] != (0, 0, 0):
                    letter_similarity_counter = -1
                    break
                if letter_image_pixel_data[x_coordinate, y_coordinate] == (0, 0, 0) \
                        and pixel_data[x_coordinate, y_coordinate] == (0, 0, 0):
                    letter_similarity_counter += 1
            if letter_similarity_counter == -1:
                break
        if letter_similarity_counter >= letter[1]:
            letter_similarity_list.append((letter, letter_similarity_counter))
    letter_similarity_list.sort(key=lambda k: k[1], reverse=True)
    if not letter_similarity_list:
        return '_', 0, 0
    return letter_similarity_list[0][0]


if __name__ == '__main__':
    dataset_directory = "incorrect_captcha"
    for filename in os.listdir(dataset_directory):
        captcha_solve = filename[:-3]
        image_filename = captcha_solve + "png"
        decode_result = decoder(os.path.join(dataset_directory, image_filename))
        print(f"{decode_result}:{captcha_solve[:-1]} {decode_result == captcha_solve[:-1]}")
