# import re
# from contextlib import contextmanager
#
# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_name_age(self):
#         print('名字是%s, 年龄是%s' % (self.name, self.age))
# @contextmanager
# def contextInstance(tag):
#     print('这是上文')
#     yield
#     print('这是下文')
#
# # with contextInstance('上下文示例'):
# #     s = Student('小张', 20)
# #     s.show_name_age()
#
# exp = 'bnCh_7s'
# print(re.match(exp, 'bnCh_7s'))
#
# exp = r"[]-]{2}"
# print(re.match(exp, "]-"))
#
# exp = r'ol\b'
# print(re.match(exp, 'ol'))
#
# exp = r'ol$'
# print(re.findall(exp, 'asfeaol '))
#
# exp = r'^ol'
# print(re.findall(exp, 'olasfe\nolsafe'))
#
# exp = r"^(login)(\\)\1\2$"
# print(re.match(exp, "login\\login\\"))
#
# str_ip = "123.45.78.9"
# exp = r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# print(re.match(exp, str_ip))
#
# str_ip = "lili.brown sam.zhang 1.2.3"
# #exp = "(?:(?:[a-zA-Z]+)\.)*(?:[a-zA-Z]+)"
# exp = "(([a-zA-Z]+)\.)*([a-zA-Z]+)"
# print(re.findall(exp, str_ip))

# with open('test2.txt','a', encoding='utf-8') as f:
#     f.write('\n你好啊')
#     f.close()


import pymysql
import datetime


