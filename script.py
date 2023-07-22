import os, time
from pick import pick
from termcolor import colored

banner = '''             __   __        __           __  ___             ___  __   __  
|  | | |\ | |  \ /  \ |  | /__`     /\  /  `  |  | \  /  /\   |  /  \ |__) 
|/\| | | \| |__/ \__/ |/\| .__/    /~~\ \__,  |  |  \/  /~~\  |  \__/ |  \ 


                    [<>]    github.com/miceroman   [<>]                                              
'''


os.system('@mode con cols=80 lines=30')



def sprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.5/20)
    print()



def main_menu():
    os.system('title Windows Activator')
    title = banner
    options = ['[1] Windows 7', '[2] Windows 10', '[3] Windows 11']
    option, index = pick(options, title, indicator='=>', default_index=0)

    if index == 0:
        win7()
    elif index == 1:
        win10()
    elif index == 2:
        win11()



def win7():
    os.system('title Windows Activator')
    os.system('cls')
    title = banner +    '''
[-] Windows 7 [-] 
'''
    options = ['[1] Windows 7 Home', '[2] Windows 7 Pro', '[3] Windows 7 Ultimate', '[4] Windows 7 Enterprise', '[0] Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if index == 0:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 7 Home Version...','cyan'))
        os.system('slmgr /ipk ')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 7 Home Activated!','green'))
        os.system('pause >nul')
    elif index == 1:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 7 Pro Version...','cyan'))
        os.system('slmgr /ipk ')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 7 Pro Activated!','green'))
        os.system('pause >nul')
    elif index == 2:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 7 Ultimate Version...','cyan'))
        os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ipk JHY4Q-NH85H-XK8VD-9Y68P-RFQ43 >nul')
        os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ipk 45KI6-6GY6Y-KHXCQ-7DDY6-TF7CD >nul')
        os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ipk LOHY7-P3ERP-ZXYCV-Q2H7C-FCGFR >nul')
        os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ipk h6Y9R-C9PPG-3CWTY-Y4MPW-COI2J >nul')
        os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ipk 65THD-F8XX6-YG69F-9M66D-MKSTY >nul')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 7 Ultimate Activated!','green'))
        os.system('pause >nul')
    elif index == 3:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 7 Enterprise Version...','cyan'))
        os.system('slmgr /ipk ')
        os.system('slmgr /skms kms8.msguides.com')
        os.system('slmgr /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 7 Enterprise Activated!','green'))
        os.system('pause >nul')
    elif index == 4:
        main_menu()



def win10():
    os.system('title Windows Activator')
    os.system('cls')
    title = banner +    '''

[-] Windows 10 [-] 
'''
    options = ['[1] Windows 10 Home', '[2] Windows 10 Home N', '[3] Windows 10 Pro', '[4] Windows 10 Pro N', '[5] Windows 10 Enterprise', '[6] Windows 10 Enterprise N', '[7] Windows 10 Education', '[8] Windows 10 Education N', '[0] Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if index == 0:
        os.system('title Activating Windows 10 Home')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Home Version ...','cyan'))
        os.system('slmgr //B /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Home Activated!','green'))
        os.system('pause >nul')
    elif index == 1:
        os.system('title Activating Windows 10 Home N')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Home N Version ...','cyan'))
        os.system('slmgr //B /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Home N Activated!','green'))
        os.system('pause >nul')
    elif index == 2:
        os.system('title Activating Windows 10 Pro')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Pro Version ...','cyan'))
        os.system('slmgr //B /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Pro Activated!','green'))
        os.system('pause >nul')
    elif index == 3:
        os.system('title Activating Windows 10 Pro N')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Pro N Version...','cyan'))
        os.system('slmgr //B /ipk MH37W-N47XK-V7XM9-C7227-GCQG9')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Pro N Activated!','green'))
        os.system('pause >nul')
    elif index == 4:
        os.system('title Activating Windows 10 Enterprise')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Enterprise Version...','cyan'))
        os.system('slmgr //B /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Enterprise Activated!','green'))
        os.system('pause >nul')
    elif index == 5:
        os.system('title Activating Windows 10 Enterprise N')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Enterprise N Version...','cyan'))
        os.system('slmgr //B /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Enterprise N Activated!','green'))
        os.system('pause >nul')
    elif index == 6:
        os.system('title Activating Windows 10 Education')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Education Version...','cyan'))
        os.system('slmgr //B /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Succcess] Windows 10 Education Activated!','green'))
        os.system('pause >nul')
    elif index == 7:
        os.system('title Activating Windows 10 Education N')
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 10 Education N Version...','cyan'))
        os.system('slmgr //B /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ')
        os.system('slmgr //B /skms kms8.msguides.com')
        os.system('slmgr //B /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 10 Education N Activated!','green'))
        os.system('pause >nul')
    elif index == 8:
        main_menu()



def win11():
    os.system('title Windows Activator')
    os.system('cls')
    title = banner +    '''

[-] Windows 11 [-]
'''
    options = ['[1] Windows 11 Home', '[2] Windows 11 Pro', '[3] Windows 11 Enterprise', '[4] Windows 11 Education', '[0] Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if index == 0:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 11 Home Version...','cyan'))
        os.system('slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
        os.system('slmgr.vbs /skms kms.lotro.cc')
        os.system('slmgr.vbs /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 11 Home Activated!','green'))
        os.system('pause >nul')
    elif index == 1:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 11 Pro Version...','cyan'))
        os.system('slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
        os.system('slmgr.vbs /skms kms.lotro.cc')
        os.system('slmgr.vbs /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 11 Pro Activated!','green'))
        os.system('pause >nul')
    elif index == 2:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 11 Pro for Workstations Version...','cyan'))
        os.system('slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
        os.system('slmgr.vbs /skms kms.lotro.cc')
        os.system('slmgr.vbs /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 11 Pro for Workstations Activated!','green'))
        os.system('pause >nul')
    elif index == 3:
        os.system('cls')
        print(banner)
        sprint(colored('[>] Activating Windows 11 Education Version...','cyan'))
        os.system('slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43B8YKP-D69TJ')
        os.system('slmgr.vbs /skms kms.lotro.cc')
        os.system('slmgr.vbs /ato')
        os.system('cls')
        print(banner)
        sprint(colored('[Success] Windows 11 Education Activated!','green'))
        os.system('pause >nul')
    elif index == 4:
        main_menu()



#start 
main_menu()