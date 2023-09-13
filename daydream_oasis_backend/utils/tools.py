import base64
import os
from re import search, findall
from datetime import datetime
from time import time, localtime, strftime, strptime, mktime
import calendar
import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar, Pie
from pyecharts.globals import ThemeType
import heapq
from os.path import join
import hashlib
from typing import Union
import orjson


# 时间戳转换成日期


def timestamp_to_date(timestamp):
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = localtime(timestamp)  # 30/12/2020 21:05:19
    otherStyleTime = strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


# 把时间转换成秒数
def str_to_timestamp(str_time=None, format='%Y-%m-%d %H:%M:%S'):
    if str_time:
        time_tuple = strptime(str_time, format)  # 把格式化好的时间转换成元祖
        result = mktime(time_tuple)  # 把时间元祖转换成时间戳
        return int(result)
    return int(time())


# base64数据转换成图片 返回图片保存的路径
def base64ToPicture(dataList, title, path='static/image/imgInBlog'):
    # 去掉文件名中的特殊符号
    for i in '/ \:*"<>|?.':
        title = title.replace(i, '')
    title = title + str(time())

    date = timestamp_to_date(time()).split(' ')[0].replace('-', '')
    fileNameList = []
    for data in dataList:
        imgdata = base64.b64decode(data)
        fileName = title + str(dataList.index(data)) + '.png'
        path = f'{path}/{date}/'
        if not os.path.exists(path):
            os.mkdir(path)
        f = open(path + fileName, 'wb')
        f.write(imgdata)
        f.close()
        fileNameList.append(f'{path}' + fileName)
    return fileNameList


# 返回替换后的content
def returnNewContent(content, title):
    imgDataList = findall(r'<img src="data:image/png;base64,(.*?)alt="">', content)  # 取消贪婪模式
    imgPathList = base64ToPicture(imgDataList, title)  # 把博客中的base64转成图片保存到本地
    for i in imgPathList:  # 把博客内容中的图片数据改成对应的图片路径
        content = content.replace(rf'<img src="data:image/png;base64,{imgDataList[imgPathList.index(i)]}alt="">',
                                  f'<img src="http://www.lll.plus/{i}">', 1)  # 每次只替换一次
    return content


# 返回某一年某一个月的所有日期
def getMothDate(year, month):
    """
    返回某年某月的所有日期
    :param year:
    :param month:
    :return:
    """
    date_list = []
    for i in range(calendar.monthrange(year, month)[1] + 1)[1:]:
        str1 = str("%02d" % i)
        date_list.append(str1)
    return date_list


