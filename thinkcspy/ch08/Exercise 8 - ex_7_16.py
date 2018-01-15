import image
img = image.Image("luther.jpg")

imgW = img.getWidth()
imgH = img.getHeight()

newImg = image.EmptyImage(imgW,imgH)



imgWin = image.ImageWin(imgW, imgH)
#newImgWin = newImg.ImageWin(imgW, imgH)
#img.draw(imgWin)
newImg.setDelay(0)   # setDelay(0) turns off animation

for w in range( 0, imgW ):
   for h in range( 0, imgH ):
    p = img.getPixel(w, h)
    newGray = (p.getRed() + p.getGreen() + p.getBlue() )/3
    newpixel = image.Pixel(newGray, newGray, newGray)
    newImg.setPixel(w, h, newpixel)

newImg.draw(imgWin)
#imgWin.exitonclick()
