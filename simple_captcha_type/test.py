import os
import unittest

import captcha_algo_decoder


class TestDecoderOnDataset(unittest.TestCase):

    def test_works_as_expected(self):
        for filename in os.listdir("captcha_dataset\\evergreen"):
            if filename.endswith(".txt"):
                file_with_captcha_solve = open(os.path.join("captcha_dataset\\evergreen", filename),
                                               encoding="UTF-8")
                expected = file_with_captcha_solve.read().upper()
                image_filename = filename.replace("_request", "")[:-3] + "png"
                decode_result = captcha_algo_decoder.decoder(
                    os.path.join("captcha_dataset\\evergreen", image_filename))
                file_with_captcha_solve.close()
                with self.subTest():
                    self.assertEqual(expected, decode_result)


if __name__ == '__main__':
    unittest.main()
