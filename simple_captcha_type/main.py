import captcha_decoder

if __name__ == '__main__':
    for number in range(1, 9):
        print(captcha_decoder.decoder(f'captches/captcha ({number}).png'))
