import qrcode as qr
from PIL import Image


img = qr.QRCode(version=1,
                box_size=15,
                border=5
                )

data = 'Hi I am learning Pyton from Skillup Academy'

img.add_data(data=data)

img = img.make_image(fill_color='red',
                     back_color='pink')

img.save('C:/Users/Hasnain/Desktop/images/image.png')

