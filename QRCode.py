import pyqrcode
import qrcode as qrcode

# QR CODE GENERATOR :

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 10, border = 4,)
print("\n  *** Welcome to the QR Code Generator !!! ***")
print("   ======================================")
print("\n   Enter the Link for QR Code : ",end="")
link = str(input())
qr.add_data(link)
qr.make(fit = True)
img = qr.make_image(fill_color = "black", back_color = "white")
print("\n   Enter the Name for QR Code [Format:(.png)]: ",end="")
name = str(input())
img.save(name)
