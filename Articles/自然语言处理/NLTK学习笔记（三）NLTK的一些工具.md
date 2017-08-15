[toc]

> 主要总结一下简单的工具：条件频率分布、正则表达式、词干提取器和归并器。

***

## 条件分布频率
> 《自然语言学习》很多地方都用到了条件分布频率，nltk提供了两种常用的接口：`FreqDist` 和 `ConditionalFreqDist` 。后面很多都会用到这两种方法，特别是第二个。因为第二个更符合定义，会智能的找到条件。
然后根据绘图的库，可以做出来很漂亮的图形。

#### 简单的`FreqDist`
函数接收list类型的参数后，会自动创建字典，生成对应的值为键值，而value就是元素的次数。
```python
from nltk import *
tem = ['hello','world','hello','dear']
print(FreqDist(tem))
```
    out:
    FreqDist({'dear': 1, 'hello': 2, 'world': 1})

通过 `plot(TopK,cumulative=True)` 和 `tabulate()` 可以绘制对应的折线图和表格（必须安装matplotlib库）

#### 条件分布`ConditionalFreqDist`
> 以一个配对链表作为输入，需要给分配的每个事件关联一个条件，输入时类似于 `(条件,事件)` 的元组。之后的工作交给nltk就可以了，更多的精力可以用来关注上层逻辑。

```python
import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist((genre,word) for genre in brown.categories() for word in brown.words(categories=genre))
print("conditions are:",cfd.conditions()) #查看conditions
print(cfd['news'])
print(cfd['news']['could'])#类似字典查询
```
    out:
    conditions are: ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
    <FreqDist with 14394 samples and 100554 outcomes>
    86

尤其对于`plot()` 和 `tabulate()` 有了更多参数选择：
- conditions：指定条件
- samples：迭代器类型，指定取值范围
- cumulative：设置为True可以查看累积值

```python
cfd.tabulate(conditions=['news','romance'],samples=['could','can'])
cfd.tabulate(conditions=['news','romance'],samples=['could','can'],cumulative=True)
```
            could   can 
    news    86    93 
    romance   193    74 

            could   can 
    news    86   179 
    romance   193   267 

***

## 正则表达式及其应用
> 记录正则表达式在自然语言中的应用。

#### 输入法联想提示（9宫格输入法）
查找类似于hole和golf序列（4653）的单词。
```python
import re
from nltk.corpus import words
wordlist = [w for w in words.words('en-basic') if w.islower()]
same = [w for w in wordlist if re.search(r'^[ghi][mno][jlk][def]$',w)]
print(same)
```
只用键盘的一部分搜索就是*手指绕口令*。例如：`^[ghijklmno]+$`等。像`[^aeiouAEIOU]`就是匹配除元音外的所有字母。

#### 寻找字符块
查找两个或两个以上的元音序列，并且确定相对频率。
```python
import nltk
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}',word))
fd.items()
```
而且，我们也可以辅音元音序列。

#### 查找词干
apples和apple对比中，apple就是词干。写一个简单脚本来查询词干。
```python
def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return None
```
而使用正则表达式，只需要一行：
```python
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$',word)
```

***

### 词干提取器和归并器
nltk提供了`PorterStemmer` 和 `LancasterStemmer`两个词干提取器，Porter比较好，可以处理lying这样的单词。
```python
porter = nltk.PorterStemmer()
print(porter.stem('lying'))
```
如果需要处理women这样的词，需要词性归并器：`WordNetLemmatizer`
```python
wnl = nltk.WordNetLemmatizer()
print(wnl.lemmatize('women'))
```
#### 利用词干提取器实现索引文本(concordance)
利用到nltk.Index这个函数，`nltk.Index((word , i) for (i,word) in enumerate(['a','b','a']))`
```python
class IndexText:
    def __init__(self,stemmer,text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word),i) for (i,word) in enumerate(text))
    def _stem(self,word):
        return self._stemmer.stem(word).lower()
    def concordance(self,word,width =40):
        key = self._stem(word)
        wc = width/4 #words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[int(i-wc):int(i)])
            rcontext = ' '.join(self._text[int(i):int(i+wc)])
            ldisplay = '%*s' % (width,lcontext[-width:])
            rdisplay = '%-*s' % (width,rcontext[:width])
            print(ldisplay,rdisplay)
porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')
text = IndexText(porter,grail)
text.concordance('lie')
```