from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280, height= 90)

captcha_text = 'Paulo'

data = image.generate(captcha_text)

image.write(captcha_text, 'captcha.png')

# o captcha é salvo na pasta do projeto.
