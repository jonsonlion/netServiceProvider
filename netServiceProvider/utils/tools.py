import pymysql
class DbManager(object):
    def __init__(self):
        self.con = pymysql.connect(host='39.108.134.38',
                                   user='root',
                                   password='123456',
                                   db='test',
                                   port=3306)
        self.cursor=self.con.cursor()

    def createTable(self, sql):
        try:
            self.cursor.execute(sql)
            print('sucess !')
        except Exception as e:
            print("fail to create table , case: {}".format(e))
            self.con.rollback()

    def insertRecord(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("fail to insert table , case: {}".format(e))

    def queryData(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            print(row)

    def deleteData(self, sql):
        try:
            self.cursor.execute(sql)
            print('delete successful!')
        except Exception as e:
            print('fail to delete data: {}'.format(e))

    def closeDb(self):
        self.con.commit()
        self.con.close()

if __name__ == "__main__":
    db = DbManager()
    sql = 'create table chinaunicom(typeName varchar(20) null,title1 varchar(50),title2 varchar(100),price varchar(20),detail_url varchar(100),inVoicetime varchar(50),inFlowgn varchar(50),inIncrementbusiness varchar(50),inFreeanswer varchar(50),extraVoicetime varchar(50),extraSms varchar(20),extraOtherbusiness varchar(50),combofeatures varchar(500),extraFlowgnAdd varchar(50),addPrivilege varchar(50)'
    db.createTable(sql)