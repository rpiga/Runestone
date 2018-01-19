import image

def make_it_red(pixel_in):
    new_pixel = [0, 0, 0]
    #new_pixel = image.Pixel(0, 0, 0)
    
    new_pixel[0] = (1.1 * pixel_in.getRed())
    new_pixel[1] = (0.5 * pixel_in.getGreen())
    new_pixel[2] = (0.5 * pixel_in.getBlue())
    
    return new_pixel

def mapper(img_in, mapping_f):
    new_image = image.EmptyImage(img_in.getWidth(),
                                 img_in.getHeight())
    
    for w in range(0,400):
        for h in range(0, 100):
            px_orig = img_in.getPixel(w, h)
            px_new = mapping_f(px_orig)
            new_pixel = image.Pixel(px_new[0],
                                    px_new[1],
                                    px_new[2])
            new_image.setPixel(w,h,new_pixel)
            
    return new_image

    
img = image.Image("luther.jpg")
width = img.getWidth()
height = img.getHeight()

win = image.ImageWin(width, height)

#img.draw(win)

img_new = mapper(img, make_it_red)
img_new.draw(win)
