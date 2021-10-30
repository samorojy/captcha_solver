import os


def clean_dataset(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and os.path.getsize(os.path.join(directory, filename)) > 4:
            os.remove(os.path.join(directory, filename))
            image_filename = filename.replace("_request", "")[:-3] + "png"
            try:
                os.remove(os.path.join(directory, image_filename))
            except:
                print(image_filename)


if __name__ == '__main__':
    clean_dataset("captcha_dataset\evergreen")
