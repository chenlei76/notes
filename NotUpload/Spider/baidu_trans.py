import urllib.request
import urllib.parse
import json
import random
import time
import random

URL="http://fanyi.baidu.com/v2transapi"
# "Accept-Encoding":"gzip, deflate" 浏览器自带的压缩模式。请注意。
HEADER = {
    "Accept":r"*/*","Accept-Language":"zh-CN,zh;q=0.8","Host":"fanyi.baidu.com","Origin":"http://fanyi.baidu.com","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",\
}

# from原语言
# to目标语言
DataForm = {
    "query":None,\
    "from":"zh",
    "to":"en",\
    "transtype":"translang",\
    "simple_means_flag":"3"
}
def translate(url=None,data=None,header=None):
    if url and data and header:
        data['query'] = input(">>> 请输入您要翻译的内容：")

        data = urllib.parse.urlencode(data).encode("utf-8") # DataForm需要类型转化
        req = urllib.request.Request(url,data,header) # 创建Request对象
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8") # 得到应答，并且解码
        result_list = [res['dst'] for res in json.loads(html)['trans_result']['data']]
        print("<<< 其他的翻译结果是：",r"\n\t".join(result_list))

if __name__=='__main__':
    print("********* 目前支持以下中文转英文的翻译 *********")
    while True:
        translate(URL,DataForm,HEADER)
        time.sleep(random.randint(1,5))

    input(">>> 按任意键退出")

