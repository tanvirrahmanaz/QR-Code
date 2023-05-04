import qrcode 
from PIL import Image

qr= qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
details = input("Enter your details: ")
qr.add_data("details")
qr.make(fit=True)
img = qr.make_image(fill_color = 'Black',back_color = 'White')
image_name = input("Enter your QR name: ")
img.save("image_name.png")