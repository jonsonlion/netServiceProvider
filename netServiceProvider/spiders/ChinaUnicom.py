# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import parse
from ..items import ChinaunicomItem


class ChinaunicomSpider(scrapy.Spider):
    """
    联通4G基础套餐及资费详情
    手机app含所有附加包，暂未爬取
    """
    name = 'ChinaUnicom'
    allowed_domains = ['10010.cn', 's.10010.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            # 管道入库
            # 'netServiceProvider.pipelines.MysqlChinaunicomPipeline': 200
        }
    }

    # 套餐 api
    # start_urls = ['http://iservice.10010.com/e3/static/query/countryTariffQuery',]

    def start_requests(self):
        """post请求"""
        url = 'http://iservice.10010.com/e3/static/query/countryTariffQuery'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        formdata = {
            'isKey': 'public',
            'provinceId': '076',
            'cityId': '760'
        }
        yield scrapy.FormRequest(url=url, method='POST', headers=headers, formdata=formdata, callback=self.parse)

    def parse(self, response):
        print(response.headers)
        """
        一级页面，获取基础套餐
        """
        # print(response.body.decode())
        result = json.loads(response.body.decode())
        typeName1 = '公众套餐'
        for typeGoods in result['tariffTypeList']:
            title1 = typeGoods['tariffTypeName']
            isComboSet = typeGoods['isComboSet']
            packageNameCode = typeGoods['packageNameCode']
            typeName2 = typeGoods['tariffTypeName']
            for goods in typeGoods['tariffLis']:
                title2 = goods['basepackagename']
                feeUnit = goods['feeUnit']
                detailid = goods['detailid']
                detail_url = 'http://iservice.10010.com/e4/query/tariff/index_aTariffInfoDetail.html?id=' + \
                             detailid + '&isComboSet=' + isComboSet + '&type=' + \
                             packageNameCode + '&feeUnit=' + feeUnit
                price = goods['basemonthfee']
                url_api = 'http://iservice.10010.com/e3/static/query/tariffDetailInfo'
                formdata = {
                    'tariffDetailId': detailid,
                    'isComboSet': isComboSet,
                    'type': packageNameCode
                }
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                }
                goods_dic = {'typeName1': typeName1,'typeName2': typeName2, 'title1': title1, 'title2': title2, 'price': price,
                             'detail_url': detail_url}
                # print(typeName,title1, title2,price,detail_url)
                yield scrapy.FormRequest(url=url_api, method='POST', headers=headers, formdata=formdata,
                                         callback=self.get_detail, meta={'goods': goods_dic}, dont_filter=True)

    def get_detail(self, response):
        """
        二级页面，获取套餐详情
        """
        item = ChinaunicomItem()
        goods = response.meta['goods']
        goodsDetail = json.loads(response.body.decode())['packageinfo']

        item['typeName1'] = goods['typeName1']
        item['typeName2'] = goods['typeName2']
        item['title1'] = goods['title1']
        item['title2'] = goods['title2']
        item['price'] = goods['price']
        item['detail_url'] = goods['detail_url']
        item['inVoicetime'] = goodsDetail['inVoicetime']
        item['inFlowgn'] = goodsDetail['inFlowgn']
        item['inIncrementbusiness'] = goodsDetail['inIncrementbusiness']
        item['extraVoicetime'] = goodsDetail['extraVoicetime']
        item['extraSms'] = goodsDetail['extraSms']
        item['inFreeanswer'] = goodsDetail['inFreeanswer']
        item['extraOtherbusiness'] = goodsDetail['extraOtherbusiness']
        item['combofeatures'] = goodsDetail['combofeatures']
        item['extraFlowgnAdd'] = goodsDetail['extraFlowgnAdd']
        item['addPrivilege'] = goodsDetail['addPrivilege']

        yield item
