
import os
import time
import pygame
import psutil
import pymysql
import requests
import win32gui
import win32con
import win32api
import subprocess
from datetime import date
from aip import AipSpeech


# 当天的日期
today = date.today()
todate = today.strftime("%Y-%m-%d")


# 高德地图API的Key
KEY = '33faf9a1558a748f1831321710b15742'

# 查询城市的名称
city = '梅州'
# 构造API请求
url = "https://restapi.amap.com/v3/weather/weatherInfo?city={}&key={}&extensions=all".format(city, KEY)
url1 = "https://restapi.amap.com/v3/weather/weatherInfo?city={}&key={}&extensions=base".format(city, KEY)

# 百度API数据
APP_ID = '34381407'
API_KEY = 'DwHRrqMlk66o7lHNwBj9jlRQ'
SECRET_KEY = 'fEZHsUI4elsj5IYdH27RPH7ZQmALF2ri'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 关闭正在运行的酷狗音乐
def stop_music():
    os.system('taskkill /IM KuGou.exe /F')


def sj_music():
    # 打开Win10程序
    subprocess.Popen(['D:\\Program Files (x86)\\KuGou\\KGMusic\\KuGou.exe'])
    # 等待应用程序启动
    while True:
        window = win32gui.FindWindow(None, '酷狗音乐')
        if window != 0:
            break
        time.sleep(0.1)
    # 最小化窗口
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)


# 日程表数据检查
def sc_check():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行 SQL 查询
    sql = "select count(1) xssc from `xt_schedule_v0.0.1` where `xs_date` = CURDATE() and `xs_schedule` = '未完成'"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xsin = results[0]
    if xsin == 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '今天的日程已全部完成，先生，就是我崇拜的偶像。'
    elif xsin > 7:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，日程表数据可能有异常，需要排查下'
    else:
        sql = "select `xs_item` from `xt_schedule_v0.0.1` where `xs_date` = CURDATE() and `xs_schedule` = '未完成'"
        cursor.execute(sql)
        # 获取查询结果
        results = cursor.fetchall()
        combined = (row[0] for row in results)
        merge = "，".join(str(v) for v in combined)
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return f"先生，未完成的项目有{merge}，请选择一项日程更新到数据库"


# 日程书籍
def sc_book():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查
    sql = "select count(1) xt_chack from `xt_schedule_v0.0.1` where xs_date = curdate() and xs_item = '书籍' and xs_schedule = '已完成';"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xt_check = results[0]
    if xt_check != 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，今天的日程书籍已经记录过了'
    else:
        # 执行 SQL 更新
        sql = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_item` = '书籍' and xs_date = curdate();"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '书中自有黄金屋，书中自有颜如玉。先生，日程书籍已记录'


# 日程散步
def sc_walk():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查
    sql = "select count(1) xt_chack from `xt_schedule_v0.0.1` where xs_date = curdate() and xs_item = '散步' and xs_schedule = '已完成';"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xt_check = results[0]
    if xt_check != 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，今天的日程散步已经记录过了'
    else:
        # 执行 SQL 更新
        sql = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_item` = '散步' and xs_date = curdate();"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '闲庭信步看庭前花开花落，去留无意望天上云卷云舒。先生，日程散步已记录'


# 日程新闻
def sc_news():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查
    sql = "select count(1) xt_chack from `xt_schedule_v0.0.1` where xs_date = curdate() and xs_item = '新闻' and xs_schedule = '已完成';"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xt_check = results[0]
    if xt_check != 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，今天的日程新闻已经记录过了'
    else:
        # 执行 SQL 更新
        sql = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_item` = '新闻' and xs_date = curdate();"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '秀才不出门，全知天下事。先生，日程新闻已记录'


# 日程财务
def sc_finance():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查
    sql = "select count(1) xt_chack from `xt_schedule_v0.0.1` where xs_date = curdate() and xs_item = '财务' and xs_schedule = '已完成';"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xt_check = results[0]
    if xt_check != 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，今天的日程财务已经记录过了'
    else:
        # 执行 SQL 更新
        sql = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_item` = '财务' and xs_date = curdate();"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '国富民强 开元盛世。先生，日程财务已记录'


