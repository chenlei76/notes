[TOC]

## 创建和删除数据库

```sql
CREATE DATABASE justForLearn;
```

```sql
DROP DATABASE justForLearn;
```



## 创建和删除表

语法：
```sql
CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);
```

```sql
DROP TABLE table_name;
```

**如果只删除数据，不破坏结构：**
```sql
DELETE FROM  table_name;
```

## 添加、修改和删除字段

添加字段：
```sql
ALTER TABLE table_name
ADD column datatype;
```

修改字段
```sql
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

删除字段：
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```


***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***