# 可视化
# 记录 登录页面 注册页面 错误页面 学习星球页面 快乐星球页面 博客编辑页面 搜索功能 个人中心页面 首页 的请求
def draw(xList, dataDic, timeList, filename='demo.html', series_name='年访问量'):
    total_data = {}
    titleList = [
        '首页页面',
        '学习星球',
        '快乐星球',
        '搜索功能',
        '个人中心',
        '博客编辑',
        '登录页面',
        '注册页面',
        '错误页面',
    ]
    keyList = [
        'dataIndex',
        'dataLearning',
        'dataPlaying',
        'dataSearch',
        'dataCenter',
        'dataModify',
        'dataLogin',
        'dataRegister',
        'dataError',
    ]

    data_login = dataDic[0]  # 登录页面
    data_register = dataDic[1]  # 注册页面
    data_error = dataDic[2]  # 错误页面
    data_learning = dataDic[3]  # 学习星球页面
    data_playing = dataDic[4]  # 快乐星球页面
    data_modify = dataDic[5]  # 博客编辑页面
    data_search = dataDic[6]  # 搜索功能
    data_center = dataDic[7]  # 个人中心页面
    data_index = dataDic[8]  # 首页页面

    def format_data(data: dict) -> dict:
        for year in timeList:
            max_data, sum_data = 0, 0
            temp = data[year]
            max_data = max(temp)
            # print(f'{len(temp)}:{temp}\n{len(xList)}:{xList}')

            while len(temp) > len(xList):
                last_day = 'day' + str(int(xList[-1].replace('day', '')) + 1)
                xList.append(last_day)

            for i in range(len(temp)):
                sum_data += temp[i]
                data[year][i] = {"name": xList[i], "value": temp[i]}
            data[str(year) + "max"] = int(max_data / 100) * 100
            data[str(year) + "sum"] = sum_data

        return data

    total_data['dataLogin'] = format_data(data=data_login)  # 登录
    total_data['dataRegister'] = format_data(data=data_register)  # 注册
    total_data['dataError'] = format_data(data=data_error)  # 错误
    total_data['dataLearning'] = format_data(data=data_learning)  # 学习
    total_data['dataPlaying'] = format_data(data=data_playing)  # 快乐
    total_data['dataModify'] = format_data(data=data_modify)  # 编辑
    total_data['dataSearch'] = format_data(data=data_search)  # 搜索
    total_data['dataCenter'] = format_data(data=data_center)  # 中心
    total_data['dataIndex'] = format_data(data=data_index)  # 首页

    #####################################################################################
    # 2012 - 2021 年的数据
    def get_year_overlap_chart(year: int) -> Bar:
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
                .add_xaxis(xaxis_data=xList)
                .add_yaxis(
                titleList[0],  # 首页
                total_data[keyList[0]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                titleList[1],  # 学习星球
                total_data[keyList[1]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                titleList[2],  # 快乐星球
                total_data[keyList[2]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                titleList[3],  # 搜索功能
                total_data[keyList[3]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                titleList[4],  # 个人中心
                total_data[keyList[4]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                titleList[5],  # 博客编辑
                total_data[keyList[5]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )

                .add_yaxis(
                titleList[6],  # 登录页面
                total_data[keyList[6]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                titleList[7],  # 注册页面
                total_data[keyList[7]][year],
                label_opts=opts.LabelOpts(is_show=False),
            ).add_yaxis(
                titleList[8],  # 错误页面
                total_data[keyList[8]][year],
                label_opts=opts.LabelOpts(is_show=False),
            )

                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="{}各页面访问量统计".format(year), subtitle="数据来自后台统计"
                ),
                toolbox_opts=opts.ToolboxOpts(is_show=True),  # 添加toolbox选项,toolbox中提供了一些对图片的操作工具
                tooltip_opts=opts.TooltipOpts(is_show=True, trigger="axis", axis_pointer_type="shadow"),
                datazoom_opts=opts.DataZoomOpts(type_="inside"),
                legend_opts=opts.LegendOpts(pos_top="10%"),
            )
        )
        pie = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
                .add(
                series_name=series_name,
                data_pair=[
                    [titleList[0], total_data[keyList[0]]["{}sum".format(year)]],
                    [titleList[1], total_data[keyList[1]]["{}sum".format(year)]],
                    [titleList[2], total_data[keyList[2]]["{}sum".format(year)]],
                    [titleList[3], total_data[keyList[3]]["{}sum".format(year)]],
                    [titleList[4], total_data[keyList[4]]["{}sum".format(year)]],
                    [titleList[5], total_data[keyList[5]]["{}sum".format(year)]],
                    [titleList[6], total_data[keyList[6]]["{}sum".format(year)]],
                    [titleList[7], total_data[keyList[7]]["{}sum".format(year)]],
                    [titleList[8], total_data[keyList[8]]["{}sum".format(year)]],

                ],
                center=["75%", "35%"],
                radius="28%",
            )
                .set_series_opts(tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"))
        )
        return bar.overlap(pie)

    # 生成时间轴的图
    timeline = Timeline(init_opts=opts.InitOpts(width="100%", height="80%"))
    for time in timeList:
        timeline.add(get_year_overlap_chart(year=time), time_point=str(time))
    # 1.0.0 版本的 add_schema 暂时没有补上 return self 所以只能这么写着
    timeline.add_schema(is_auto_play=True, play_interval=1000)
    return timeline.render(filename)


# 后台数据的统计
def statisticData(request_table_model, whichOne=2):
    nowTime = datetime.now()
    nowyear, nowmonth = nowTime.year, nowTime.month
    month_list = [
        '一月',
        '二月',
        '三月',
        '四月',
        '五月',
        '六月',
        '七月',
        '八月',
        '九月',
        '十月',
        '十一月',
        '十二月'
    ]  # 横坐标的值
    year_list = [year for year in range(nowyear - 9, nowyear + 1)]  # 从现在开始前退10年
    x_list = ['day' + i for i in getMothDate(nowyear, nowmonth)]  # x的坐标改为日期
    requestObjs = request_table_model.get_all()

    if whichOne == 2:
        data_login = {}  # 登录页面  数据里面的时间key要与timeline的同步
        data_register = {}  # 注册页面
        data_error = {}  # 错误页面
        data_learning = {}  # 学习星球页面
        data_playing = {}  # 快乐星球页面
        data_modify = {}  # 博客编辑页面
        data_search = {}  # 搜索功能
        data_center = {}  # 个人中心页面
        data_index = {}  # 首页页面
        for year in range(nowyear - 9, nowyear + 1):
            data_login[year] = [0 for i in range(12)]  # {2021:[0,0,0,0,0,0,0,0,0,0]}
            data_register[year] = [0 for i in range(12)]
            data_error[year] = [0 for i in range(12)]
            data_learning[year] = [0 for i in range(12)]
            data_playing[year] = [0 for i in range(12)]
            data_modify[year] = [0 for i in range(12)]
            data_search[year] = [0 for i in range(12)]
            data_center[year] = [0 for i in range(12)]
            data_index[year] = [0 for i in range(12)]

        for requestObj in requestObjs:
            rPath = requestObj.requestPath
            ryear = requestObj.requestTime.year
            rmonth = requestObj.requestTime.month
            if rPath == '/':
                data_index[ryear][rmonth - 1] += 1  # {2021:[1,0,0,0,0,0,0,0,0,0,0,0,0]}

            elif search(r'login', rPath):
                data_login[ryear][rmonth - 1] += 1

            elif search(r'register', rPath):
                data_register[ryear][rmonth - 1] += 1

            elif search(r'error', rPath):
                data_error[ryear][rmonth - 1] += 1

            elif search(r'learningPlanet', rPath):
                data_learning[ryear][rmonth - 1] += 1

            elif search(r'playingPlanet', rPath):
                data_playing[ryear][rmonth - 1] += 1

            elif search(r'modifyBlog', rPath):
                data_modify[ryear][rmonth - 1] += 1

            elif search(r'search', rPath):
                data_search[ryear][rmonth - 1] += 1

            elif search(r'personalCenter', rPath):
                data_center[ryear][rmonth - 1] += 1

        dataDic = [
            data_login,
            data_register,
            data_error,
            data_learning,
            data_playing,
            data_modify,
            data_search,
            data_center,
            data_index
        ]
        draw(xList=month_list, dataDic=dataDic, timeList=year_list, filename=join('templates', 'demo2.html'),
             series_name='年访问量')

    else:
        data_login2 = {}  # 登录页面  数据里面的时间key要与timeline的同步
        data_register2 = {}  # 注册页面
        data_error2 = {}  # 错误页面
        data_learning2 = {}  # 学习星球页面
        data_playing2 = {}  # 快乐星球页面
        data_modify2 = {}  # 博客编辑页面
        data_search2 = {}  # 搜索功能
        data_center2 = {}  # 个人中心页面
        data_index2 = {}  # 首页页面
        for month in month_list:
            cur_month = month_list.index(month) + 1
            cur_day_list = getMothDate(nowyear, cur_month)  #

            data_login2[month] = [0 for i in cur_day_list]  # {'十一月':[0,0,0,0,0...0]}
            data_register2[month] = [0 for i in cur_day_list]
            data_error2[month] = [0 for i in cur_day_list]
            data_learning2[month] = [0 for i in cur_day_list]
            data_playing2[month] = [0 for i in cur_day_list]
            data_modify2[month] = [0 for i in cur_day_list]
            data_search2[month] = [0 for i in cur_day_list]
            data_center2[month] = [0 for i in cur_day_list]
            data_index2[month] = [0 for i in cur_day_list]

        for requestObj in requestObjs:
            rPath = requestObj.path
            ryear = requestObj.requestTime.year
            rmonth = requestObj.requestTime.month
            rday = requestObj.requestTime.day

            if str(ryear) == str(nowyear):  # 统计当年的数据
                if search(r'learningPlanet', rPath):
                    data_learning2[month_list[rmonth - 1]][rday - 1] += 1
                elif rPath == '/':
                    data_index2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'login', rPath):
                    data_login2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'register', rPath):
                    data_register2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'error', rPath):
                    data_error2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'playingPlanet', rPath):
                    data_playing2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'modifyBlog', rPath):
                    data_modify2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'personalCenter', rPath):
                    data_center2[month_list[rmonth - 1]][rday - 1] += 1
                elif search(r'search', rPath):
                    data_search2[month_list[rmonth - 1]][rday - 1] += 1

        # 月数据
        dataDic2 = [
            data_login2,
            data_register2,
            data_error2,
            data_learning2,
            data_playing2,
            data_modify2,
            data_search2,
            data_center2,
            data_index2
        ]
        draw(xList=x_list, dataDic=dataDic2, timeList=month_list, filename=join('templates', 'demo1.html'),
             series_name='月访问量')


