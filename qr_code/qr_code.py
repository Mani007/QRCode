import qrcode
import qrtools

img = qrcode.make('name: Niladri\n ID : 12345')

img.save("filename.png")
# we can also save file to a particular location 
# img.save("C:/Users/all/Documents/GitHub/QRCode/qrflask/qrflask/tempimg/myQR.png")

qr = qrtools.QR()

qr.decode("filename.png")
#from qrtools import QR
#myCode = QR()
#print myCode.decode_webcam()
# The decode_webcam() method will open a zbar(driver written in C)  window that will let you scan for a code using your webcam

print qr.data

