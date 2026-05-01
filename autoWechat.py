import pyautogui
import time
import pyperclip
import requests
import json
# 全局设置：放慢操作速度，避免失控
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# ========== 替换为你的实际参数 ==========
CONTACT_NAME = "一鸣惊人"  # 联系人名称
INPUT_BOX_X = 499  # 步骤1获取的输入框x坐标
INPUT_BOX_Y = 946  # 步骤1获取的输入框y坐标

SEND_MSG = "这是一条自动发送的测试消息"

def open_and_activate_wechat():
    """打开并激活微信窗口（确保获得焦点）"""
    # 1. 回到桌面，避免窗口遮挡
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    # 2. 唤起微信
    pyautogui.hotkey("alt", "ctrl", "w")
    time.sleep(1)  # 给足加载时间（新版微信启动慢）
    # 3. 强制激活微信窗口（点击窗口空白处）
    # 微信主窗口坐标（可根据实际调整，比如输入框左边100px）
    pyautogui.click(INPUT_BOX_X - 100, INPUT_BOX_Y - 200)
    time.sleep(1)

import pyperclip
# 定义一个查询联系人的函数，参数为name
def chatWho(name):
    # 使用hotkey函数，操作按键"command","f"，打开搜索
    pyautogui.hotkey("ctrl","f")
    # 使用pyperclip模块中的copy函数，复制微信号name到剪贴板
    pyperclip.copy(name)
    # 使用hotkey函数，操作按键"command", "v"，粘贴微信号
    pyautogui.hotkey("ctrl", "v")
    # 使用hotkey函数，操作按键"return"，确认搜索
    pyautogui.hotkey("enter")
def send_message(msg):
    """精准粘贴并发送消息"""
    # 1. 点击输入框，强制激活（核心！）
    pyautogui.click(INPUT_BOX_X, INPUT_BOX_Y)
    time.sleep(1)
    # 2. 清空输入框（可选）
    pyautogui.hotkey("ctrl", "a", "backspace")
    time.sleep(0.5)
    # 3. 复制消息到剪贴板（双重确认）
    pyperclip.copy(msg)
    time.sleep(1)  # 等待剪贴板同步
    # 4. 粘贴（如果Ctrl+V无效，改用模拟输入）
    try:
        pyautogui.hotkey("ctrl", "v")
    except:
        # 备用方案：直接输入（绕过剪贴板风控）
        pyautogui.typewrite(msg)
    time.sleep(1)
    # 5. 发送消息（双保险：先试Ctrl+Enter，再试Enter）
    
    pyautogui.hotkey("enter")

def getWeather():
    """
    使用HTTP协议的天气API（彻底避开SSL错误）
    """
    try:
        city = "北京"
        # 纯HTTP API（无SSL限制）
        url = f"http://t.weather.sojson.com/api/weather/city/101010100"  # 101010100是北京的城市代码
        
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=header, timeout=10)
        response.raise_for_status()
        
        # 解析JSON数据
        data_json = response.json()
        if data_json.get("status") != 200:
            return f"天气查询失败：API返回异常 - {data_json.get('message', '未知错误')}"
        
        # 提取数据
        today = data_json.get("data", {}).get("forecast", [{}])[0]
        print(today)
        tempH = today.get("high", "未知").replace("高温", "")  # 提取最高温
        tempL = today.get("low", "未知").replace("低温", "")  
        weather = today.get("type", "未知")
        wind = today.get("fx","")+today.get("fl", "")
        notice = today.get("notice","")
        aqi = today.get("aqi","未知")
        return f"早上好！现在{city}的天气是{weather}，最高温度{tempH}，最低气温{tempL}，空气指数AQI {aqi}，{wind}，{notice}，好好照顾自己～"

    except requests.exceptions.RequestException as e:
        return f"天气查询失败：网络错误 - {str(e)}"
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        return f"天气查询失败：数据解析错误 - {str(e)}"
    except Exception as e:
        return f"天气查询失败：未知错误 - {str(e)}"

# 主流程
if __name__ == "__main__":
    open_and_activate_wechat()
    chatWho(CONTACT_NAME)
    send_message(getWeather())
    print("消息发送完成！")