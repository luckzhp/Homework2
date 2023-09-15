import tkinter
from tkinter import ttk
import requests
import sv_ttk
import time
import re
import urllib.request,urllib.error
import bs4
import os
import json
import urllib.parse
import io
import sys


start_num = 1051
end_num = 1052

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

#询问网址
def get_Html(url):
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    if str(html).find("Exception") == -1:       
        return html
    else:
        return "error"

#获得问题的markdown
def get_qustion(html):
    bs = bs4.BeautifulSoup(html,"html.parser")
    core = bs.select("article")[0]
    #que存下title和最终title
    que = str(core)

    #找到题目
    title=""
    pattern = re.compile(r'<h1>.*?</h1>')
    matches = pattern.findall(que)
    title=matches[0]
    title = re.sub("<h1>", "",title)
    title = re.sub("</h1>", "", title)
    #删去无关字符并且改markdo格式
    que = re.sub("<h1>","# ",que)
    que = re.sub("<h2>","## ",que)
    que = re.sub("<h3>","#### ",que)
    que = re.sub("</?[a-zA-Z]+[^<>]*>","",que)

    return title, que

def saveData(data,title):
    # 设置基础路径
    base_path = r"D:\Users\pythontest\res"

    # 创建存放 Luogu 数据的文件夹
    luogu_folder = os.path.join(base_path, "Luogu")
    if not os.path.exists(luogu_folder):
        os.makedirs(luogu_folder)

    # 创建题目对应的文件夹
    folder_path = os.path.join(luogu_folder, title)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 创建 Markdown 文件
    output_file = os.path.join(folder_path, title + ".md")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(data)


def main():
    for problem_num in range(start_num, end_num + 1):
        nowurl = f'https://www.luogu.com.cn/problem/P{problem_num}'
 
        html = get_Html(nowurl)
        if html == "error" :
            print("爬取失败，无法打开该网站")
        else:
            title, que = get_qustion(html)
            saveData(que, title)
            print("p",problem_num,title,"爬取成功")

if __name__ == "__main__":
    main()
