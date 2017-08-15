[toc]

> 写一篇笔记，记录一下常见的**sql函数**，以备之后的查找需要。

## 算数函数

#### abs(num)：绝对值函数

#### mod(被除数,除数)：求余函数

#### round(num,保留小数的位数):四舍五入函数


## 字符串函数

#### concat(str1,str2):拼接字符串函数

#### length(str):字符串长度

#### lower(str)/upper(str):小/大写函数

#### replace(对象str,要替换的str,替换后的str)：字符串替换函数

#### substring(字符串,开始位置,截取长度)：截取字符串


## 日期函数

#### current_date:当前日期。`select current_date;`

#### current_time

#### current_timestamp:返回当前日期+时间

#### extract(日期元素 from 日期):截取日期元素
示例：`select extract(year from current_timestamp) as year;`

日期元素还可以是：month,day,hour,minute,second

#### `year`/`month`/`day`日期转化字符
有些时候结合`where`使用时，`extract`实现一种功能会很麻烦。假设有一列pub_data，里面的类型是varchar类型，但是代表的是日期（例如：2017-05-15）。存成varchar类型可能为了其他的程序读取或者其他的软件整理。

如果想提取这一列中大于2017年的数据，可以：
```sql
select * from myTable where year(pub_date)>2017;#month、day用法相似
```


## 转化函数

#### cast：类型转换
示例：
```sql
select cast('0001' as signed integer) as int_col;
select cast('2017-12-14'as date) as date_col;
```

#### coalesce(数据1,数据2,...)：将null转化为其他值
> 参数可以有无限个，返回可变参数左侧开始第一个不是`null`的值。所以，包含`null`的列，就可以转化为其他的值，结果就不是`null`了。

示例：
```sql
select coalesce(null,1) as col_1,
	coalesce (null,'test',null) as col_2;
```


## 聚合函数
> 见之前的博客


***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***