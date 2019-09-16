import time, datetime
import hashlib, base64
import json
import re

class ChinaMobile(object):
    def __init__(self):
        pass
    @classmethod
    def form_data(cls):
        """
        http://www.10086.cn/web-Center/shopservice/query_goods_list.do
        http://www.10086.cn/web-Center/shopservice/query_goods_list.do
        js逆向，form表单封装
        :return: form表单
        :type: dict
        """
        curtime = int(round(time.time() * 1000))
        data = {
                     'channelId': '0001',
                     'provId': 371,
                     'cityId': 371,
                     'goodsType': 2,
                     'pageSize': 9999999,
                     'pageNo': 1,
                     'isNeedTotalNum': 1
                 }
        header = {
                 'version': '1.0',
                 'timestamp': curtime,
                 'digest': getDigest(curtime, 'CM_201606'),
                 'conversationId': getConversationId(curtime)
             }
        form = {
            'serviceName': 'if005_query_goods_list',
             'header': json.dumps(header),
            'data': json.dumps(data)
        }
        form_data ={
            'requestJson': re.sub(r' |\\','',json.dumps(form)).replace('"{','{').replace('}"','}')
        }

        return form_data

def getDigest(curtime, secret):
    strmd5 = hashlib.md5((str(curtime) + secret).encode())
    strbase64 = base64.b64encode(strmd5.hexdigest().encode('utf-8'))
    return str(strbase64)[2:-1]

def getConversationId(curtime):
    date_now = datetime.datetime.now()
    year = "%02d" % date_now.year
    month = "%02d" % date_now.month
    day = "%02d" % date_now.day
    hour = "%02d" % date_now.hour
    minute = "%02d" % date_now.minute
    second = "%02d" % date_now.second
    millisecond = str(date_now.microsecond)[:3]
    strseed = str(curtime) + ',' + 'http://www.10086.cn/fee/ha/index_371_371.html' + 'Netscape' + '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' + 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    # 根据当前时间毫秒数、url以及用户特定信息进行md5运算，产生随机数
    # rnd = formarNumber(parseInt($.md5(strSeed).substring(25, 32), 16), 6);
    mid = hashlib.md5(strseed.encode()).hexdigest()[25:32]
    rnd = str(int(mid, 16))[-6:]

    rv = year + month + day + hour + minute + second + millisecond +rnd
    return rv
