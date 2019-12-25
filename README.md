# MssqlSeckill
## 0x001 开发初衷

最近在研究mssql的一些利用姿势，懒惰是人最大的特性，为了省去一些操作时间，于是有了自动化的想法，python可以完美的完成我们的需求，所以就有了MssqlSeckill.

## 0x002 具体功能

1.xp_cmdshell模式。==========>>顾名思义就是交互式的shell模式(前提是数据库xp_cmdshell模式为开启状态)，工具中也提供了xp_cmdshell的一键开启模式。

2.clr不落地执行模式。==========>>解决xp_cmdshell无法开启的问题。

3.base64写文件模式。==========>>这个功能主要是针对那些，无外网环境，需要将某些文件写入，并执行某些不可描述的操作时，无法通过主机访问外网获取文件时使用，例如传入mimikatz获取密码。

4.sqlshell模式。==========>>直接执行交互式sqlshell可执行查询等操作。

# 0x003 如何使用

git clone 到本地或者直接下载压缩包即可。

环境:pythone3 
包:pymssql

python3 MssqlSeckill.py -i 10.22.112.114 -p 1433 -u sa -P test -d msdb -m(模式选择) -f(exe,dll文件位置)


