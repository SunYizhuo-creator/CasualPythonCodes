import requests

def get_hitokoto():
    # 请求一言API，指定返回纯文本
    url = "https://v1.hitokoto.cn/?c=a&encode=text"
    # c=a 表示动漫类，可选：c=b（名言）、c=c（古诗词）、c=d（网络）
    try:
        return requests.get(url, timeout=5).text
    except:
        return "愿你遍历山河，觉得人间值得。"  # 兜底句子

print("今日一言：", get_hitokoto())

def get_daily_sentence():
    # 可选接口1：每日诗词（推荐）
    url = "https://v1.jinrishici.com/rensheng.txt"
    # 可选接口2：每日一句名言
    # url = "https://api.ooopn.com/mingyan/api.php?type=shuowen"
    
    try:
        response = requests.get(url, timeout=5)
        response.encoding = "utf-8"  # 确保中文不乱码
        return response.text.strip()  # 返回纯文本句子
    except Exception as e:
        return f"获取失败：{e}"

# 调用并打印
if __name__ == "__main__":
    print("今日一句：", get_daily_sentence())


def get_zen_quote():
    url = "https://zenquotes.io/api/random"
    try:
        data = requests.get(url, timeout=5).json()[0]
        return f"{data['q']}\n— {data['a']}"
    except:
        return "Dream big and dare to fail.\n— Norman Vaughan"

print(get_zen_quote())
