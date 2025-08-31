import cv2
import os

# 设置图像文件夹路径
image_folder = "./output"
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()
print(images)
# 读取第一张图片，获取图片的尺寸
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
print(first_image_path)
height, width, layers = frame.shape

# 定义视频编码器，这里使用mp4v编码
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# 创建视频写入对象，帧率设置为30
video = cv2.VideoWriter("./video", fourcc, 20, (width, height))

# 循环读取每一张图片，并写入视频
for image in images:
    image_path = os.path.join(image_folder, image)
    img = cv2.imread(image_path)
    video.write(img)

# 释放视频写入对象
video.release()
print("视频生成完毕")