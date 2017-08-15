[toc]

> **首先声明一下，`exist`和`case`没有必然联系，这里只是为了一起整理个笔记。**

## `EXIST`谓词

> 如果存在对应的记录，返回`TRUE`。否则，返回`FALSE`。*实际使用中，即使不适用`exist`，基本也可以使用`in`或者`not in`来代替。

示例：
```sql
select shohin_mei ,hanbai_tanka from Shohin as S
where exists
( select * from TenpoShohin as TS 
  where TS.tenpo_id = '000C' and TS.shohin_id = S.shohin_id);
```

通过这个例子发现：**`exist`通常会使用关联子查询作为参数。**

当然，用`in`代替：(更容易理解)
```sql
select shohin_mei,hanbai_tanka from Shohin
where shohin_id in 
( select shohin_id from TenpoShohin where tenpo_id = '000C');
```

## `case`表达式

语法：
```sql
case when <判断表达式> then <表达式>
    when <判断表达式> then <表达式>
    when <判断表达式> then <表达式>
    when <判断表达式> then <表达式>
    ...
    else <表达式>
end;
```
从语法中可以发现，类似于c等高级语言的`switch`语法。

示例：
```sql
select shohin_mei,
  case when shohin_bunrui='衣服' then concat('A:',shohin_bunrui)
  when shohin_bunrui = '办公用品' then  concat('B:',shohin_bunrui)
	when shohin_bunrui = '厨房用具' then concat('C:',shohin_bunrui)
	else null
  end 
	as abc_shohin_bunrui
from Shohin;
```

所以，我们发现，**`case`语句可以写在任意位置。**

这里再看一个用法，用`group by`按照种类得到商品的和（行输出）。`case`语句，可以实现列输出。

```sql
select shohin_bunrui,sum(hanbai_tanka) as sum_tabka 
from Shohin
group by shohin_bunrui;

#接下来是case语句实现按类列输出
select sum(case when shohin_bunrui = '衣服' then hanbai_tanka else 0 end) as sum_tabka_ihuku,
  sum(case when shohin_bunrui = '厨房用具' then hanbai_tanka else 0 end) as sum_tabka_ihuku,
	sum(case when shohin_bunrui = '办公用品' then hanbai_tanka else 0 end) as sum_tabka_ihuku
from Shohin;
```


（原始数据集：
```
0002	打孔器	办公用品	500	320	2009-09-11
0003	运动T恤	衣服	4000	2800	
0004	菜刀	厨房用具	3000	2800	2009-09-20
0005	高压锅	厨房用具	6800	5000	2009-01-15
0006	叉子	厨房用具	500		2009-09-20
0007	擦菜板	厨房用具	880	790	2008-04-28
0008	圆珠笔	办公用品	100		2009-11-11
```
)


***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***

