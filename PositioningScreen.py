import pyautogui
import time

# 先打开微信（手动打开，最小化）
input("请手动打开微信并最小化，按回车继续...")
# 唤起微信
pyautogui.hotkey("alt", "ctrl", "w")
time.sleep(2)
# 提示操作
print("请在5秒内将鼠标移到微信聊天输入框上...")
time.sleep(5)
# 打印坐标
x, y = pyautogui.position()
print(f"输入框坐标：x={x}, y={y}")  # 比如输出：x=285, y=726
