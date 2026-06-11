# app/search_novels.py

import requests
from bs4 import BeautifulSoup
from flask import jsonify


def search_novels(query):
    search_results = []

    # 使用 Bing 搜索小说
    url = f"https://www.bing.com/search?q={query}+novel"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # 确保请求成功
    if response.status_code != 200:
        return jsonify({"error": "无法访问 Bing 搜索结果"}), 500

    # 解析搜索结果
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取搜索结果中的链接和标题
    for item in soup.find_all('li', class_='b_algo'):
        title = item.find('h2').text
        link = item.find('a')['href']
        source = 'Bing'
        search_results.append({'title': title, 'url': link, 'source': source})

    return search_results