# 日程泡脚
def sc_soak():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查
    sql = "select count(1) xt_chack from `xt_schedule_v0.0.1` where xs_date = curdate() and xs_item = '泡脚' and xs_schedule = '已完成';"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xt_check = results[0]
    if xt_check != 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，今天的日程泡脚已经记录过了'
    else:
        # 执行 SQL 更新
        sql = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_item` = '泡脚' and xs_date = curdate();"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '休养生息，涵煦于百年之深也。先生，日程泡脚已记录'


# 日程健身
def sc_fitness():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查
    sql = "select count(1) xt_chack from `xt_schedule_v0.0.1` where xs_date = curdate() and xs_item = '健身' and xs_schedule = '已完成';"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xt_check = results[0]
    if xt_check != 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，今天的日程健身已经记录过了'
    else:
        # 执行 SQL 更新
        sql = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_item` = '健身' and xs_date = curdate();"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '野蛮其体魄，文明其精神。先生，日程健身已记录'


# 日程表数据
def sddata():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 检查库表数据
    sql = "select count(1) data from `xt_schedule_v0.0.1` where `xs_date` = CURDATE()"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    mysqldate = results[0]
    if mysqldate == 7:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '日程已启动，先生。'
    elif mysqldate == 0:
        # 插入数据
        sql = "INSERT INTO `xt_schedule_v0.0.1` (`xs_date`, `xs_module`, `xs_item`, `xs_priority`, `xs_instructions`, `xs_executor`, `xs_schedule`, `xs_remark`) VALUES \
        (CURDATE(), '数据', '同步', '高级', '坚果云数据同步', '丞相', '未完成', ''),\
        (CURDATE(), '修身', '书籍', '中级', '渤海小吏百战系列看书一小时', '丞相', '未完成', ''),\
        (CURDATE(), '修身', '散步', '中级', '晚饭后散步，室内停电一小时', '丞相', '未完成', ''),\
        (CURDATE(), '修身', '新闻', '中级', 'CCTV新闻联播', '丞相', '未完成', ''),\
        (CURDATE(), '财务', '财务', '高级', '每日花销记录', '丞相', '未完成', ''),\
        (CURDATE(), '健康', '泡脚', '高级', '姜艾叶泡脚', '丞相', '未完成', ''),\
        (CURDATE(), '健康', '健身', '高级', '哑铃深蹲20个为1组，安排5组', '丞相', '未完成', '');"
        cursor.execute(sql)
        # 提交更改
        db.commit()
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '日程已启动，先生。'
    else:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '日程表数据可能有差异，需要排查下，先生'


# 查询日程信息
def xt_in():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行 SQL 查询
    sql = "select count(1) xssc from `xt_schedule_v0.0.1` where `xs_date` = CURDATE() and `xs_schedule` = '未完成'"
    cursor.execute(sql)
    # 获取查询结果
    results = cursor.fetchone()
    # 获取结果中的数据值并赋给变量
    xsin = results[0]
    if xsin == 0:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '今天的日程已完成，先生就是我崇拜的偶像！'
    elif xsin > 0:
        sql = "select `xs_instructions` from `xt_schedule_v0.0.1` where `xs_date` = CURDATE() and `xs_schedule` = '未完成'"
        cursor.execute(sql)
        # 获取查询结果
        results = cursor.fetchall()
        combined = (row[0] for row in results)
        merge = "，".join(str(v) for v in combined)
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return f"先生，今天未完成的日程有{merge}"
    else:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()
        return '先生，日程数据表可能有异常需要排查下'


# 获取当下的时间
def nowdate():
    # 时间信息
    nowday = today.strftime("%Y年%m月%d日")
    nowtime = time.strftime("%H时%M分%S秒", time.localtime())
    return f"现在的时间是{nowday}{nowtime}"


