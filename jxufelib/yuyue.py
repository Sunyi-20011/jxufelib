# -*- coding: UTF-8 -*-
# @Time : 2022/9/19
# @Author : Sunyi
# @File : yuyue.py
# @Detail : jxufelib
import random
import time

import requests as rq
import execjs
import datetime
import json
import sys

# 忽略requests证书警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning

time_ends = [0, "12:00", "17:00", "23:00"]
nums = [0, "上午", "下午", "晚上"]
User_Agents = [
    'Mozilla/5.0 (Linux; Android 11; IN2010 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/7693 MicroMessenger/8.0.18.2060(0x28001237) Process/toolsmp WeChat/arm32 Weixin NetType/4G Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/3590 MicroMessenger/8.0.27.2220(0x28001B36) WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 8.1.0; MI 5X Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200801 Mobile Safari/537.36 MMWEBID/9633 MicroMessenger/7.0.18.1740(0x2700123B) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001124) NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001124) NetType/4G Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 8.1.0; DUA-TL00 Build/HONORDUA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2690 MMWEBSDK/200502 Mobile Safari/537.36 MMWEBID/2494 MicroMessenger/7.0.15.1680(0x27000F50) Process/toolsmp WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/2591 MicroMessenger/7.0.19.1760(0x2700133F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 10; VOG-AL00 Build/HUAWEIVOG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/8872 MicroMessenger/7.0.19.1760(0x2700133F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 9; vivo X21A Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/6397 MicroMessenger/7.0.19.1760(0x2700133F) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 10; WLZ-AN00 Build/HUAWEIWLZ-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/4902 MicroMessenger/7.0.19.1760(0x2700133F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 10; ELE-AL00 Build/HUAWEIELE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/215 MicroMessenger/7.0.19.1760(0x2700133F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 8.0.0; BLA-AL00 Build/HUAWEIBLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2690 MMWEBSDK/200401 Mobile Safari/537.36 MMWEBID/3762 MicroMessenger/7.0.14.1660(0x27000EC6) Process/toolsmp NetType/WIFI Language/zh_CN ABI/arm64 WeChat/arm32',
    'Mozilla/5.0 (Linux; Android 9; PBEM00 Build/PKQ1.190519.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/4773 MicroMessenger/7.0.19.1760(0x27001335) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
    'Mozilla/5.0 (Linux; Android 10; JEF-AN00 Build/HUAWEIJEF-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/8362 MicroMessenger/7.0.19.1760(0x2700133F) Process/toolsmp WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64'
]


def main():
    req('j001', 1, 0, '')
    #   四个参数
    # pos:位置
    # num:预约时间段(1:上午,2:下午,3:晚上)
    # day:预约日期(0:今天,1:明天,2:后天)
    # user_id:抓包获取


# pos:位置 num:预约时间段(1:上午,2:下午,3:晚上) day:预约日期(0:今天,1:明天,2:后天) user_id:抓包获取
# 示例 pos = 'j001', num = 1, day = 0, user_id = 0lL68iMY74TFFuIjYG%2B0bA%3D%3D
def req(pos, num, day, user_id):
    (pl_id, vd_id) = get_pl_vd_id(pos)
    if pl_id == 0 and vd_id == 0:
        print("不存在该位置")
        return
    rq.packages.urllib3.disable_warnings(InsecureRequestWarning)
    appoint_day = datetime.datetime.now() + datetime.timedelta(days=day)
    day_time = appoint_day.strftime('%Y-%m-%d')
    time_end = time_ends[num]  # 座位截至时间("12:00" "17:00" "23:00"
    code = str(pl_id) + ',' + str(vd_id) + ',' + str(num) + ',' + day_time + ',' + time_end
    # print(code)
    info = encry_info(code)
    headers = {
        'Connection': 'close',

        'User-Agent': User_Agents[random.randint(0, len(User_Agents) - 1)],
        # 'User-Agent': 'Mozilla/5.0 (Linux; Android 11; IN2010 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/7693 MicroMessenger/8.0.18.2060(0x28001237) Process/toolsmp WeChat/arm32 Weixin NetType/4G Language/zh_CN ABI/arm64',

        'charset': 'utf-8',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wxa30b47e94c4c8f08/25/page-frame.html'
    }
    url = "https://wxcourse.jxufe.cn/wxlib/wx/appoint" \
          "?userId={}&isPeriod=1&officeCode=jxcjdx&colleageId=51" \
          "&appointType=0&info={}".format(user_id, info)
    con = 1
    while con <= 5:
        try:
            resp = rq.get(url=url, headers=headers)
            result = resp.json()['message']
            detail = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') \
                     + ' ' + str(pos) + ',' + nums[num] + ',' + day_time
            print(detail, ' ', result)
            break
        except Exception as e:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end=' ')
            # print(e)
            print("第", con, "次连接异常，重连中...")
            headers['User-Agent'] = User_Agents[random.randint(0, len(User_Agents)-1)]
            con += 1
            time.sleep(1)


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result


def encry_info(info):
    # 编译加载js字符串
    context1 = execjs.compile(js_from_file('./info.js'))
    result1 = context1.call("encry_info", info)
    return result1


def get_pl_vd_id(position):
    pos = position.upper()
    seats = get_seats()
    for seat in seats:
        if seat['seat_number'] == pos:
            return seat['id'], seat['vd_id']
    return 0, 0


def get_seats():  # 返回seats数组字典 [{},{}]
    with open('position.json', 'r', encoding='UTF-8') as file_object:
        seats = json.load(file_object)
        return seats


if __name__ == "__main__":
    main()
