[TOC]

> 众所周知，爬虫、日志文件和数据库是大数据的**三大来源**。很久没做爬虫的我，那天突然发现拿手技能有些遗忘，想查一下原来的代码，然而当时才疏学浅，代码样式及其混乱、难看。所以，现在想重新整理一下，并且做一些有用的东西。希望可以坚持下去，Share、Project、Image。

## 1. 工作环境
- python3.x
- pycharm（或者一款不错专业编辑器）
- Chrome浏览器（这次的例子很简单，之后会用到专业的抓包工具Fiddler）

## 2. 学习urllib
> 更详细的自动转到文档，这里只做常用的API和类的介绍。

### 2.1 `urllib.error`
- `urllib.request.URLError`:有reason属性
    ```python
    try:
        ...
    except urllib.request.URLError as e:
        print(e.reason)
    ```

- `urllib.request.HTTPError`:这是URLError的子类，有code和reason属性
    ```python
    try:
        ...
    except urllib.request.HTTPError as e:
        print(e.code)
    except urllib.request.URLError as e:
        print(e.reason)
    #更好的选择
    try:
        ...
    except urllib.request.URLError as e:
        if hasattr(e,'reason'):
            ...
        elif hasattr(e,'code'):
            ...
    ```
### 2.2 `urllib.parse`
- `urllib.parse.urlencode(data)`:将DataForm编码后，才可以传递给服务器。当然，之后会有`requests`这款神奇的库。

### 2.3 `urllib.request`

- `urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)`:下载url，并且命名为filename。经常用于爬取图片，文件，exe等。

- `urllib.request.Request(url,data=None,headers={})`:最重要的Request对象。
1. 关于data:<br>
    > 官方文档：**data must be a bytes object specifying additional data to send to the server, or None if no such data is needed.** Currently HTTP requests are the only ones that use data; the HTTP request will be a POST instead of a GET when the data parameter is provided. data should be a buffer in the standard application/x-www-form-urlencoded format. The **urllib.parse.urlencode()** function takes a mapping or sequence of 2-tuples and returns an ASCII string in this format. **It should be encoded to bytes before being used as the data parameter.**
    <br>代码示例如下所示<br>
    ```python
        data={}
        data['type']='AUTO'
        data['i']=words
        data['doctype']='json'
        data['xmlVersion']='1.8'
        data['keyfrom']='fanyi.web'
        data['ue']='UTF-8'
        data['action']='FY_BY_CLICKBUTTON'
        data['typoResult']='true'
        data=urllib.parse.urlencode(data).encode('utf-8')
    ```

2. 关于header：<br>
    > **headers should be a dictionary, and will be treated as if add_header(key,value)** was called with each key and value as arguments. **This is often used to “spoof” the User-Agent header value, which is used by a browser to identify itself – some HTTP servers only allow requests coming from common browsers as opposed to scripts. For example, Mozilla Firefox may identify itself as "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11", while urllib‘s default user agent string is "Python-urllib/2.6" (on Python 2.6).

- `urllib.request.urlopen(url,data=None[,timeout])`:url可以是网址/Request对象。

- `response.read()`:解码网页代码，返回bytes-like。需要`decode('utf-8')`进行解码

## 3. 翻译脚本的编写
> 利用Chrome进行抓包分析，这里考虑到网速和墙以及翻译效果的问题，我们采用有道翻译。具体可以看注释。


