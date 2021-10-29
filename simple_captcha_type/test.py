import unittest
import captcha_decoder


class TestStringMethods(unittest.TestCase):

    def test_images(self):
        self.assertEqual(captcha_decoder.decoder('captches/captcha (1).png'), 'CGCC')
        self.assertEqual(captcha_decoder.decoder('captches/captcha (2).png'), 'UXCU')
        self.assertEqual(captcha_decoder.decoder('captches/captcha (3).png'), 'GGVK')
        self.assertEqual(captcha_decoder.decoder('captches/captcha (4).png'), 'KDND')
        self.assertEqual(captcha_decoder.decoder('captches/captcha (5).png'), 'EFFE')
        self.assertEqual(captcha_decoder.decoder('captches/captcha (6).png'), 'OIRQ')


if __name__ == '__main__':
    unittest.main()
