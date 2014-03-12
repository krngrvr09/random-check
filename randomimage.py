import Image
import random
 
img = Image.new( 'RGB', (255,255), "black")
pixels = img.load()
 
for i in range(img.size[0]):
    for j in range(img.size[1]):
	if random.randint(0,1):
        	pixels[i,j] = (0,0,0)
	else:
        	pixels[i,j] = (255,255,255)
img.show()

