#!/usr/bin/python
# -*- coding: utf-8 -*-
import config

class mssql_exec():
    def __init__(self, coon, payload):
        self.payload = payload
        self.coon = coon

    def sql_exec(self):
        cur = self.coon.cursor()
        cur.execute(self.payload)
        try:
            return cur.fetchall()
        except Exception as e:
            pass
        cur.close()

def shell(coon):
    isXpCmdShell = config.get_systeminfo(conn=coon).get_xpcmdshell()
    if isXpCmdShell:
        code = input("[+]当前xp_cmdshell为开启模式，可以使用交互式shell，是否进入交互式shell(Y/N):").upper()
        if code == 'Y':
            print('[+]进入交互式shell模式，输入Q即可退出')
            while True:
                payload = input('请输入需执行的命令:')
                if payload.upper() != "Q":
                    payload=r"""exec master..xp_cmdshell '{}';""".format(payload)
                    restul = mssql_exec(coon=coon,payload=payload).sql_exec()
                    print(restul)
                else:
                    quit()
        else:
            quit()
    else:
        quit()