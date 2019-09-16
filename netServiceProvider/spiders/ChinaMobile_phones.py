# -*- coding: utf-8 -*-
import scrapy
import json
import re
from urllib import parse
from ..items import NetserviceproviderPhonesItem


class ChinaunicomSpider(scrapy.Spider):
    """
    移动手机商城
    手机详情暂未爬取
    """
    name = 'ChinaMobile_phones'
    allowed_domains = ['shop.10086.cn']
    custom_settings = {
        'ITEM_PIPELINES':{
            # 管道入库
            # 'netServiceProvider.pipelines.MysqlServicePhonesPipeline': 100
        }
    }
    start_urls = ['https://shop.10086.cn/list/101_371_371_1_0_0_0_0_0_0_0.html',]

    def parse(self,response):
        # print(response.body.decode())
        goods_list = response.xpath('.//div[@class="goodsList"]/ul/li')
        item = NetserviceproviderPhonesItem()
        for goods in goods_list:
            title = ''.join([title.strip() for title in goods.xpath('.//p[@class="name"]//text()').getall()])
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
            price = ''.join(goods.xpath('.//p[@class="price red"]//text()').getall())
            pattern = '\d+.\d+|\d+'
            price = eval(re.findall(pattern, price)[0])
            detail_url = goods.xpath('.//p[@class="img"]/a/@href').get()
            provider = 1
            evalNum = ''
            goods_dic = {k: v for k, v in zip(['title', 'brand','price', 'evalNum', 'detail_url', 'provider'],\
                                              [title, brand,price, evalNum, detail_url, provider])}
            for k,v in goods_dic.items():
                item[k] = v
            yield item
        next_page = response.xpath('.//a[text()="下一页"]/@href').get()
        if next_page:
            yield scrapy.Request('https://shop.10086.cn' + next_page, callback=self.parse, dont_filter=True)
    def get_detail(self, response):
        """
        请求页面，获取手机详情，building...
        todo
        """
        goods_dic = response.Meta['goods_dic']
        # print(response.body.decode('utf-8'))
        print(goods_dic)



