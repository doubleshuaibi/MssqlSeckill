#!/usr/bin/python
# -*- coding: utf-8 -*-
import config


class get_dbinfo:
    def __init__(self, coon,model):
        self.model = model
        self.coon = coon
    
    def get_mssqlinfo(self):
        systeminfo = config.get_systeminfo(conn=self.coon)
        sqlVersion = systeminfo.get_version()
        isXpCmdShell = systeminfo.get_xpcmdshell()

        print(sqlVersion)
        if isXpCmdShell:
            print("[+]xpcmdshell为开启状态")
            CurrentPermisssions = systeminfo.get_CurrentPermisssions()
            print(CurrentPermisssions)
        elif self.model.upper() !='C' and self.model.upper() != "S":
            xunze = input("[-]xp_cmdshell未开启是否尝试开启(请输入Y/N):").upper()
            if xunze == 'Y':
                code = systeminfo.openXpCmdshell()
                if code:
                    Permisssions = systeminfo.get_CurrentPermisssions()
                    print(Permisssions)
                else:
                    quit()
            else:
                quit()
        else:
            print("[-]xp_cmdshell未开启s")
