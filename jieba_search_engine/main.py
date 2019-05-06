import requests
from bs4 import BeautifulSoup
import json
import re
import jieba

USER_AGENT = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) '
                            'Chrome/20.0.1092.0 Safari/536.6'}
URL_TIMEOUT = 10

# 格式：{"id": xxx, "url": "xxxxx", "word": {"word1": x, "word2": x, "word3": x}}
dict_result = {}

def crawler(list_URL):
    for i, url in enumerate(list_URL):
        print("网页爬取:", url, "...")
        page = requests.get(url, headers=USER_AGENT, timeout=URL_TIMEOUT)
        page.encoding = page.apparent_encoding  # 防止编码解析错误
        result_chinese = bs4_page_clean(page)
        print("网页中文内容：", result_chinese)
        if result_chinese:
            dict_result["id"] = 


def bs4_page_clean(page):
    print("正则表达式：清除网页标签等无关信息...")
    soup = BeautifulSoup(page.text, "html.parser")
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    soup.prettify()
    reg1 = re.compile("<[^>]*>")
    content = reg1.sub('', soup.prettify())
    return re_chinese(str(soup))


def re_chinese(content):
    print("正则表达式：提取中文...")
    pattern = re.compile(u'[\u1100-\uFFFD]+?')
    result = pattern.findall(content)
    return ''.join(result)

def jieba_search(string):
    list_word = jieba.lcut_for_search(string)


if __name__ == "__main__":

    # list_URL_sport = input()
    # list_URL_sport = ["http://fiba.qq.com/a/20190420/001968.htm",
    #                   "http://sports.qq.com/a/20190424/000181.htm",
    #                   "http://sports.qq.com/a/20190423/007933.htm",
    #                   "http://new.qq.com/omn/SPO2019042400075107"]
    list_URL_sport = ["http://fiba.qq.com/a/20190420/001968.htm"]
    crawler(list_URL_sport)