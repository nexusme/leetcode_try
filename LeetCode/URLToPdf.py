import pdfkit
import time

test_url = 'http://10.0.0.93:7001/memberAnalysis/groups'


def get(get_name):
    # url = get_name
    # 文件路径
    # to_file = 'out.pdf'

    options = {
        'encoding': "utf-8"
    }

    pdfkit.from_url(get_name, 'out.pdf', options=options)
    print('已生成pdf文件')


get(test_url)
