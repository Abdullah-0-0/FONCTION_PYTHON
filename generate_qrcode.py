import qrcode as qr
data = input("Enter the data to generate QR code: ")

img = qr.make(data)

img.save("qrcode.png")
img.show()