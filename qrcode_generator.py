import qrcode

img = qrcode.make('https://twitter.com/hadleywickham')
img.save("myQr.png")