class DbManager(object):
    def __init__(self):
        self.con = pymysql.connect(host='39.108.134.38',
                                   user='root',
                                   password='123456',
                                   db='test',
                                   port=3306)
        self.cursor = self.con.cursor()

    def createTable(self, sql):
        try:
            self.cursor.execute(sql)
            print('sucess !')
        except Exception as e:
            print("fail to create table , case: {}".format(e))
            self.con.rollback()

    def insertRecord(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("fail to insert table , case: {}".format(e))

    def queryData(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            create_time = row[5]
            dt = datetime.datetime.strptime("{}".format(create_time), "%Y-%m-%d %H:%M:%S")
            print(fname, lname, age, sex, income, create_time)

    def deleteData(self, sql):
        try:
            self.cursor.execute(sql)
            print('delete successful!')
        except Exception as e:
            print('fail to delete data: {}'.format(e))

    def closeDb(self):
        self.con.commit()
        self.con.close()


import datetime
# db = DbManager()
#
# alist = []
# blist = ['姓名','工号','','']
# for i in range(5):
#     alist.append(input("请输入%s:") % blist[i])
# # alist = [input('请输入{}:'.format(blist(i))) for i in range(5)]
# sql = 'insert into test_table values ("{}", "{}", "{}", "{}","{}", "{}")'\
#     .format(alist[0], alist[1], alist[2], alist[3], int(alist[4]), datetime.datetime.now())
# db.insertRecord(sql=sql)
# if __name__ == '__main__':
#     db = DbManager()  # 实例化DbManager对象
#     sql0 = 'create table test_table(first_name char(20) not null ,last_name char(20),age int,sex char(1),income float,create_time datetime)'
#     # db.createTable(sql0) # 建表
#     sql1 = 'insert into test_table values ("{}", "{}", "{}", "{}","{}", "{}")'.format('张', '三', '18', '男', 1800, datetime.datetime.now())
# sql2 = 'insert into test_table values ("{}", "{}", "{}", "{}","{}", "{}")'.format('李', '四', '20', '男', 1800, datetime.datetime.now())
#     sql3 = 'select * from test_table'
#     sql4 = 'delete from test_table where age = {}'.format(18)
#     db.insertRecord(sql1) # 插数据
#     # db.queryData(sql3)  # 查数据
#     db.deleteData(sql4)  # 删数据
#
#
#     # commit and close connect db
#     db.closeDb()

from tkinter import *

# window = Tk()
# window.title('Label and button')
# lblPrincipal = Label(window, text = 'python，从入门到头秃', fg = 'yellow', bg = 'gray')
# lblPrincipal.grid(padx = 120, pady = 15)
# def change_color():
#     db = DbManager()
#     print(db)
#     lblPrincipal['text'] = db
#     db.closeDb()
# def changefgcolor():
#     if entName['fg'] == 'green':
#         entName['fg'] = 'blue'
#     elif entName['fg'] == 'blue':
#         entName['fg'] = 'red'
#     else:
#         entName['fg'] = 'gray'
#
# btn = Button(window, text = "1800", bg = 'light gray', command = change_color)
# btn.grid(padx = 120, pady = 50)
#
# entName = Entry(window, width = 20, fg = 'green')
# entName.grid(padx = 120, pady = 30)
# entName.bind("<Button-1>", changefgcolor())
#
# window.mainloop()

# window = Tk()
#
# def queryData():
#     db = DbManager()
#     sql = 'select * from test_table'
#     try:
#         db.cursor.execute(sql)
#         results = db.cursor.fetchone()
#         conOfEntOutput.set('姓名: {}{}, 年龄: {}, 性别: {}, 收入: {}'.\
#                            format(results[0], results[1], results[2], results[3], results[4]))
#     except Exception as e:
#         conOfEntOutput.set('Error: 无法获取数据，错误信息: {}'.format(e))
#     finally:
#         db.closeDb()
#
# window.title('Readonly Entry Widget')
# conOfEntOutput = StringVar()
# conOfEntOutput.set('我是只读输入控件')
# entName = Entry(window, state = 'readonly', width = 50, textvariable = conOfEntOutput)
# entName.grid(row = 0, column = 0, padx = 100, pady = 15)
# Btn = Button(window, text = '查询', command = queryData)
# Btn.grid(padx = 100, pady = 30)
# window.mainloop()

# def printString(event):
#     curIndex = event.widget.nearest(event.y)
#     print(listname.get(curIndex))
# window = Tk()
# window.title('列表框控件')
# L = ['red', 'yellow', 'light blue', 'orange']
# conOfLstColors = StringVar()
# conOfLstColors.set(tuple(L))
# listname = Listbox(window, width = 20, height = 10, listvariable = conOfLstColors)
# listname.grid(padx = 100, pady = 30)
# listname.bind("<Button-1>", )
# window.mainloop()

# window = Tk()
# window.title('有滚动条的列表框')
# yscroll = Scrollbar(window, orient = VERTICAL)
# yscroll.grid(row = 0, column = 2, rowspan = 4, padx = (0, 100), pady = 5, sticky = NS)
# stateList = ['张三', '李四']
# todo

# -*- coding: utf-8 -*-

from tkinter import *
import pymysql

window = Tk()
window.title("有滚动条的列表框")
##标签
lblPrincipal = Label(window, text="姓名", bg="white")
lblPrincipal.grid(row=0, column=0, padx=10, pady=15, sticky=E)
##输入框
conOfEntOutput = StringVar()
conOfEntOutput.set("我是只读输入控件")
entName = Entry(window, width=20, textvariable=conOfEntOutput)
entName.grid(row=0, column=1, padx=10, pady=15, sticky=W)

##按钮
# def search_name():
#     name = conOfEntOutput.get()
#     firstName = name[0]
#     lastName = name[1:]
#     db = pymysql.connect("localhost", "root", "123", "python")
#     cursor = db.cursor()
#     # SQL查询语句
#     sql = "select * from employee where first_name='%s' && last_name='%s'" \
#           % (lastName, firstName)
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获得所有记录
#         results = cursor.fetchall()
#         infoList = []
#         for i in results:
#             infoList.append("%s,%s,%d,%s,%d" % i[0:5])
#         conOFlstNE.set(tuple(infoList))
#         infoLabel["text"] = "恭喜查询成功!"
#     except Exception as e:
#         print("Error:无法获得数据, 错误信息:%s" % e)
#         infoLabel["text"] = "别气馁,再接再厉!"
#     finally:
#         db.close()
#
#
# btn = Button(window, text="提交", command=search_name)
# btn.grid(row=1, column=0, columnspan=2, padx=15, pady=15)
# ##信息提示
# infoLabel = Label(window, text="欢迎使用查询框！", bg="white")
# infoLabel.grid(row=2, column=0, columnspan=2, padx=1, pady=15, sticky=E)
# ##信息列表
# ##信息列表滚动条
# stateList = []
# conOFlstNE = StringVar()
# conOFlstNE.set(tuple(stateList))
# yscroll = Scrollbar(window, orient=VERTICAL)
# yscroll.grid(row=0, column=3, rowspan=5, padx=(0, 50), pady=5, sticky=NS)
# lstNE = Listbox(window, width=14, height=4, listvariable=conOFlstNE, yscrollcommand=yscroll.set)
# lstNE.grid(row=0, column=2, rowspan=5, padx=(50, 0), pady=5, sticky=E)
# yscroll["command"] = lstNE.yview
# window.mainloop()

import socket


def main_udp():
    # 1. 初始化
    udp_skt = socket.socket(type=socket.SOCK_DGRAM)

    # 2. 发送消息
    udp_skt.sendto('我是udp的客户端'.encode("utf-8"), (socket.gethostname(), 6789))
    # 接收服务端的消息
    server_msg, address = udp_skt.recvfrom(1024)
    print(server_msg.decode())

    udp_skt.close()


def main_tcp(client_msg):
    # 1. 初始化socket
    skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 2. 连接服务端
    skt.connect((socket.gethostname(), 6789))

    # 3. 发送消息
    skt.send(client_msg.encode())
    # 接收server消息
    recv = skt.recv(1024)
    print(recv.decode())

    # 4. 关闭socket连接
    skt.close()


import _thread
from datetime import datetime
from time import sleep

date_time_format = "%y-%m-%d %H:%M:%S"


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop_one():
    print("1 kai shi shi jian:", date_time_str(datetime.now()))
    print("1 sleep 4 miao")
    sleep(4)
    print("1 jie shu shi jian :", date_time_str(datetime.now()))


def loop_two():
    print("2 kai shi shi jian:", date_time_str(datetime.now()))
    print("2 sleep 2 miao")
    sleep(2)
    print("2 jie shu shi jian :", date_time_str(datetime.now()))


def main():
    print("kai shi shi jian :", date_time_str(datetime.now()))
    _thread.start_new_thread(loop_one, ())
    _thread.start_new_thread(loop_two, ())
    sleep(6)
    print("jie shu shi jian:", date_time_str(datetime.now()))


import threading


# class MyThread(threading.Thread):
#     def __int__(self, myName):
#         threading.Thread.__init__(self)
#         self.myName = myName
#     def myFun(self):
#         print('你好啊')
#
#     def run(self):
#         self.myFun()


def recv(serve_socket):
    while True:
        recv_data, skt = serve_socket.recvfrom(1024)
        print('\r\n' + "接收到的消息：%s" % recv_data.decode())


def send(serve_socket, dest_ip, dest_port):
    while True:
        send_data = input("请输入要发送的内容：")
        serve_socket.sendto(send_data.encode(), (dest_ip, dest_port))


def main():
    serve_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_ip = input("请输入目的ip：")
    dest_port = eval(input("请输入目的端口："))

    local_port = 7890

    local_ip = socket.gethostname()
    serve_socket.bind((local_ip, local_port))

    # serve_socket.close()
    sendthread = threading.Thread(target=send, args=(serve_socket, dest_ip, dest_port))
    recvthread = threading.Thread(target=recv, args=(serve_socket,))

    # 启动多线程
    sendthread.start()
    recvthread.start()


# 数据分析
import numpy as np


def dealdata():
    # arr = np.array([1, 2, 3, 4, 5])
    # print(type(arr), arr)
    # print(arr.dtype)
    # print(arr.shape)
    # print(arr.size)
    # arr = np.array([1, 2, 3, "4", '567'])
    # print(arr, arr.dtype)
    # arr = np.zeros(10)
    # arr = np.zeros([2,3])
    # arr1 = np.array([[1,2],[3,4]])
    # arr2 = np.zeros_like(arr1)
    # arr3 = np.zeros(arr1.shape)
    # print(arr1,arr.dtype)
    # print(arr2,arr.dtype)
    # print(arr3,arr.dtype)
    arr = np.empty(5)
    print(arr, arr.dtype)
    arr = np.empty([5, 6])
    print(arr, arr.dtype)
    arr = np.arange(0, 1, 0.2)
    print(arr)
    arr = np.eye(4)
    print(arr)
    arr = np.identity(4)
    print(arr, arr.size, arr.dtype, arr.itemsize, arr.max())
    arr = np.array([[1, 2, 3], [3, 4, 5]])
    print(arr)
    arr2 = np.array(arr, dtype='float')
    arr3 = arr2.astype('str')
    print(arr3, arr3.dtype)
    arr4 = arr2.astype('string_')
    print(arr4, arr4.dtype)
    arr5 = np.array([1.1, 2.2, 3.3])
    print(arr5.astype(np.int))
    arr6 = np.array(['1.1', '2.2'])
    print(arr6.astype(np.float))
    # print(arr6.astype(np.complex))
    # arr7 = np.array([[1,2]],[3,4,5])
    # print(arr7,arr7.dtype)
    arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    print(arr1)
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    print(np.concatenate([arr1, arr2], axis=1))
    print(np.concatenate([arr1, arr2], axis=0))
    print(np.hstack([arr1, arr2]))
    arr1 = np.arange(12).reshape((3, 4))
    print(arr1)
    print(np.split(arr1, [2, 3], axis=1))
    print(np.split(arr1, [2], axis=0))
    arr1 = np.arange(12).reshape((3, 4))
    print(arr1.transpose(1, 0))
    print(arr1.T)
    print(np.random.rand(1))
    print(np.random.rand(1)[0])


from pandas import Series, DataFrame


def pdtest():
    dictVar = {'python': 100, "java": 99}
    obj = Series(dictVar, index=['python', 'java'])
    obj.index.name = 'P1'

    data = {
        'name': ['张三', '李四', '王五'],
        'sex': ['男', '男', '女']
    }
    df = DataFrame(data, index=['a', 'b', 'c'], columns=['name', 'sex'])
    print(df)

    df = DataFrame([[1, 2], [3, 4]], index=['r1', 'r2'], columns=['c1', 'c2'])
    print(df)

    s1 = Series([1, 2, 3], index=['a', 'b', 'c'])
    s2 = Series([4, 5, 6], index=['a', 'b', 'c'])
    data = [s1, s2]
    df = DataFrame(data)
    print(df)
    data = {
        's1': s1,
        's2': s2
    }
    print(DataFrame(data))

    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(DataFrame(arr, columns=['a', 'b', 'c']))

    obj = Series([1, 2, 3])
    print(obj.index)
    obj = Series([1, 2, 3], index=['a', 'b', 'c'])
    print(obj.index)

    data = {
        'age': {'张三': 20, "李四": 30},
        'sex': {'张三': 'f', '李四': 'm'}
    }
    df = DataFrame(data)
    print(df.index.values)
    print(df.columns.values)

    df = DataFrame([[1, 2, 3], [4, 5, 6]], index=['r1', 'r2'], columns=['c1', 'c2', 'c3'])
    print(df)
    df2 = df.reindex(columns=['c2', 'c1', 'c3'])
    print(df2)
    df3 = df2.reindex(columns=['c2', 'c1', 'c3', 'c4'], fill_value=0)
    print(df3)

    data = {
        'name':['张三','李四','王五','赵六'],
        'score': [77,89,76,90]
    }
    df = DataFrame(data)
    df2 = df.sort_values(by='score')
    df3 = df2.reset_index()
    df4 = df2.reset_index(drop=True)
    print(df4)

    obj = Series([1,2,3,4],index=['a','b','c','d'])
    print(obj)
    print(obj[1])
    print(obj['c'])
    print(obj[['a','c']])
    print(obj[0:2])
    print(obj['a':'c'])

if __name__ == "__main__":
    pdtest()
