from PIL import Image
try: 
    img  = Image.open('770818.770843.fp.jpg') 
    img.show()
except IOError:
    pass