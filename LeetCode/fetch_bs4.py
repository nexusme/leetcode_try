from decimal import Decimal
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import urllib.request
import json
import requests
import re
import pandas as pd

link1 = 'https://www.dreamgrow.com/top-15-most-popular-social-networking-sites/'


# link = "https://www.bilibili.com/ranking/bangumi/13/0/7"


def get_HTML(link_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36 Edg/85.0.564.23',
    }
    response = requests.get(link_name, headers=headers)
    print(response.status_code)
    response.encoding = None
    if response.status_code != 200:
        raise ConnectionError
    result = response.text
    soup = BeautifulSoup(result, 'html.parser')
    # print(soup)
    return soup


def str_to_double(df_name):
    for c in range(len(df_name)):
        # print(row)
        if re.search('万', df_name[c]):
            row = df_name[c]
            df_name[c] = Decimal(row[:-1])
        else:
            row = df_name[c]
            row = Decimal(row[:-1])
            df_name[c] = row * 10000


def manage_data():
    soup_doc = get_HTML()
    data = []
    i = 0

    soup_doc_next = soup_doc.find("div", attrs={"class": "rank-list-wrap"})
    soup_doc_next_ul = soup_doc_next.find("ul", attrs={"class": "rank-list pgc-list"})
    soup_find_li = soup_doc_next_ul.find_all('li')
    for s in soup_find_li:
        i += 1
        soup_find_class = s.find("div", attrs={"class": "content"})
        soup_find_name = soup_find_class.find("img")
        soup_find_detail = soup_find_class.find("div", attrs={"class": "detail"})
        data_box = soup_find_detail.find_all("span", attrs={"class": "data-box"})
        play_data = [data.text for data in data_box]
        data.append([i, soup_find_name['alt']] + play_data)

    columns = ["total_rank", "title", "play", "comments", "liked"]
    df = pd.DataFrame(data, columns=columns)
    for name in ["play", "comments", "liked"]:
        str_to_double(df[name])
    print(df)

    df.plot.bar(x=df['title'], y=[df['play']])
    plt.show()


# manage_data()

# get_HTML(link1)

soup = get_HTML(link1)
# print(soup)
# soup_doc_next = soup.body.div.article.div.table.tbody
# soup_doc_td = soup_doc_next.findAll("tr")
# final_value = []
# final_dict = []
# for row in soup_doc_td:
#     for next_level in row.findAll("a"):
#         final_value.append(next_level.string)
# print(final_value)
# for i in range(0, len(final_value) - 1, 2):
#     final_dict.append({'name': final_value[i], 'value': int(final_value[i + 1].replace(',', ''))})
# print(final_dict)
content = [i.string for i in soup.body.div.article.div.table.tbody.findAll('a')]
print(dict(zip(content[::2], content[1::2])))
# print(list_final)
