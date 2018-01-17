import image
FACTOR = 2

def enlargeImage(origImage, factor = FACTOR):
    
    origW = origImage.getWidth()
    origH = origImage.getHeight()
    #print(">", origW, origH)
    enlargedImage = image.EmptyImage(factor * origW,
                               factor * origH)
    
    new_index = 0
    
    for w in range(0, origW):
        for h in range(0, origH):
            origPixel = origImage.getPixel(w, h)
            for new_w in range(w * FACTOR, 
                               (w * FACTOR) + FACTOR):
                for new_h in range(h * FACTOR, 
                                   (h * FACTOR) + FACTOR):
                    enlargedImage.setPixel(new_w, new_h, origPixel)
            
            new_index = new_index + FACTOR
            
    return enlargedImage


img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth() * FACTOR,
                     img.getHeight() * FACTOR)

new_img = enlargeImage(img)
new_img.draw(win)

win.exitonclick()
