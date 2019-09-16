# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import parse
from ..items import NetserviceproviderItem

from ..utils.Chinamobile import ChinaMobile


class ChinamobileSpider(scrapy.Spider):
    """
    移动基础套餐及附加包
    """
    name = 'ChinaMobile'
    allowed_domains = ['10086.cn']
    start_urls = ['http://www.10086.cn/fee/ha/index_371_371.html']
    custom_settings = {
        'ITEM_PIPELINES': {
            # 管道入库
            # 'netServiceProvider.pipelines.MysqlServicePipeline':200
        }
    }

    def start_requests(self):
        """
        post方式请求可选包api
        """
        # 可选包url
        url = 'http://www.10086.cn/web-Center/shopservice/query_goods_list.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        data = ChinaMobile.form_data()
        # print(data)
        yield scrapy.FormRequest(url, method='POST', headers=headers, formdata=data, callback=self.parse_list)

    def parse_list(self, response):
        """
        解析json数据，获取可选包list
        """
        json_data = json.loads(response.body.decode('utf-8'))
        goodsList = json_data['result']['data']['goodsInfo']   # 可选包
        for item in goodsList:
            item['type'] = 1
            item['provider'] = 1 # 移动
        # for id,goods in enumerate(goodsList):
        #     print(id, goods['goodsName'], goods['price'], goods['summary'].strip(),goods['webUrl'])
        url = 'http://www.10086.cn/fee/ha/index_371_371.html'
        yield scrapy.Request(url, callback=self.parse,meta={'goodsList':goodsList})

    def parse(self, response):
        """
        请求页面，获取基础套餐
        """
        # print(response.body.decode('utf-8'))
        resp = response.xpath('.//div[@class="zf_list_one"]')
        goodsList = response.meta['goodsList']

        for item in resp:
            goodsName = item.xpath('.//h3/text()').get().strip()
            price = item.xpath('.//span/text()').get()
            summary = item.xpath('.//div[@class="zf_jj"]/text()').get().strip()
            webUrl = 'http://www.10086.cn/' + item.xpath('.//a/@href').get().strip()
            d = {
                'goodsName': goodsName,
                'price': price,
                'summary': summary,
                'webUrl': webUrl,
                'type': 0,  # 基础套餐
                'provider': 1 # 移动
            }
            goodsList.append(d)

        item = NetserviceproviderItem()
        for goods in goodsList:
            item['goodsName'] = goods['goodsName']
            item['price'] = goods['price']
            item['summary'] = goods['summary']
            item['webUrl'] = goods['webUrl']
            item['type'] = goods['type']
            item['provider'] = goods['provider']

            yield item
