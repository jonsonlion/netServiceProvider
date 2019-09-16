# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import parse
from ..items import ChinaMobileAppItem

class ChinaunicomAppSpider(scrapy.Spider):
    """
    手机app含所有附加包
    """
    name = 'ChinaMobile_app'
    allowed_domains = ['h5.ha.chinamobile.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            # 管道入库
            # 'netServiceProvider.pipelines.MysqlChinaMobileAppPipeline': 100
        }
    }

    # start_urls = ['https://m.client.10010.com/mobileService/businessTransact/query3gFlowData.htm',]

    def start_requests(self):
        """post请求api"""
        url = 'https://h5.ha.chinamobile.com/hnmccClientWap/zuheNew/getGlobalMealList.do'
        headers = {
            'Host': 'h5.ha.chinamobile.com',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://h5.ha.chinamobile.com',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'https://m.client.10010.com/mobileService/businessTransact/query3gFlowDetail.htm?flowType=adFlow&menuId=000300010001',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
        }
        cookieStr = 'JSESSIONID=5A97A22D5F5587696560A5BF656408DB; hncmtokenid="7ca279d998d056500a4507dfb8924fef@hn.ac.10086.cn"; hncmjsSSOCookie="7ca279d998d056500a4507dfb8924fef@hn.ac.10086.cn"; VersionName=6.3.1; channel=HUAWEI_CHANNEL; DeviceUDID=867476039456516&18839125156&H; mobile=61733-8534-6169-33683; WT_FPC=id=23743f997c16e4b01131567942007165:lv=1567945357295:ss=1567945340752'
        cookieList = cookieStr.replace(' ', '').split(';')
        cookie = {}
        for item in cookieList:
            cookie[item.split('=')[0]] = item.split('=')[1]

        formdata = {
            'isOpenKD': 'true',
            'broadRate': '50M'
        }
        yield scrapy.FormRequest(url=url, method='POST', headers=headers, cookies=cookie, formdata=formdata,
                                 callback=self.parse, dont_filter=True)
    def parse(self, response):
        result = json.loads(response.body.decode())
        item = ChinaMobileAppItem()
        for goods in result['returnMealList']:
            item['name'] = goods['V_NAME']
            item['speedlimit'] = goods['V_SPEEDLIMIT']
            item['callbeyondfee'] = goods['V_CALLBEYONDFEE']
            item['show_total_call'] = goods['V_SHOW_TOTAL_CALL']
            item['dingxiang_flow'] = goods['V_DINGXIANG_FLOW']
            item['callanswer'] = goods['V_CALLANSWER']
            item['flowbeyondfee'] = goods['V_FLOWBEYONDFEE']
            item['v_4g_kd_new'] = goods['V_4G_KD_NEW']
            item['tariffdesc'] = goods['V_TARIFFDESC']
            yield item


