[toc]

> 这是一篇纯粹的乱七八糟的笔记。。。（勿喷）主要记录一下初入SQL坑的杂七杂八的注意事项。

一、先补充下事务的写法：
```sql
start transaction;#开始事务
    --各种事务...
commit;#将上述的事务一次性提交
```

当然如果小心翼翼防止一些错误的决定，可以：
```sql
start transaction;
    --各种事务...
rollback;#回滚命令，相当于以上各种事务没有执行
```

在DB2、Oracle中没有`start transaction;`，在SQLSEVER和PostgreSQL中是`begin transaction;`

---

二、字符类型

`varchar`是可变长度字符串，`char`是不可变长度字符串（用`空格`填充）

---

三、插入数据

如果想一次性插入多行数据：
```sql
insert into access_log values(col1,col2...),(col1,col2...),...
;
```

插入`NULL`时候，最好显性指明插入。

如果插入默认值，可以使用`default`关键词。

---

四、`distinct`函数

例如这句话：`select count(distinct myID) from forLearn;`。**可以发现，`distinct`要写在括号里面，先删除列中重复数据**。否则先计算行数，再删除重复数据，得到的就是所有行数。

---

五、[数据库恢复]
[教程1](http://bbs.csdn.net/topics/310068149)

[教程2](http://kerry.blog.51cto.com/172631/146259/)



[Windows下启动mysqlbinlog](http://blog.csdn.net/aitangyong/article/details/53114633)

[windows下启动MySQL：](http://www.cnblogs.com/java-class/p/4279389.html)