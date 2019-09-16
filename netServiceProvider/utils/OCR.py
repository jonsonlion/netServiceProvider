# - * - coding:utf-8 - * -
import hashlib
import time
import random
from urllib import parse
import base64,requests

info = {
    "ID":"2121122875",
    "KEY":"4lu1c35uvsKBy57j"
}


def getNonce_str():
    '''
    获得API所需的Nonce_str参数
    :return:Nonce_str 请求参数
    '''
    eg = "fa577ce340859f9fe"
    seed_ = "abcdefghijklmnopqrstuvwxyz0123456789"
    Nonce_str = ""
    for i in range(len(eg)):
        Nonce_str += seed_[random.randint(0,len(seed_)-1)]
    return Nonce_str


def getTimestamp():
    '''
    返回秒级时间戳
    '''
    t = time.time()
    return int(t)

def getMD5(strings):
    my_Md5 = hashlib.md5()
    my_Md5.update(strings.encode("utf-8"))
    secure = my_Md5.hexdigest()
    #print (secure)
    return secure

def parser(paramsDic):
    params = sorted(paramsDic.items())
    data = parse.urlencode(params).encode("utf-8")
    return data

def imgProcessing(imgPathstr):
    '''

    :param imgPathstr:图片路径
    :return: 图片base64编码
    '''

    f = open(imgPathstr, "rb")
    ls_f = base64.b64encode(f.read())
    ls_f = str(ls_f,encoding = "utf-8")
    f.close()
    return ls_f


def getReqSign(paramsDic, AppKey):
    '''
    签名有效期5分钟
    :param paramsDic: 参数字典
    :param AppKey: APPKey
    :return:
    '''
    params = sorted(paramsDic.items())
    url_data = parse.urlencode(params)
    print(url_data)
    url_data = url_data + "&" + "app_key" + "=" + info["KEY"]
    url_data = getMD5(url_data).upper()
    return  url_data
if __name__ in "__main__":
    url = r"https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr"

    reqDic = {
        "app_id": int(info["ID"]),
        "image": imgProcessing("电信.jpg"),
        "nonce_str": getNonce_str(),
        "time_stamp": int(getTimestamp()),
    }

    reqDic["sign"] = getReqSign(reqDic, info["KEY"])
    
    # reqData = str(parser(reqDic),encoding="utf-8")

    # print (reqData)
 
    # reqData = json.dumps(reqDic)
    reqData = sorted(reqDic.items())
    reqDatas = parse.urlencode(reqData)
    print(reqData)
    req = requests.post(url, reqData)
    res = req.text
    print(req.status_code)
    print(res)