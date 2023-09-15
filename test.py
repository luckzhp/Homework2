import requests
from urllib.parse import unquote
from selenium import webdriver


# 设置浏览器驱动程序路径，需要下载对应浏览器的驱动程序
driver_path = 'D:/Download/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # 需要下载 Chrome 驱动程序
url = "https://www.luogu.com.cn/problem/solution/P1012"

cookies = "__client_id=32cbd0dc13541229ed22ae35b88338689027cae6; _uid=1093788"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    cookies_jar.set(key, value)

# 创建一个 Chrome 浏览器实例
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)

# 使用浏览器加载页面
browser.get(url)

# 获取页面的JavaScript渲染后内容
rendered_content = browser.page_source

# 关闭浏览器
browser.quit()

# 解码响应内容
print(rendered_content)
