m=raw_input() : 键盘输入词典目录名
n=raw_input() : 键盘输入词典目录下的.txt文本名

path、r_path、pa都是用于设置路径

把'选景.txt'的文本格式改为utf8格式

line =re.sub('\n','',line)
line =re.sub(' ','',line)    用于去掉词条上的换行符，空格符


总结：这代码是我参考同学并进一步改进而来的，通过同学的帮助我大概了解到正则表达式匹配的一些用法，如re.sub(),re.findall()等函数
此次作业让我对python的基本用法有了更深的理解，感觉收入良多。
