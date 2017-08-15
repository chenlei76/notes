# 目录
[TOC]

***
## nltk资料下载

```python
import nltk
nltk.download()
```
其中,`download()` 参数默认是all,可以在脚本里面加上`nltk.download(需要的资料库)` 来进行下载<br>

***

## 文本和词汇
首先，通过`from nltk.book import *` 引入需要的内置9本书
### 搜索文本
上下文：`Text.concordance('monstrous')` ，concordance是一致性的意思。即在Text对象中monstrous出现的上下文

相同上下文单词：`Text.similar('monstrous')` ,查找哪些词还有相同的上下文 。（比如 the__size 空格上可以是big/small），这个函数会自动找出来并返回。

多个单词上下文: `Text.common_contexts(['very','monstrous'])` ,返回共用两个或两个以上词汇的上下文

多个单词频率绘图工具： `Text.dispersion_plot(['citizens','freedom'])` , 可以得到很好看的离差散点图

### 计数词汇(去重、定位)
不去重的计算用BIF里面的*len()* 就可以了:`len(text1)`<br>
**去重计算** 需要用到内置结构**set**: `len(set(text1))`<br>
可以使用nltk内置BIF：`Text.count(word)` 查找单词出现次数；使用`Text.index(word)`可以进行定位

***
## 词链表
> 主要是结合python内置list的特点，可以进行链接等一些链表操作，十分方便，对于一些基本的list操作，可以自行看文档

***

## 自然语言简单数学统计

### 频率分布
用法：`FreqDist(WordList)` ，参数可以实List或者其子类，所以 Text（text1，text2...）也可以作为参数。函数返回字典形式，可以调用`dict.keys()` 查询所有单词和符号
```python
from nltk import *
fdist = FreqDist(text1)
print(fdist['whale'])
```
可以通过 `fdist.plot(TopK,cumulative=True)` 画出来出现频率前K的词汇的光滑曲线，去掉第二个参数，是折线图。个人感觉曲线好看。。。<br>
对于只出现一次的词汇，通过`fdist.hapaxes()` 返回的list查看。

### 细粒度的选择词
> 细粒度: 细粒度模型,通俗的讲就是将业务模型中的对象加以细分,从而得到更科学合理的对象模型,直观的说就是划分出很多对象。对于词汇，我们可能需要长度大于5的不重复词汇，这就是一个Model

```python
v = set(text1)
long_words = [w for w in v if len(w) > 5]
```
如果我们需要频率大于7，长度大于10的呢？
```python
fdist = FreqDist(text1)
long_words = [w for w in set(text1) if len(w)>10 and fdist[w] > 7]
```

### 双连词和词汇搭配
> 双连词就是n-gram模型中n=2，组成的词链表

在nltk里面有BIF，`bigrams(wordlist)` ,生成词链表
```python
>>> list(bigrams(['a','b','c']))
[('a', 'b'), ('b', 'c')]
```
通过这个词链表，我们可以找到搭配（定义：不经常在一起出现的词序列）.`Text.collocations()` 可以查找出现频率比预期频率更频繁的双连词
```python
>>> text4.collocations()
United States; fellow citizens; four years; years ago; Federal
Government; General Government; American people; Vice President; Old
World; Almighty God; Fellow citizens; Chief Magistrate; Chief Justice;
God bless; every citizen; Indian tribes; public debt; one another;
foreign nations; political parties
```

### 词长分布
代码实现：
```python
fdist = FreqDist([len(w) for w in text1])
print(fdist.items())
print(fdist.freq(3))#查找频率
```
词长可以帮助我们理解作者、文本和语言之间的差异