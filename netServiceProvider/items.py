# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NetserviceproviderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goodsName = scrapy.Field()
    price = scrapy.Field()
    summary = scrapy.Field()
    webUrl = scrapy.Field()
    type = scrapy.Field()
    provider = scrapy.Field()
class NetserviceproviderPhonesItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    evalNum = scrapy.Field()
    detail_url = scrapy.Field()
    provider = scrapy.Field()

class ChinaunicomItem(scrapy.Item):
    """河南web端联通数据模型"""
    # 一级页面
    typeName1 = scrapy.Field()
    typeName2 = scrapy.Field()
    title1 = scrapy.Field()
    title2 = scrapy.Field()
    price = scrapy.Field()
    detail_url = scrapy.Field()
    # 二级页面
    inVoicetime = scrapy.Field()
    inFlowgn = scrapy.Field()
    inIncrementbusiness = scrapy.Field()
    inFreeanswer = scrapy.Field()
    extraVoicetime = scrapy.Field()
    extraSms = scrapy.Field()
    extraOtherbusiness = scrapy.Field()
    combofeatures = scrapy.Field()
    extraFlowgnAdd = scrapy.Field()
    addPrivilege = scrapy.Field()
class ChinaunicomAppPkgItem(scrapy.Item):
    """河南联通手机端附加包"""
    typeValue = scrapy.Field()
    title = scrapy.Field()
    fee = scrapy.Field()
    flow = scrapy.Field()
class ChinaMobileAppItem(scrapy.Item):
    """河南联通app端套餐"""
    name = scrapy.Field()
    speedlimit = scrapy.Field()
    callbeyondfee = scrapy.Field()
    show_total_call = scrapy.Field()
    dingxiang_flow = scrapy.Field()
    callanswer = scrapy.Field()
    flowbeyondfee = scrapy.Field()
    v_4g_kd_new = scrapy.Field()
    tariffdesc = scrapy.Field()