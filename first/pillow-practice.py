from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
img = Image.open('/Users/doc88/Desktop/banner.png')
# 获得图像尺寸:
w, h = img.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
img.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
img.save('/Users/doc88/Desktop/thumbnail.png', 'png')

# 应用模糊滤镜:
img2 = img.filter(ImageFilter.BLUR)
img2.save('/Users/doc88/Desktop/blur.png', 'png')