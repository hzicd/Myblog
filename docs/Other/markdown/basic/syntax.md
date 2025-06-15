---
layout: doc
text: Markdown的基本语法学习
---
# Markdown学习
## 基本语法  
### 一、标题
```markdown
# 一级标题
## 二级标题
### 三级标题 
...
###### 六级标题

#后面是有一个空格的，下面的语法大部分基本也是有的 //[!code error]
```
![](/title.png)
### 二、段落  
```markdown
这是一个段落
这是第二个段落
实现上面两行这样的效果，需要在第一行结尾加tab键（即两个空格）和一个回车键
```
### 三、强调文本
```markdown
*斜体文本*或者_斜体文本_
**加粗文本**或者__加粗文本__
***加粗并斜体***或者___加粗并斜体
~~删除线~~
```
![](/xieti.png)
### 四、列表
#### 无序列表
```markdown
- 列表项 1
- 列表项 2
或
* 列表项 1
* 列表项 2
或
+ 列表项 1
+ 列表项 3
```
![](/list.png)
#### 有序列表
```markdown
1. 第一项
2. 第二项
3. 第三项
```
### 五、链接
```mardown
文字的连接
[文本](链接地址 '该链接的提示信息')


图片的链接
![代替文本](链接图片地址) 

```
![](/baidu.png)
### 六、代码块
```markdown
两对```反引号,把代码写入里面即可像我这样的代码块
第一个```后面及加入代码语言如：python，右侧即可实现右上角代码说明
markdown支持的有：
bash
clojure，cpp，cs，css
dart，dockerfile, diff
erlang
go，gradle，groovy
haskell
java，javascript，json，julia
kotlin
lisp，lua
makefile，markdown，matlab
objectivec
perl，php，python
r，ruby，rust
scala，shell，sql，swift
tex，typescript
verilog，vhdl
xml
yaml
```