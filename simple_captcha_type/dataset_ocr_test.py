import os
import time

import captcha_ocr_decoder


def test(dataset_directory):
    number_of_correct_solved = 0
    count_of_captcha = 0
    for filename in os.listdir(dataset_directory):
        if filename.endswith(".txt"):
            file_with_captcha_solve = open(os.path.join(dataset_directory, filename),
                                           encoding="UTF-8")
            captcha_solve = file_with_captcha_solve.read().upper()
            file_with_captcha_solve.close()
            image_filename = filename.replace("_request", "")[:-3] + "png"
            decode_result = captcha_ocr_decoder.ocr_method_decoder(
                os.path.join(dataset_directory, image_filename))
            count_of_captcha += 1
            print(f"{decode_result}:{captcha_solve}")
            if decode_result == captcha_solve:
                number_of_correct_solved += 1
    print(number_of_correct_solved)
    print(count_of_captcha)


if __name__ == '__main__':
    start_time = time.time()
    test("captcha_dataset\\evergreen")
    print(time.time() - start_time)
