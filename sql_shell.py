# -*- coding: utf-8 -*
#!/usr/bin/python3

import config


def sql_shell(coon):
    while True:
        xuanze = input("[+]请输入要执行SQL语句：")
        if xuanze.upper() != "Q" :
            payloads = xuanze + ";"
            print(payloads)
            result = config.mssql_exec(coon=coon, payload=payloads).sql_shell()
            print(result)
        else:
            quit()















