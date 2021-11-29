# Automatic *CAPTCHA* recognition

The first type of captcha. This captcha is easy to solve and for its solution there are 2 algorithms. 

![evergreen_00150923062021StRrDfBk3z](https://user-images.githubusercontent.com/71323710/143767495-df0d0c9f-3281-4f07-8200-c6ec042ce28f.png)


### First algorithm: "captcha_algo_decoder" and "captcha_algo_decoder2".

It is based on an analytical solution. An alphabet of letters was created and now the letters from the alphabet are superimposed on the letters of the captcha and the answer is obtained by the number of matches. Since the CAPTCHA of the simple (first) type is generated in two different ways, the division of the CAPTCHA into letters is also done in two different ways. The "captcha_algo_decoder" divides it into 4 equal parts, and the "captcha_algo_decoder2" imposes a letter from the alphabet at the beginning, checks the similarity and then cuts off the first letter of the CAPTCHA, knowing its size. 

#### Metrics: 

Time: 120 seconds to solve 4,232 CAPTCHAs

Accuracy: 99.9%

### The second algorithm: "captcha_ocr_decoder"

It is based on optical recognition. The selected OCR was Tesseract (pyTesseract). After recognition all characters except letters are removed from the text. 

#### Metrics:

Time: 520 seconds to solve 4232 CAPTCHAs

Accuracy: about 10.5%


*A detailed Readme for II type will be written soon*
