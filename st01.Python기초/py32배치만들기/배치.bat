@echo off

setlocal enableDelayedExpansion 

rem bat ������ ������ ���� ���� ���� ������ �߿��մϴ�.
rem bat ������ utf-8 ������� �����ϸ� ������ �ȵ� ���� ����. 
rem bat ������ ������ ���� �ݵ�� ASCII ������� �����ؾ� �Ѵ�. 
rem
rem bat ������ ������ ���񽺷� ����ϴ� ����� ���� �˻��Ѵ�. 
rem https://potensj.tistory.com/108

SET ROOTDIR=%CD%

:CheckOS
IF EXIST "%PROGRAMFILES(X86)%" (set BITS=64) ELSE (set BITS=32)



rem @@@@@@@@@@@@@@@@@@@@@
rem step 1. PYTHONPATH Ȯ��
rem @@@@@@@@@@@@@@@@@@@@@

echo %PYTHONPATH%

rem @@@@@@@@@@@@@@@@@@@@@
rem step 2. ���� ���丮 Ȯ��
rem @@@@@@@@@@@@@@@@@@@@@
echo %ROOTDIR%
echo[ 

rem %PYTHONPATH%\python.exe %ROOTDIR%\py�ҽ�.py

python.exe %ROOTDIR%\��ġ.py





PAUSE
EXIT


