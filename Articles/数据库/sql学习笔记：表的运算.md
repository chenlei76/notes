[toc]

> 在MICK的《SQL基础教程》里读到的一章，写的很好，之前很乱的思路变清晰了很多。简单来说，表的运算主要是两种：列的运算和行的运算。

## 表的加减法

这里是对表的列操作(向下扩展)。因此，按照常理，我们需要注意：
1. 作为运算对象的列的类型要一致
2. 两个表选择出来的列的列数要相同：`select a,b from tableA union select a from tableB;`就不正确
3. **`order by`子句只能在最后使用一次，即只能进行一次分组**

#### 关键字
- 表的加法`UNION`：选择并集（所以重复的部分就只出现一次）。如果想包含重复行，请用`union all`
- 表的公共部分`intersect`:选择交集（MySQL不能用）
- 表的减法`except`:差集（MySQL不能用）

#### MYSQL实现交集和差集

建立两张表：
```sql
create table t1(id int primary key,nickname varchar(20),playNum varchar(20));
create table t2(id int primary key,nickname varchar(20),playNum varchar(20));
insert into t1 values(1,1,10);
insert into t1 values(2,2,20);
insert into t1 values(3,3,30);
insert into t2 values(1,1,10);
insert into t2 values(2,2,200);
insert into t2 values(3,33,300);
```

一、**实现交集**：
```sql
SELECT id, nickname, playNum, COUNT(*)
FROM (SELECT id, nickname, playNum
    FROM t1
    UNION ALL
    SELECT id, nickname, playNum
    FROM t2
    ) as temp

GROUP BY id, nickname, playNum
HAVING COUNT(*) > 1;
```

思路如下：
1. 取两个表的全集
2. 次数大于1的就是交集

二、**实现差集**

对于小的数据集，可以使用`not in`来实现，大的数据集效率很低（可以去试试）。下面提供一种思路：
```sql
SELECT t1.id, t1.nickname, t1.playNum
FROM t1 LEFT JOIN t2 ON t1.id = t2.id
WHERE t1.nickname != t2.nickname
    OR t1.playNum != t2.playNum;
```

三、参考博客：http://www.linuxidc.com/Linux/2014-06/103551.htm

---

## 联结
**这里是对行进行操作（向右扩展）。**

格式：`select col,... from table inner/full/right/left join table2 on ...;`

- `FULL JOIN`:全连接，显示两个表的所有信息（即是没有匹配，on的条件为假）。**MySQL不支持全连接**
- `INNER JOIN`：内连接。显示的是表相关的信息（on的条件为真，**此时on和where形同**）
- `LEFT JOIN`:左表是主表。返回的是主表和别的表的相关信息。
- `RIGHT JOIN`:右表是主表。


[主表的判断可以来这里看看代码就懂了。](http://blog.csdn.net/shadowyelling/article/details/7684714)

### 三张以上表的联结
虽然不建议这样弄，但是还是记录一下：
```sql
select TS.col ,S.col
from TS INNER JOIN S
on TS.id= S.id
    INNER JOIN ZS
        ON ZS.id = TS.id
;
```
我理解的思路就是：新生成的集合再次操作。