# 获取天气信息
def weather():
    # 获取API响应，预报天气和实况天气
    response = requests.get(url).json()
    response1 = requests.get(url1).json()
    # 提取所需的预报天气信息并输出
    casts = response["forecasts"][0]["casts"]
    today_cast = [cast for cast in casts if cast['date'] == todate][0]
    # 赋予预报天气的值
    td_date = today_cast['date']
    week = today_cast['week']
    day_weather = today_cast['dayweather']
    night_weather = today_cast['nightweather']
    temp_min = today_cast['nighttemp']
    temp_max = today_cast['daytemp']
    # 赋予实况天气的值
    rtweather = response1["lives"][0]["weather"]
    winddir = response1["lives"][0]["winddirection"]
    windpower = response1["lives"][0]["windpower"]
    humidity = response1["lives"][0]["humidity"]
    return f"{td_date}，星期{week}的气温是，{temp_min}到{temp_max}摄氏度，{day_weather}转{night_weather}，目前天气是{rtweather}，\
    风向为{winddir}风, 风向级别{windpower}，空气湿度是{humidity}"


# 播放声音
def play():
    # 生成音频
    os.system('edge-tts --voice zh-CN-YunyangNeural --text "{}" --write-media "writ.mp3"'.format(text))
    # 播放声音
    pygame.mixer.init()
    pygame.mixer.music.load('E:/python/XiaoMu/01-xiaotian/writ.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.unload()


# 程序执行
if __name__ == "__main__":
    # 打开政务
    # win32api.ShellExecute(0, 'open', r"E:\02-二木生活区\武侯府内政v0.0.1.xlsx", '', '', 1)
    # win32api.ShellExecute(0, 'open', r"E:\01-二木工作室\武侯府军事v0.0.1.xlsx", '', '', 1)
    # win32api.ShellExecute(0, 'open', r"E:\02-二木生活区\05-财务\2023年度\202306财务账单v0.0.2.xlsx", '', '', 1)
    # 日程表数据
    text = sddata()
    play()
    # 调用语音回应
    value = 0
    order = 0
    while True:  # 打开文件读取最后5个字符
        with open('output.txt', 'r') as f:
            contents = f.read()
        if '小天' in contents and value == 0:  # 小天的回应条件
            text = '在的，先生。'
            play()
            value = 1
            order = 1
        if '小天' not in contents and contents != '':
            value = 0
        if order == 1 and '实现帮助' in contents:
            text = '可以帮助先生'\
                   '查询数据同步，'\
                   '查询天气，'\
                   '查询时间，'\
                   '查询日常，'\
                   '更新日常'
            play()
            order = 0
        if order == 1 and '查询数据同步' in contents:
            for proc in psutil.process_iter():
                try:
                    if proc.name() == "NutstoreClient.exe":
                        text = '数据，已开启同步，先生'
                        play()
                        # 打开数据库连接
                        db1 = pymysql.connect(host="192.168.179.130", user="root", password="root", database="xiaotian")
                        # 使用 cursor() 方法创建一个游标对象 cursor
                        cursor1 = db1.cursor()
                        sql1 = "select xs_schedule from `xt_schedule_v0.0.1` where `xs_date` = CURDATE() and `xs_instructions` = '坚果云数据同步'"
                        cursor1.execute(sql1)
                        # 获取查询结果
                        results1 = cursor1.fetchone()
                        # 获取结果中的数据值并赋给变量
                        nutstoreclient = results1[0]
                        # 输出变量的值
                        if nutstoreclient == '未完成':
                            # 执行 SQL 更新
                            sql2 = "UPDATE `xt_schedule_v0.0.1` SET `xs_schedule` = '已完成' where `xs_date` = CURDATE() and `xs_instructions` = '坚果云数据同步'"
                            cursor1.execute(sql2)
                            # 提交更改
                            db1.commit()
                        # 关闭游标和数据库连接
                        cursor1.close()
                        db1.close()
                        break
                except ZeroDivisionError:
                    pass
            else:
                text = '数据，未开启同步，先生'
                play()
            order = 0
        if order == 1 and '查询日常' in contents:
            text = xt_in()
            play()
            order = 0
        if order == 1 and '更新日常' in contents:
            text = sc_check()
            play()
            if '未完成的项目' in text:
                time.sleep(3)
                while True:
                    # 获取语音转文本
                    with open('output.txt', 'r') as f:
                        contents = f.read()
                    if '书籍' in contents:
                        text = sc_book()
                        play()
                        break
                    elif '散步' in contents:
                        text = sc_walk()
                        play()
                        break
                    elif '新闻' in contents:
                        text = sc_news()
                        play()
                        break
                    elif '财务' in contents:
                        text = sc_finance()
                        play()
                        break
                    elif '泡脚' in contents:
                        text = sc_soak()
                        play()
                        break
                    elif '健身' in contents:
                        text = sc_fitness()
                        play()
                        break
                    elif '取消' in contents:
                        text = '读书不觉已春深，一寸光阴一寸金。先生，已取消录入'
                        play()
                        break
                    else:
                        text = sc_check()
                        play()
                        time.sleep(3)
            order = 0
        if order == 1 and '查询天气' in contents:
            text = weather()
            play()
            order = 0
        if order == 1 and '查询时间' in contents:
            text = nowdate()
            play()
            order = 0
        if order == 1 and '播放音乐' in contents:
            sj_music()
            order = 0
        if order == 1 and '关闭音乐' in contents:
            stop_music()
            text = '已关闭音乐，先生'
            play()
            order = 0
        # 当下的时间
        redate = time.strftime("%H:%M:%S", time.localtime())
        if redate == '07:00:00':
            text = '一年之计在于春，一日之计在于晨。一家之计在于和，一生之计在于勤。早安，先生。'
            play()
        if redate == '07:30:00':
            text = '行灶朝香炊早饭，小园春暖掇新蔬。早餐时间到了，先生！'
            play()
        if redate == '09:00:00':
            text = '千江有水千江月，万里无云万里天。请饮用水，先生！'
            play()
        if redate == '11:00:00':
            text = '天壤之间，水居其多。请饮用水，先生！'
            play()
        if redate == '12:00:00':
            text = '午餐何所有，鱼肉一两味。午餐时间到了，先生！'
            play()
        if redate == '14:00:00':
            text = '青山看不厌，流水趣何长。请饮用水，先生！'
            play()
        if redate == '16:00:00':
            text = '一水护田将绿绕，两山排闼送青来。请饮用水，先生！'
            play()
        if redate == '18:00:00':
            text = '小饼如嚼月，中有酥与贻。晚餐时间到了，先生！'
            play()
        if redate == '19:00:00':
            text = '古之欲明明德于天下者，先治其国；\
            欲治其国者，先齐其家；欲齐其家者，先修其身；\
            欲修其身者，先正其心；欲正其心者，先诚其意；\
            欲诚其意者，先致其知，致知在格物。\
            物格而后知至，知至而后意诚，意诚而后心正，心正而后身修，身修而后家齐，家齐而后国治，国治而后天下平。' \
            '先生，新闻联播开始了！'
            play()
        if redate == '20:00:00':
            text = '南湖秋水夜无烟，耐可乘流直上天。请饮用水，先生！'
            play()
        if redate == '21:00:00':
            text = '雪沫乳花浮午盏，蓼茸蒿笋试春盘。人间有味是清欢。宵夜时间到了，先生！'
            play()
        if redate == '22:00:00':
            text = f"诗书勤乃有，不勤腹空虚。{xt_in()}"
            play()
        if redate == '22:30:00':
            text = '先生，请检查以下设施' \
                   '浴室的门窗和排气扇,后门的门窗是否已经打开'\
                   '循环扇的风向是否转向后门外启动，且风力为20档'\
                   '加湿器是否强度三分之二左右启动，且水槽中的水有一半以上。'
            play()
        if redate == '23:00:00':
            text = '何处花香入夜清？石林茅屋隔溪声。先生，晚安。'
            play()
        if redate == '00:00:00':
            # 日程表数据
            text = sddata()
            play()
