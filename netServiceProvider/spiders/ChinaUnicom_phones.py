# -*- coding: utf-8 -*-
import scrapy
import json
import re
from urllib import parse
from ..items import NetserviceproviderPhonesItem


class ChinaunicomSpider(scrapy.Spider):
    """
    联通手机商城
    """
    name = 'ChinaUnicom_phones'
    allowed_domains = ['10010.cn','s.10010.com']
    custom_settings = {
        'ITEM_PIPELINES':{
            # 管道入库
            # 'netServiceProvider.pipelines.MysqlServicePhonesPipeline': 100
        }
    }
    start_urls = ['http://s.10010.com/henan/mobilelist-0-0-0-0-65-0-0-0-0-0-0/',]

    def parse(self,response):
        # print(response.body.decode())
        goods_list = response.xpath('.//ul[@class="goodsListInfor"]/li[@class="goodsLi"]')
        pattern = r"\d+"
        item = NetserviceproviderPhonesItem()
        for goods in goods_list:
            title = goods.xpath('.//img/@title').get() # .extract()
            pattern = r'iPhone|苹果|华为|小米|OPPO|oppo|VIVO|vivo|荣耀|三星|IQOO'
            result = re.search(pattern, title)
            if result:
                brand = result[0]
                if brand == "iPhone":
                    brand = '苹果'
                elif brand == 'IQOO':
                    brand = 'VIVO'
                elif brand == 'oppo':
                    brand = 'OPPO'
                elif brand == 'vivo':
                    brand = 'VIVO'
                elif brand == '荣耀':
                    brand = '华为'
            else:
                brand = '其他'
            price = goods.xpath('.//p[@class="evaluation"]/label/text()').get()
            pattern = '\d+.\d+|\d+'
            price = eval(re.findall(pattern, price)[0])
            evalNum = goods.xpath('.//p[@class="evalNum"]/a/text()').get()
            if evalNum:
                evalNum = re.findall(pattern, evalNum)
            else:
                evalNum = ''
            detail_url = goods.xpath('.//a[@class="goodsImg"]/@href').get()
            provider = 0
            goods_dic = {k:v for k,v in zip(['title','brand','price','evalNum','detail_url','provider'],[title,brand,price,evalNum,detail_url,provider])}
            for k,v in goods_dic.items():
                item[k] = v
            yield item

        next_page = response.xpath('.//div[@class="pageCount"]/a[1]/@href').get()
        cur_page = response.xpath('.//div[@class="pageCount"]/span[last()]/text()').get()
        if cur_page != '7/7':
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)

    def get_detail(self, response):
        """
        请求页面，获取手机详情，building...
        todo
        """
        goods_dic = response.Meta['goods_dic']
        # print(response.body.decode('utf-8'))
        print(goods_dic)



