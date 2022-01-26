from PIL import Image  #read the image
file_name = "media/products/1023871338.jpg"
im = Image.open(file_name) #image size
size=(225,225) #resize image
out = im.resize(size) #save resized image
out.save(file_name)
