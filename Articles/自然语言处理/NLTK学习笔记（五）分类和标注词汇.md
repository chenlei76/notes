[TOC]
## 词性标注器
> 之后的很多工作都需要标注完的词汇。nltk自带英文标注器`pos_tag`

```python
import nltk
text = nltk.word_tokenize("And now for something compleyely difference")
print(text)
print(nltk.pos_tag(text))
```

***

## 标注语料库
### 表示已经标注的标识符:`nltk.tag.str2tuple('word/类型')`

```python
text = "The/AT grand/JJ is/VBD ."
print([nltk.tag.str2tuple(t) for t in text.split()])
```

### 读取已经标注的语料库
> nltk语料库ue肚脐提供了统一接口，可以不必理会不同的文件格式。格式:`语料库.tagged_word()/tagged_sents()`。参数可以指定categories和fields

```python
print(nltk.corpus.brown.tagged_words())
```

### 名词、动词、形容词等
> 这里以名词为例
```python
from nltk.corpus import brown
word_tag = nltk.FreqDist(brown.tagged_words(categories="news"))
print([word+'/'+tag for (word,tag)in word_tag if tag.startswith('V')])
################下面是查找money的不同标注#################################
wsj = brown.tagged_words(categories="news")
cfd = nltk.ConditionalFreqDist(wsj)
print(cfd['money'].keys())
```

### 尝试找出每个名词类型中最频繁的名词
```python
def findtag(tag_prefix,tagged_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (word,tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag,list(cfd[tag].keys())[:5]) for tag in cfd.conditions())#数据类型必须转换为list才能进行切片操作

tagdict = findtag('NN',nltk.corpus.brown.tagged_words(categories="news"))
for tag in sorted(tagdict):
    print(tag,tagdict[tag])
```

### 探索已经标注的语料库
> 需要`nltk.bigrams()`和`nltk.trigrams()`，分别对应2-gram模型和3-gram模型。

```python
brown_tagged = brown.tagged_words(categories="learned")
tags = [b[1] for (a,b) in nltk.bigrams(brown_tagged) if a[0]=="often"]
fd = nltk.FreqDist(tags)
fd.tabulate()
```

***

## 自动标注

### 默认标注器
> 最简单的标注器是为每个标识符分配统一标记。下面就是一个将所有词都变成NN的标注器。并且用`evaluate()`进行检验。当很多词语是名词时候，它有利于第一次分析并提高稳定性。

```python
brown_tagged_sents = brown.tagged_sents(categories="news")

raw = 'I do not like eggs and ham, I do not like them Sam I am'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')#创建标注器
print(default_tagger.tag(tokens)) # 调用tag()方法进行标注
print(default_tagger.evaluate(brown_tagged_sents))
```

### 正则表达式标注器
> 注意这里规则是固定（由自己决定）。当规则越来越完善的时候，精确度越高。

```python
patterns = [
    (r'.*ing$','VBG'),
    (r'.*ed$','VBD'),
    (r'.*es$','VBZ'),
    (r'.*','NN')#为了方便，只有少量规则
]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.evaluate(brown_tagged_sents)
```

### 查询标注器
> 这里和书里是有差别的，不同于python2，注意调试。而查询标注器就是存储最有可能的标记，并且可以设置`backoff`参数，不能标记的情况下，就使用这个标注器（这个过程是**回退**）

```python
fd = nltk.FreqDist(brown.words(categories="news"))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories="news"))
##############################################python2和3的区别#########
most_freq_words = fd.most_common(100)
likely_tags = dict((word,cfd[word].max()) for (word,times) in most_freq_words)
#######################################################################
baseline_tagger = nltk.UnigramTagger(model=likely_tags,backoff=nltk.DefaultTagger('NN'))
baseline_tagger.evaluate(brown_tagged_sents)
```

***

## N-gram标注

### 基础的一元标注器
> 一元标注器的行为和查找标注器很相似，建立一元标注器的技术，为**训练**。<br>
这里我们的标注器只是记忆训练集，而不是建立一般模型，那么吻合很好，但是不能推广到新文本。

```python
size = int(len(brown_tagged_sents)*0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size+1:]
unigram_tagger = nltk.UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)
```

### 一般的N-gram标注器
> N元标注器，就是检索index= n 的 word，并且检索n-N<=index<=n-1 的 tag。即通过前面词的tag标签，进一步确定当前词汇的tag。类似于`nltk.UnigramTagger()`，自带的二元标注器为:`nltk.BigramTagger()`用法一致。

### 组合标注器
> 很多时候，覆盖范围更广的算法比精度更高的算法更有用。利用`backoff`指明**回退标注器**,来实现标注器的组合。而参数`cutoff`显式声明为int型，则会自动丢弃只出现1-n次的上下文。

```python
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents,backoff=t0)
t2 = nltk.BigramTagger(train_sents,backoff=t1)
t2.evaluate(test_sents)
```
可以发现，和原来比较之后，精确度明显提高

### 跨句子边界标注
> 对于句首的单词，没有前n个单词。解决方法：通过已标记的tagged_sents来训练标注器。

***

## 基于转换的标注：Brill标注器
> 较上面的都优秀。实现的思路：以大笔化开始，然后修复细节，一点点进行细致改变。<br>不仅占用内存小，而且关联上下文，并且根据问题的变小，实时修正错误，而不是一成不变的。当然，在python3和python2的调用有所不同。

```python
from nltk.tag import brill
brill.nltkdemo18plus()
brill.nltkdemo18()
```

***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***