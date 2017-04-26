
#coding=utf-8
import re


m=raw_input()
n=raw_input()
path ='/home/yun/作业/'
r_path =path +'结果/'

def focus(m,n):
    pa =path + '词典/' + m +'/' + n
    if n !='试听效果中的其他':
        pa =pa +'.txt'
    with open(pa,'r') as p:
        for line in p.readlines():
            if n =='选景':
                line =line.decode('gb2312').encode('utf8')
            if line !='\n':
                #line=line.strip()

                line =re.sub('\n','',line)
                line =re.sub(' ','',line)

                with open(path+'太空旅客.txt','r') as f:
                    with open(r_path+m+'/'+n,'a') as w:
                        w.write(line +':' +str(len(re.findall(line, f.read())))+'\n')
focus(m,n)




