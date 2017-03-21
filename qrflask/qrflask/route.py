from flask import Flask, render_template, url_for
from app import *
import qrcode
import qrtools

img1 = qrcode.make('THE QR test')
img = img1.save("C:/Users/madhu/Documents/GitHub/QRCode/qrflask/qrflask/static/images/myQR.png")

@app.route('/')
def hello():
    """Renders a sample page."""
    #return "Hello World!"
    return render_template('index.html')