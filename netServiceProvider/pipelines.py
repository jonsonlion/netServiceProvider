# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class NetserviceproviderPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlServicePipeline(object):
    def __init__(self):
        self.con = pymysql.connect(host='39.108.134.38',
                                   user='',
                                   password='',
                                   db='provider',
                                   port=3306)
        self.cursor=self.con.cursor()
    def process_item(self, item, spider):
        self.cursor.execute('insert into mobile(goodsName,price,summary,webUrl,type,provider) VALUES ("{}","{}","{}","{}","{}","{}")'.format(item['goodsName'],item['price'],item['summary'],item['webUrl'],item['type'],item['provider']))
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()
class MysqlServicePhonesPipeline(MysqlServicePipeline):
    """三家运营商手机商城信息入库"""
    def process_item(self, item, spider):
        self.cursor.execute('insert into phones(title,brand,price,evalNum,detail_url,provider) VALUES ("{}","{}","{}","{}","{}","{}")'.format(item['title'],item['brand'],item['price'],item['evalNum'],item['detail_url'],item['provider']))
        self.con.commit()
        return item

class MysqlChinaunicomPipeline(MysqlServicePipeline):
    """联通web端套餐详情入库"""
    def process_item(self, item, spider):
        self.cursor.execute('insert into chinaunicom(typeName1,typeName2,title1,title2,price,detail_url,inVoicetime,inFlowgn,inIncrementbusiness,inFreeanswer,extraVoicetime,extraSms,extraOtherbusiness,combofeatures,extraFlowgnAdd,addPrivilege) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.\
                            format(item['typeName1'],item['typeName2'],item['title1'],item['title2'],item['price'],item['detail_url'],item['inVoicetime'],item['inFlowgn'],item['inIncrementbusiness'],item['inFreeanswer'],item['extraVoicetime'],item['extraSms'],item['extraOtherbusiness'],item['combofeatures'],item['extraFlowgnAdd'],item['addPrivilege']))
        self.con.commit()
        return item

class MysqlChinaunicomAppPkgPipeline(MysqlServicePipeline):
    """联通app端附加包入库"""
    def process_item(self, item, spider):
        self.cursor.execute(
            'insert into chinaunicom_app_pkg(type,title,fee,flow) VALUES ("{}","{}","{}","{}")'.format(
                item['typeValue'], item['title'], item['fee'], item['flow']))
        self.con.commit()
        return item
class MysqlChinaMobileAppPipeline(MysqlServicePipeline):
    """移动app端套餐入库"""
    def process_item(self, item, spider):
        print('正在入库...')
        self.cursor.execute(
            'insert into chinamobile_app(name,speedlimit,callbeyondfee,show_total_call,dingxiang_flow,callanswer,flowbeyondfee,v_4g_kd_new,tariffdesc) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                item['name'], item['speedlimit'], item['callbeyondfee'], item['show_total_call'],item['dingxiang_flow'],item['callanswer'],item['flowbeyondfee'],item['v_4g_kd_new'],item['tariffdesc']))
        self.con.commit()
        return item