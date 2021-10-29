from PIL import Image

import captcha_letters_cutter


def decoder(image_file_name):
    captcha_letters_cutter.cut_letters(image_file_name)
    answer = ""
    for x in range(0, 4):
        answer = answer + detekt_letter(f"letters/{x}.png")[0]
    return answer


def detekt_letter(image_file_name):
    alphabet_list_with_weight = [('A', 230), ('B', 270), ('C', 190), ('D', 282), ('E', 208), ('F', 166), ('G', 224),
                                 ('H', 260),
                                 ('I', 112), ('J', 131), ('K', 228), ('L', 148), ('M', 368), ('N', 268), ('O', 265),
                                 ('P', 211),
                                 ('Q', 297), ('R', 263), ('S', 185), ('T', 172), ('U', 217), ('V', 197), ('W', 354),
                                 ('X', 216),
                                 ('Y', 165), ('Z', 211)]
    image = Image.open(image_file_name)
    image = image.convert("RGB")
    pixel_data = image.load()
    letter_similarity_list = []
    for letter in alphabet_list_with_weight:
        letter_image_pixel_data = Image.open(f"alphabet/{letter[0]}.png").load()
        letter_similarity_counter = 0
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                if letter_image_pixel_data[x, y] == (0, 0, 0) and pixel_data[x, y] == (0, 0, 0):
                    letter_similarity_counter += 1
        if letter_similarity_counter >= letter[1]:
            letter_similarity_list.append((letter, letter_similarity_counter))
    letter_similarity_list.sort(key=lambda k: k[1], reverse=True)
    return letter_similarity_list[0][0]
