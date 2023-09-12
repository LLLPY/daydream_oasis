# *_* coding:utf8 *_*
import csv
import os
import pymysql

# 将所有文件导入数据库
basePath = '\\Users\LLL\Desktop\python\python基础(演练)'

def file_name(file_dir):
    fileNum = 0
    fileList = []
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        for file in files:
            if file.endswith('.py'):
                if 'lll' in file:
                    abPath = root + '\\' + file
                    fileList.append(abPath)
                    fileNum += 1
        # print('*'*50)
        # break
    return fileList

#返回文件列表
def returnFileList():
    fileList = file_name(basePath)
    dataList = []
    for file in fileList[:-2]:
        if 'build' not in file and 'venv' not in file and 'ex_html' not in file:
            filePartList = file.split('\\')
            # 文件的类别
            classOne = filePartList[-2:][0]
            # 文件名
            fileName = filePartList[-2:][1]
            # 文件的路径
            filePath = file
            dataList.append((classOne, fileName, filePath))
    return dataList


#将数据导入数据库
def importToDBS(dataList):

    # 创建来接对象
    con = pymysql.connect(host='121.199.23.213', port=3306, user='LLL', password='LVLL0318', database='daydream_oasis')

    # 创建游标对象
    cur = con.cursor()
    # 编写插入的sql语句
    sql = '''insert into 博客 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

    try:
        # 执行插入的sql语句
        cur.executemany(sql, dataList)
        # 事务提交
        con.commit()
        print('数据插入成功!')
    except Exception as e:
        print(e)
        # 书事务回滚
        con.rollback()
        print('数据插入失败!')
    finally:
        con.close()

#返回读取到的文件内容
def returnFileContent(filePath):
    con='内容不见了~'
    try:
        with open(filePath, 'r', encoding='utf8') as f:
            con = f.read()
    except:
        pass
    return con

#执行导入数据库的操作 每次执行后需要重新导入分类表的数据
def doImportToDBS():
    classSet=set(['js学习','html学习','css学习','GUI编程', '正则表达式', 'Web开发编程', 'flask基础', '数据库编程', '数据挖掘', '网络编程(书)', 'matplotlib学习', '并发编程', 'os模块的学习', '文件', '数据结构', '猫眼', '语法进阶', '算法', '爬虫学习', '网络编程', 'pyecharts学习', 'numpy学习', '模块', '异常', '面向对象', 'python基础', '函数', '面向对象的特性', '高级变量类型', '高阶函数',  '测试', '感想', '总结', '数学建模', '大数据'])
    classDic = {'pyecharts学习': 1, '面向对象的特性': 2, '语法进阶': 3, 'os模块的学习': 4, 'flask基础': 5, '异常': 6, 'matplotlib学习': 7,
                '高级变量类型': 8, '总结': 9, '并发编程': 10, '数学建模': 11, '爬虫学习': 12, '数据结构': 13, '数据库编程': 14, 'python基础': 15,
                'css学习': 16, '数据挖掘': 17, '测试': 18, '模块': 19, '猫眼': 20, '感想': 21, '函数': 22, 'Web开发编程': 23, '大数据': 24,
                'js学习': 25, 'html学习': 26, 'numpy学习': 27, '算法': 28, '网络编程': 29, '网络编程(书)': 30, '文件': 31, '高阶函数': 32,
                '正则表达式': 33, '面向对象': 34, 'GUI编程': 35}

    #将文件的分类写入文件
    with open('fileClass.csv','w',encoding='utf8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['id','标题','创建时间'])
        # n=1
        for i in classSet:
            writer.writerow({'id':classDic[i],'标题':i,'创建时间':'2021-5-29 14:17:26'})
            # classDic[i]=n
            # n += 1

    for file in returnFileList():
        class_ = file[0]
        for i in range(10):
            class_ = class_.replace(f'{i}', '').replace('_', '')

        fileName = file[1]
        filePath = file[2]
        # print(f'文件的类别:{class_},文件名:{fileName},文件路径:{filePath}')
        classSet.add(class_)
    dataList=[]
    N=1
    for i in returnFileList():
        #标题 标签
        class_ = i[0]
        for k in range(10):
            class_ = class_.replace(f'{k}', '').replace('_', '')
        content=returnFileContent(i[2]).replace(' ','&nbsp;').replace('\n','<br>')
        classId=classDic[class_]
        data=(N,i[1],class_,content[:200],content,0,0,'2021-5-29 14:17:26','2021-5-29 14:17:26','1','1',classId)
        N+=1
        dataList.append(data)
    importToDBS(dataList)

if __name__ == '__main__':
    doImportToDBS()






