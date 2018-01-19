import image

def smooth(image_in):
    image_new = image.EmptyImage(image_in.getWidth(),
                                 image_in.getHeight())
    search = 9
    for w in range(0, image_in.getWidth()):
        w_range = range(w - 1, w + 2) 
        for h in range(0, image_in.getHeight()):
            h_range = range(h - 1, h + 2)
            px_orig = image_in.getPixel(w, h)
            px_new = [0, 0, 0]
            px_indexes = 0
            for px_w in w_range:
                for px_h in w_range:
                    if px_w < 0 or px_w >= image_in.getWidth() or px_h < 0 or px_h >= image_in.getHeight():
                        pass
                    else:
                        px_indexes += 1
                        px_new[0] += px_orig.getRed()
                        px_new[1] += px_orig.getGreen()
                        px_new[2] += px_orig.getBlue()
                        
            
            px_new[:] = [ x/px_indexes for x in px_new ]
#            print(px_orig, px_new)
            new_pixel = image.Pixel(px_new[0],
                                    px_new[1],
                                    px_new[2])
            image_new.setPixel(w,h,new_pixel)
            
    return image_new
            

img = image.Image("luther.jpg")
width = img.getWidth()
height = img.getHeight()
win = image.ImageWin(width, height)
img.draw(win)

img_new = smooth(img)
win2 = image.ImageWin(width, height)

img_new.draw(win2)




