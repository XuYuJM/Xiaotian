@echo off
ping localhost -n 60
E:
cd E:\01-二木工作室
start "" pythonw runv0.0.1.py
:: vmrun -T ws start "E:\05-虚拟主机\vbird\vbird.vmx" nogui
:: ping localhost -n 60
:: E:
:: cd E:\python\XiaoMu\01-xiaotian
:: start "" pythonw 01-SSYYv0.0.1.py
:: start "" pythonw 02-SSHYv0.0.8.py
