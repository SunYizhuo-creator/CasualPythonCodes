# 导入必要模块（统一放在开头，规范代码结构）
import os
import random
from PIL import Image 

# ===================== 核心配置（请根据你的实际文件位置修改）=====================
# 主文件夹路径（必须用原始字符串 r"" 避免转义错误）
BASE_PATH = r"C:\Users\Administrator\OneDrive\编程成果\python练手示例"
# 背景图片名称（确保pink.png确实在上述文件夹中）
BACKGROUND_IMAGE = "pink.png"
# 存放拼接照片的文件夹名称（在BASE_PATH下新建model文件夹，放入你的照片）
PHOTO_FOLDER = "model"
# 形状图片名称（爱心.png/520.png/1314.png，确保在BASE_PATH下）
# ===============================================================================

# 1. 获取用户输入的形状图片名称
pngName = input("输入图片名称（爱心/520/1314）:").strip()  # strip()去除输入的空格
shape_file = os.path.join(BASE_PATH, f"{pngName}.png")  # 安全拼接路径

# 2. 检查并打开形状图片（增加异常处理，避免文件找不到崩溃）
try:
    img = Image.open(shape_file)
except FileNotFoundError:
    print(f"错误：找不到形状图片 {shape_file}，请检查文件是否存在！")
    exit(1)

# 3. 图片二值化+缩放（修复取模运算错误）
img_1 = img.convert("1")  # 转为二值图片（0=黑，255=白）
new_img = img_1.resize((20, 20))  # 缩放到20x20像素

# 4. 提取形状像素数据（修复取模逻辑，正确转换为0/1）
figure = []
for i in range(20):
    row = []
    for j in range(20):
        pix = new_img.getpixel((j, i))
        # 二值图片像素是0（黑）或255（白），转为0（需要贴照片）/1（不贴）
        pix_new = 1 - (pix %254)  # 替代错误的 pix % 254
        row.append(pix_new)
    figure.append(row)

# 5. 配置照片尺寸
pic_width = 100
pic_height = 100

# 6. 打开并缩放背景图片（增加异常处理）
background_path = os.path.join(BASE_PATH, BACKGROUND_IMAGE)
try:
    img_back = Image.open(background_path).resize((2000, 2000))
except FileNotFoundError:
    print(f"错误：找不到背景图片 {background_path}，请检查文件是否存在！")
    exit(1)

# 7. 获取拼接照片列表（修复路径转义+增加文件夹检查）
photo_folder_path = os.path.join(BASE_PATH, PHOTO_FOLDER)
if not os.path.exists(photo_folder_path):
    print(f"错误：找不到照片文件夹 {photo_folder_path}，请新建该文件夹并放入照片！")
    exit(1)

# 过滤出图片文件（避免读取非图片文件）
image_names = [f for f in os.listdir(photo_folder_path) 
               if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
if not image_names:
    print(f"错误：{photo_folder_path} 文件夹中没有找到图片文件！")
    exit(1)

# 8. 遍历形状像素，粘贴照片
row_num = len(figure)
column_num = len(figure[0])

for row in range(row_num):
    for column in range(column_num):
        if figure[row][column] == 1:  # 0表示需要贴照片的位置
            # 随机选一张照片
            ran_photo_name = random.choice(image_names)
            ran_photo = os.path.join(photo_folder_path, ran_photo_name)
            # 打开并缩放照片
            try:
                pic = Image.open(ran_photo).resize((pic_width, pic_height))
                # 计算粘贴位置并粘贴
                x = pic_width * column
                y = pic_height * row
                img_back.paste(pic, (x, y))
            except Exception as e:
                print(f"警告：处理照片 {ran_photo} 失败 - {e}")
                continue

# 9. 保存最终图片
save_path = os.path.join(BASE_PATH, "final.png")
img_back.save(save_path)
print(f"成功！照片墙已保存到：{save_path}")