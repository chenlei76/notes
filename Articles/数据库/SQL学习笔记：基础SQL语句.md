[TOC]
## 语句特点
1. 每一句结尾都有`;`。**所以注意换行，来增加可读性。**
2. 大小写不敏感。**命令一般全大写，便于区分。**
3. 当遇到差异的时候，以MySQL为基础进行笔记整理

## 进入数据库
1. 选择数据库：`use name;`
2. 设置字符集：`set names 字符编码方式;`

## 基本查询语句

### SELECT

```sql
SELECT column_name,...
FROM table_name;
```

如果是全选：`SELECT * FROM Websites;`

### DISTINCT

DISTINCT 关键词用于返回唯一不同的值。**它和很多语法/函数都有组合。**。

```sql
SELECT DISTINCT column_name,...
FROM table_name;
```

### WHERE

WHERE 子句用于提取那些满足指定标准的记录。

```sql
SELECT column_name,...
FROM table_name
WHERE 表达式;
```

表达式的基本形式式：`column_name operator value`

而operator比较特别：

|运算符	|描述|
|-|-|
|=	|等于|
|<>|	不等于。注释：在 SQL 的一些版本中，该操作符可被写成 !=
|>|	大于|
|<|小于|
|\>=|大于等于|
|<=|	小于等于|
|BETWEEN	|在某个范围内|
|LIKE|	搜索某种模式|
|IN|	指定针对某个列的多个可能值|

**BETWEEN在不同的sql中左右区间是否取闭不相同。所以这里建议用>/</>=/<=**

#### IN

类似于python的in操作符：
```sql
Select * from emp where sal in (5000,3000,1500);
```

#### LIKE：模糊搜索
示例:`Select * from emp where ename like 'M%';`.注意`''`单引号包裹相应的表达式。

查询 EMP 表中 Ename 列中有 M 的值，M 为要查询内容中的模糊信息。
 - % 表示多个字值，_ 下划线表示一个字符；
 - M% : 为能配符，正则表达式，表示的意思为模糊查询信息为 M 开头的。
 - %M% : 表示查询包含M的所有内容。
 - %M_ : 表示查询以M在倒数第二位的所有内容。

### AND/OR/NOT ：逻辑运算符

和编程语言的用法一致，也支持对括号的先运算。示例
```sql
select * from learn 
where (not id = 4 )and id<= 3;
```

### ORDER BY :排序

ORDER BY 关键字用于对结果集按照一个列或者多个列进行排序。默认按照升序对记录进行排序(`ASC`关键字)。如果需要按照降序对记录进行排序，可以使用 `DESC` 关键字。

语法：
```sql
SELECT column_name,column_name
FROM table_name
ORDER BY column_name,column_name ASC|DESC;
```

对多列排序的时候，排序的顺序是由`order by`后面的列的顺序绝对的。类似于python里面的`sorted`函数。

## 基本修改语句

### INSERT：添加语句

语法：
```sql
INSERT INTO table_name
VALUES (value1,value2,value3,...);
```

如果只是插入特定的列：
```sql
INSERT INTO table_name(col_name,...)
VALUES (value1,value2,value3,...);
```

### UPDATE：修改（更新）语句

必须和`WHERE`语句搭配使用：**WHERE 子句规定哪条记录或者哪些记录需要更新。如果您省略了 WHERE 子句，所有的记录都将被更新！**

语法：
```sql
UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;
```

实例 ：`update learn set url='www.kengni.com' where id =4;`

### DELETE： 删除记录

**WHERE 子句规定哪条记录或者哪些记录需要删除。如果您省略了 WHERE 子句，所有的记录都将被删除！**

所以，`DELETE * FROM table_name;` 和 `DELETE FROM table_name;`都会清空数据库，但会保持原来的结构不变，只是清空数据。

一般的语法是这样的：
```sql
DELETE FROM table_name
WHERE some_column=some_value;
```

***

> 欢迎进一步交流本博文相关内容：<br>
博客园地址 : <http://www.cnblogs.com/AsuraDong/><br>
CSDN地址 : <http://blog.csdn.net/asuradong><br>
也可以致信进行交流 : <xiaochiyijiu@163.com> <br>
**欢迎转载** , 但*请指明出处 &nbsp;:&nbsp;&nbsp;)*

***