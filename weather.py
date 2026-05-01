import pyautogui
import time
import pyperclip
import requests
import json

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
        return f"Hello！现在{city}的天气是{weather}，最高温度{tempH}，最低气温{tempL}，空气指数AQI {aqi}，{wind}，{notice}，好好照顾自己～"

    except requests.exceptions.RequestException as e:
        return f"天气查询失败：网络错误 - {str(e)}"
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        return f"天气查询失败：数据解析错误 - {str(e)}"
    except Exception as e:
        return f"天气查询失败：未知错误 - {str(e)}"
print(getWeather())