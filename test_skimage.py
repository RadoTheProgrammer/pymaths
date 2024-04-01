from skimage import data,io
import numpy as np

image=data.brick()
print(type(image))
io.imsave("test.png",image)

