import czifile
from PIL import Image, ImageEnhance

image = czifile.imread('/home/techgarage/Downloads/A2-2 zstack 20X.2.czi')
print(image.shape)
image = image[0,0,0,0,0].T[0]
im = Image.fromarray(image)
enhancer = ImageEnhance.Contrast(im)
enhanced_im = enhancer.enhance(100.0)
enhanced_im.save("test2.png")