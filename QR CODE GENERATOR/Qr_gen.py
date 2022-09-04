import qrcode as qr
name=input('Enter a name : ')
img=qr.make(f"Hello {name} , You've scanned the QR successfully ")
img.save("QR_Code.png")
from PIL import Image

qrc=qr.QRCode(version=5,error_correction=qr.ERROR_CORRECT_H,box_size=5,border=4)
qrc.add_data('https://github.com/sarthakk-sharma')
qrc.make(fit=False)
img=qrc.make_image(fill_color='#232e17')
img.save('Sarthak_GitHub.png')
