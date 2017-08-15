[toc]

> 现在以MySQL为模板。学习的方法和别的数据库写法上会有不同，但是思路基本一致。

用到的数据库表的格式：
```
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 7  | stackoverflow | http://stackoverflow.com/ |   0 | IND     |
+----+---------------+---------------------------+-------+---------+
Website

+-----+---------+-------+------------+
| aid | site_id | count | date       |
+-----+---------+-------+------------+
|   1 |       1 |    45 | 2016-05-10 |
|   2 |       3 |   100 | 2016-05-13 |
|   3 |       1 |   230 | 2016-05-14 |
|   4 |       2 |    10 | 2016-05-14 |
|   5 |       5 |   205 | 2016-05-14 |
|   6 |       4 |    13 | 2016-05-15 |
|   7 |       3 |   220 | 2016-05-15 |
|   8 |       5 |   545 | 2016-05-16 |
|   9 |       3 |   201 | 2016-05-17 |
+-----+---------+-------+------------+
access_log
```


### LIMIT：限定语句
适合在成千上万条的记录中检索前几个，并非所有数据库都支持TOP语句。

```sql
select * from learn limit 8;
```

MySQL 不支持`top`和`percent`写法。

### SQL别名
> 通过使用 SQL，可以为表名称或列名称指定别名。基本上，创建别名是为了让列名称的可读性更强。

#### 列别名

**分列别名**：
```sql
SELECT name AS n, alexa AS a
FROM Website;
```

**合并列**
```sql
SELECT name, CONCAT(url, ', ', alexa, ', ') AS site_info
FROM Website;
```

结果如下：*按照自己的格式显示了出来*
```
+----------+------------------------------+
| name     | site_info                    |
+----------+------------------------------+
| 淘宝     | https://www.taobao.com/, 1,  |
| BaiDu    | www.baidu.com, 255,          |
| 随便一个 | NULL                         |
| 修改一下 | NULL                         |
| 京东     | www.jingdong.com, 5,         |
| 京东     | NULL                         |
+----------+------------------------------+
6 rows in set
```

#### 表的别名：通过使用别名让 SQL 更简短
```sql
select w.name,w.name,a.date from Website as w,access_log as a
where a.site_id = w.id ;
```

### JOIN
> SQL join 用于把来自两个或多个表的行结合起来。

格式：`select col,... from table inner/full/right/left join table2 on ...;`

- `FULL JOIN`:全连接，显示两个表的所有信息（即是没有匹配，on的条件为假）。**MySQL不支持全连接**
- `INNER JOIN`：内连接。显示的是表相关的信息（on的条件为真，**此时on和where形同**）
- `LEFT JOIN`:左表是主表。返回的是主表和别的表的相关信息。
- `RIGHT JOIN`:右表是主表。

[主表的判断可以来这里看看代码就懂了。](http://blog.csdn.net/shadowyelling/article/details/7684714)

### UNOIN
操作符合并两个或多个 SELECT 语句的结果。

语法：
```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

下面是`UNION`和 `select ... from table1,table2;`的区别：
```
+----+----------+-------------------------+------------+
| id | name     | url                     | alexa      |
+----+----------+-------------------------+------------+
|  2 | 淘宝     | https://www.taobao.com/ | 1          |
|  3 | BaiDu    | www.baidu.com           | 255        |
|  4 | 随便一个 | www.kengni.com          | NULL       |
|  0 | 修改一下 | b                       | NULL       |
|  5 | 京东     | www.jingdong.com        | 5          |
|  5 | 京东     | www.jingdong.com        | NULL       |
|  1 | 3        | 45                      | 2016-05-10 |
|  2 | 4        | 69                      | NULL       |
+----+----------+-------------------------+------------+
此时的列名字是根据table1来绝对的。

+-----+---------+-------+------------+----+----------+-------------------------+-------+
| aid | site_id | count | date       | id | name     | url                     | alexa |
+-----+---------+-------+------------+----+----------+-------------------------+-------+
|   1 |       3 |    45 | 2016-05-10 |  2 | 淘宝     | https://www.taobao.com/ |     1 |
|   2 |       4 |    69 | NULL       |  2 | 淘宝     | https://www.taobao.com/ |     1 |
|   1 |       3 |    45 | 2016-05-10 |  3 | BaiDu    | www.baidu.com           |   255 |
|   2 |       4 |    69 | NULL       |  3 | BaiDu    | www.baidu.com           |   255 |
|   1 |       3 |    45 | 2016-05-10 |  4 | 随便一个 | www.kengni.com          | NULL  |
|   2 |       4 |    69 | NULL       |  4 | 随便一个 | www.kengni.com          | NULL  |
|   1 |       3 |    45 | 2016-05-10 |  0 | 修改一下 | b                       | NULL  |
|   2 |       4 |    69 | NULL       |  0 | 修改一下 | b                       | NULL  |
|   1 |       3 |    45 | 2016-05-10 |  5 | 京东     | www.jingdong.com        |     5 |
|   2 |       4 |    69 | NULL       |  5 | 京东     | www.jingdong.com        |     5 |
|   1 |       3 |    45 | 2016-05-10 |  5 | 京东     | www.jingdong.com        | NULL  |
|   2 |       4 |    69 | NULL       |  5 | 京东     | www.jingdong.com        | NULL  |
+-----+---------+-------+------------+----+----------+-------------------------+-------+
```

**所以前者是表的上下对接，后者是左右直接拼接。UNION主要对同一结构的多个表有用。**

### INSERT INTO SELECT：复制信息

从一个表复制数据，然后把数据插入到一个已存在的表中。目标表中任何已存在的行都不会受影响。

复制所有的信息到目标表中：
```sql
INSERT INTO table2
SELECT * FROM table1;
```

复制部分信息到目标表中：
```sql
INSERT INTO table2
(column_name(s))
SELECT column_name(s)
FROM table1;
```

创建一个新表，并且复制table2的结构和数据：
```sql
CREATE TABLE table1 SELECT * FROM table2;
```

***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***