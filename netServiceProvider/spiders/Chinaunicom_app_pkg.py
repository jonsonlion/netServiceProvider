# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import parse
from ..items import ChinaunicomAppPkgItem

typeDic = {
    '月包': 'month',
    '加速包': 'jiasu',
    '加油包': 'small',
    '日包': 'day',
    '半年包': 'half',
    '视频包': 'video',
    '社交包': 'shejiao',
    '音乐包': 'music',
    '游戏包': 'games',
    '教育包': 'education'
}


class ChinaunicomAppPkgSpider(scrapy.Spider):
    """
    手机app含所有附加包，bulding...
    """
    name = 'ChinaUnicom_app_pkg'
    allowed_domains = ['m.client.10010.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            # 管道入库
            # 'netServiceProvider.pipelines.MysqlChinaunicomAppPkgPipeline': 100
        }
    }

    # start_urls = ['https://m.client.10010.com/mobileService/businessTransact/query3gFlowData.htm',]

    def start_requests(self):
        """post请求api"""
        url = 'https://m.client.10010.com/mobileService/businessTransact/query3gFlowData.htm'
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://m.client.10010.com',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'https://m.client.10010.com/mobileService/businessTransact/query3gFlowDetail.htm?flowType=adFlow&menuId=000300010001',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'clientid=76|760; mobileServicecb=cd450222ceab1d23b778198f16d172f5; city=076|776; MUT_S=android9; on_token=dc905cb7f093b99cb9cc335eb2c59cd4; a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjgyOTAwMzQsInRva2VuIjp7ImxvZ2luVXNlciI6IjE4NTM3NjIzOTkxIiwicmFuZG9tU3RyIjoieWg2OTZkOTMxNTY3Njg1MjM0In0sImlhdCI6MTU2NzY4NTIzNH0.ulO1Oc7qbXMlSfzxK_I4qmDxmuNz1npyl48_MU2Rjtmx0wyfotjM_5SGCDa2sSikDHrCSE4yaMx0XNtsYmX8qA; c_id=a2db0bdf27ca46c8c36ff6474ee8f5123b1d9d99f49fdd235982bb481c58891f; u_type=11; login_type=06; login_type=06; u_account=18537623991; c_version=android@6.0200; d_deviceCode=357594090735110; enc_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; ecs_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; random_login=0; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c3214741cf7c09951e029e6176eac10fc91c6b092847bd44713a0539dc646dc4711f571b1884d2d9496354d6fba583b61a42; t3_token=c69acc2ade3ad79f62aa7dd96117fd18; invalid_at=a0fadf9f1d1a4d6bca3200b3abf2a1285fa97cfbd207a77d91df2f79fa23943a; c_mobile=18537623991; wo_family=0; u_areaCode=776; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDJiZDhmOGZlZmRkMDNlNThmZmQyZTZhNTBlM2E2YzY4ODJmNjBkZWYwYjY0NDA1ODk1YzMyMjJiNTEyOGQwZmM0MGYyMzNiNjEyODQ2MGU5MGU2MWM3ZWUzMDExNzM0MzY4NmU0M2Q4ZTliNTQ0ZTc4ZGIyMjJkZTIxZjNmOGY4ZSIsInZlcnNpb24iOiIwMCJ9; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc2M2Q4ZWU2M2U4ZjAxYTk5OGEzNTQ2NDcwMDFmNzI3NGUzYjkxNTdmZWFhNTFhMTg2ODVjNTA2OTI2YzNkMjI5NTIzZDYxMDYxNjJhMDdiYTJmNjk3NDRhYWNmNDg5MDNhODVjYzEzMDQyY2M2ZWQwNmYyYmUwYWY3MDg2Y2ViYjQ0MTVjYTFkZjEwZmViZGZhYmNmYmYyMDA1NzdkYTljIiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODUzNzYyMzk5MSIsInBybyI6IjA3NiIsImNpdHkiOiI3NzYiLCJpZCI6IjdhZTY3ZmFkZjgyYTBkYmIwY2E5Mjc1MjJjZmZhNmIwIn0.fWB9hD_3K1X9tNuLAXxP-SufnAuvFvdQJ77Xb_5j1ak; on_info=b7ebdc40ed1791ad2f844a90b2dc06c5; route=4409263098d857a3cc010d262182161c; quickNews=c4262666dd4015fec36598709ee86054; mobileService1=AgUBUlANGuXp-4WqZItsIE77EJmL8ZdUyRXt6vaXgX1s1cmnxEi7!1281027958; mobileServicecb=08f5e4b99c5ae9cdf5e6ed5c577d82f6; mobileroute=1283a065341572fcf9f6977a9f99b90e1fd62c86; SHAREJSESSIONID=85F6BBD1D5EF590F316ED6E0204ECDEC; ecs_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; c_sfbm=234g_00; ecs_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; req_mobile=18537623991; req_serial=; req_wheel=ssss; c_sfbm=4g_1',
            'X-Requested-With': 'com.sinovatech.unicom.ui'
        }
        cookieStr = 'clientid=76|760; city=076|776; MUT_S=android9; on_token=dc905cb7f093b99cb9cc335eb2c59cd4; a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjgyOTAwMzQsInRva2VuIjp7ImxvZ2luVXNlciI6IjE4NTM3NjIzOTkxIiwicmFuZG9tU3RyIjoieWg2OTZkOTMxNTY3Njg1MjM0In0sImlhdCI6MTU2NzY4NTIzNH0.ulO1Oc7qbXMlSfzxK_I4qmDxmuNz1npyl48_MU2Rjtmx0wyfotjM_5SGCDa2sSikDHrCSE4yaMx0XNtsYmX8qA; c_id=a2db0bdf27ca46c8c36ff6474ee8f5123b1d9d99f49fdd235982bb481c58891f; u_type=11; login_type=06; login_type=06; u_account=18537623991; c_version=android@6.0200; d_deviceCode=357594090735110; enc_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; ecs_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; random_login=0; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c3214741cf7c09951e029e6176eac10fc91c6b092847bd44713a0539dc646dc4711f571b1884d2d9496354d6fba583b61a42; t3_token=c69acc2ade3ad79f62aa7dd96117fd18; invalid_at=a0fadf9f1d1a4d6bca3200b3abf2a1285fa97cfbd207a77d91df2f79fa23943a; c_mobile=18537623991; wo_family=0; u_areaCode=776; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDJiZDhmOGZlZmRkMDNlNThmZmQyZTZhNTBlM2E2YzY4ODJmNjBkZWYwYjY0NDA1ODk1YzMyMjJiNTEyOGQwZmM0MGYyMzNiNjEyODQ2MGU5MGU2MWM3ZWUzMDExNzM0MzY4NmU0M2Q4ZTliNTQ0ZTc4ZGIyMjJkZTIxZjNmOGY4ZSIsInZlcnNpb24iOiIwMCJ9; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc2M2Q4ZWU2M2U4ZjAxYTk5OGEzNTQ2NDcwMDFmNzI3NGUzYjkxNTdmZWFhNTFhMTg2ODVjNTA2OTI2YzNkMjI5NTIzZDYxMDYxNjJhMDdiYTJmNjk3NDRhYWNmNDg5MDNhODVjYzEzMDQyY2M2ZWQwNmYyYmUwYWY3MDg2Y2ViYjQ0MTVjYTFkZjEwZmViZGZhYmNmYmYyMDA1NzdkYTljIiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODUzNzYyMzk5MSIsInBybyI6IjA3NiIsImNpdHkiOiI3NzYiLCJpZCI6IjdhZTY3ZmFkZjgyYTBkYmIwY2E5Mjc1MjJjZmZhNmIwIn0.fWB9hD_3K1X9tNuLAXxP-SufnAuvFvdQJ77Xb_5j1ak; on_info=b7ebdc40ed1791ad2f844a90b2dc06c5; quickNews=c4262666dd4015fec36598709ee86054; mobileService1=AgUBUlANGuXp-4WqZItsIE77EJmL8ZdUyRXt6vaXgX1s1cmnxEi7!1281027958; mobileServicecb=08f5e4b99c5ae9cdf5e6ed5c577d82f6; mobileroute=1283a065341572fcf9f6977a9f99b90e1fd62c86; ecs_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; c_sfbm=234g_00; ecs_acc=OWorsGIu2Gm3LWHZp3fg9S/W1w8E8J57vmhvVgSX0V86HLCeHqvsy7vIf0VzfThIzkgNaK4ilgFCxrZGfXeZvP/iUIkGKWuDRx7qQGJVwdV+aPobcm3du2ql2E5E6AExWURBNG/4yy2LR7Zeq7TOO/Kchj/2+l43wkHQM+k0MA8=; req_mobile=18537623991; req_serial=; req_wheel=ssss; c_sfbm=4g_1; route=6e287cc855950ad0751dbd7f4ae6ffa1; mobileroute=d31b50fd3f62b5c2d659085cc781d8a77b72ce79; SHAREJSESSIONID=D99059A062BCE652BEA77A54DD8901BB'
        cookieList = cookieStr.replace(' ', '').split(';')
        cookie = {}
        for item in cookieList:
            cookie[item.split('=')[0]] = item.split('=')[1]
        for typeValue in typeDic.values():
            formdata = {
                'type': typeValue
            }
            yield scrapy.FormRequest(url=url, method='POST', headers=headers, cookies=cookie, formdata=formdata,
                                     meta={'typeValue': typeValue}, callback=self.parse, dont_filter=True)
    def parse(self, response):
        """获取json数据"""
        typeValue = response.meta['typeValue']
        result = json.loads(response.body.decode())
        if typeValue == 'month':
            yield scrapy.Request(response.url,callback=self.get_pkg,dont_filter=True,meta={'alist':result['xsCountry'],'typeValue':typeValue})
        elif typeValue == 'jiasu':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['smallFlowGN'], 'typeValue': typeValue})
        elif typeValue == 'small':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['smallFlowGN'], 'typeValue': typeValue})
        elif typeValue == 'day':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['moreDayCountry'], 'typeValue': typeValue})
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['dayCountry'], 'typeValue': typeValue})
        elif typeValue == 'half':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['currenList'], 'typeValue': typeValue})
        elif typeValue == 'video':
            for vlist in result.values():
                if vlist:
                    yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': vlist, 'typeValue': typeValue})
        elif typeValue == 'shejiao':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['zixun'], 'typeValue': typeValue})
        elif typeValue == 'music':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['flowStormMusic'], 'typeValue': typeValue})
        elif typeValue == 'games':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['flowStormLimits04gn'], 'typeValue': typeValue})
        elif typeValue == 'education':
            yield scrapy.Request(response.url, callback=self.get_pkg, dont_filter=True,meta={'alist': result['flowStormEducation'], 'typeValue': typeValue})
    def get_pkg(self,response):
        """获取附加包详情"""
        alist = response.meta['alist']
        typeValue = response.meta['typeValue']
        for value in alist:
            fee = value['fee']
            if isinstance(value['fee'],list):
                fee = value['fee'][0]
            try:
                title = value['packageName']
            except Exception as e:
                title = value['title']
            flow = value['flow']

            item = ChinaunicomAppPkgItem()
            item['typeValue'] = typeValue
            item['title'] = title
            item['fee'] = fee
            item['flow'] = flow
            yield item

