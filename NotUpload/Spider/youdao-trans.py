import urllib.request
import urllib.parse
import json
import random
import hashlib
import time
import random

languages = {
    "中文":"zh-CHS",\
    "英文":"en",\
    "日文":"ja",\
    "韩语":"ko",\
    "法语":"fr",\
    "俄语":"ru",\
    "西班牙语":"es",\
    "葡萄牙语":"pt"
}
URL="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom="
# "Accept-Encoding":"gzip, deflate" 浏览器自带的压缩模式。请注意。
HEADER = {
    "Accept":"application/json, text/javascript, */*; q=0.01",\
    "Accept-Language":"zh-CN,zh;q=0.8",\
    "Host":"fanyi.youdao.com",\
    "Origin":"http://fanyi.youdao.com",\
    "Referer":"http://fanyi.youdao.com/",\
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",\
    "Proxy-Connection":"keep-alive"
}
# i是翻译内容
# from原语言
# to目标语言
DataForm = {
    "i":None,\
    "from":"AUTO",
    "to":"AUTO",\
    "smartresult":"dict",\
    "client":"fanyideskweb",\
    "doctype":"json",\
    "version":"2.1",\
    "keyfrom":"fanyi.web",\
    "action":"FY_BY_CLICKBUTTION",\
    "typoResult":"true",\
    "salt":None,\
    "sign":None
}
def translate(url=None,data=None,header=None,From=None,To=None):
    if url and data and header:
        data['i'] = input(">>> 请输入您要翻译的内容：")

        # 下面开始确定随机数
        # 请自行阅读fanyi.js
        f = str(int(time.time()*1000) + random.randint(1,10))
        data['salt'] = f
        c = 'rY0D^0\'nM0}g5Mm1z%1G4' # fanyi.js中的常量
        data['sign'] = hashlib.md5((data['client']+data['i']+f+c).encode('utf-8')).hexdigest()
        # 请自行阅读fanyi.js

        if From and To:
            data['from'] = str(From)
            data['to'] = str(To)

        data = urllib.parse.urlencode(data).encode("utf-8") # DataForm需要类型转化
        req = urllib.request.Request(url,data,header) # 创建Request对象
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8") # 得到应答，并且解码
        # print(html) #先看一下格式，再决定用什么方法
        result = json.loads(html)['translateResult'][0][0]['tgt']
        try:
            smartResult = json.loads(html)["smartResult"]["entries"]
            otherResult = [res.strip("\n").strip("\r") for res in smartResult if len(res) and res.strip("\n").strip("\r")!=result]
        except Exception as error:
            print("<<< 翻译后的内容是：",result)
        else:
            print("<<< 翻译后的内容是：", result)
            if len(otherResult):
                print("<<< 其他的翻译结果是："," ".join(otherResult))

if __name__=='__main__':
    print("<<< 目前支持以下几种语言的翻译：")
    for lan in languages:
        print("        ",lan)

    From = input('>>> 请输入您要翻译语言：').strip()
    To = input('>>> 请输入翻译后的目标语言：').strip()
    From  = languages.get(From)
    To = languages.get(To)

    while True:
        translate(URL,DataForm,HEADER,From,To)
        time.sleep(random.randint(1,5))

    input(">>> 按任意键退出")

