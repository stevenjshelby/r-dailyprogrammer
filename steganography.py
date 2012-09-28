#reddit.com/r/dailyprogrammer
#intermediate-101

import sys, Image

#CONSTANTS
TERMINATION = '11111111'

def steg(image_fn,data_fn):
    #read in our image file and declare variables
    img = Image.open(image_fn)
    pixels = img.load()
    im_width = img.size[0]
    im_height = img.size[1]

    #read in our data file and declare variables
    with open(data_fn, 'r') as f:
        data = f.read()
    b_data = ""
    for char in data:
        b_data += '%08d'%int(bin(ord(char))[2:])
        
    b_data += TERMINATION #used to find end when getting data out
    
    #verify image file is large enough
    pix_needed = len(b_data) / 2 
    if im_width * im_height < pix_needed:
        print 'Image file too small for data'
        sys.exit()

    #add data to image file
    for x in range(im_width):
        for y in range(im_height):
            if len(b_data) == 0:
                break
                
            pix = pixels[x,y]
            
            blueBase = bin(pix[2])[2:] #current pixels blue binary value
            newBlue = blueBase[:-2] + b_data[0:2] #create new binary value
            
            b_data = b_data[2:] #remove used bits from b_data
            
            pixels[x,y] = (pix[0],pix[1],int(newBlue,2)) #put new pixel into image file
        else:
            continue
        break

    #save new image as png
    new_file = 'steg_' + image_fn[:image_fn.rfind('.')] + '.png'
    img.save(new_file)
    return 'image saved as ' + new_file
        
def desteg(image_fn):
    #read in our image file and declare variables
    img = Image.open(image_fn)
    pixels = img.load()
    im_width = img.size[0]
    im_height = img.size[1]

    #get bianry data
    b_data = ""
    for x in range(im_width):
        for y in range(im_height):
            pix = pixels[x,y]
            b_data += bin(pix[2])[-2:]
            
    #get actual data
    s_data = ""
    for x in range(0,len(b_data),8):
        chunk = b_data[x:x+8]
        if chunk == '11111111':
            break #end of steganography data
        
        char = chr(int(chunk,2))
        s_data += char

    return s_data
    

#Process args
if len(sys.argv) == 1:
    print 'Usage: steganography.py {steg|desteg} {image file} {data file(steg only)}'
    sys.exit()
    
if sys.argv[1] == 'steg' and len(sys.argv) == 4:
    i_file = sys.argv[2]
    d_file = sys.argv[3]
    print steg(i_file,d_file)
elif sys.argv[1] == 'desteg' and len(sys.argv) == 3:
    i_file = sys.argv[2]
    print desteg(i_file)
else:
    print 'Usage: steganography.py {steg|desteg} {image file} {data file(steg only)}'
    sys.exit()
    