# 获取ip相关的信息,
def get_ip_info(ip: str):
    # r = get(url=f'http://ip-api.com/json/{ip}?lang=zh-CN')
    country, region, city, latitude, longitude, timezone, isp = 'None', 'None', 'None', 'None', 'None', 'None', 'None'
    # try:
    #     r_json = r.json()
    #     country = r_json.get('country', 'None')
    #     region = r_json.get('regionName', 'None')
    #     city = r_json.get('city', 'None')
    #     latitude = r_json.get('latitude', 'None')
    #     longitude = r_json.get('longitude', 'None')
    #     timezone = r_json.get('timezone', 'None')
    #     isp = r_json.get('isp', 'None')
    # except:
    #     pass
    return (country, region, city, latitude, longitude, timezone, isp)

# def get_address(ip):
#     api_url = f'https://freeapi.ipip.net/{ip}'
#     try:
#         # 先从缓存中获取，如果没有就再请求接口
#         location = cache.get(f'{ip}-address', None)
#         if not location:
#             res = requests.get(api_url)
#             location = res.json()[:3]
#             cache.set(f'{ip}-address', location, 60 *
#                       60 * 24 * 7)  # 假设一个用户7天之内不会更换位置
#         return location
#     except Exception as e:
#         return ['', '', '']
# 信息摘要
def md5(content: Union[str, bytes, dict]):

    # 字符串
    if isinstance(content, str):
        content = content.encode('utf8')

    # 字典
    elif isinstance(content, dict):
        content = orjson.dumps(sorted(content.items()))

    md = hashlib.sha256(content)
    return md.hexdigest()


if __name__ == '__main__':
    con = {'a': 1}

    res = md5(con)
    print(res)
