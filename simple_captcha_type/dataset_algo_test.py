import os
import time
from shutil import copyfile

import captcha_algo_decoder


def test(dataset_directory):
    for filename in os.listdir(dataset_directory):
        if filename.endswith(".txt"):
            file_with_captcha_solve = open(os.path.join(dataset_directory, filename),
                                           encoding="UTF-8")
            captcha_solve = file_with_captcha_solve.read().upper()
            file_with_captcha_solve.close()
            image_filename = filename.replace("_request", "")[:-3] + "png"
            decode_result = captcha_algo_decoder.decoder(
                os.path.join(dataset_directory, image_filename))
            print(f"{decode_result}:{captcha_solve}")
            if decode_result != captcha_solve:
                copyfile(os.path.join(dataset_directory, image_filename),
                         f"incorrect_captcha/{captcha_solve}.png")
                os.remove(os.path.join(dataset_directory, filename))
                os.remove(os.path.join(dataset_directory, image_filename))


if __name__ == '__main__':
    start_time = time.time()
    test("captcha_dataset\\evergreen")
    print(time.time() - start_time)
