print('[info]Starting tool ipinfo \n')
try:
    # import session
    import sys
    import requests
    ## flowing with @ jit #from numba import jit
except:
    #install requement
    from os import system as sh
    sh('pip install requests && pip install numba')
## remove this if you went to get faster #@jit
def ipssl(ip):
    print('[set] search in [ ', ip, ' ] for info')
    urlG = str('http://ipinfo.io/' + ip)
    re = requests.get(urlG)
    print(re.text)
    if '-f' in sys.argv[2]:
        filej = open(sys.argv[3], 'a')
        spcace = str('\n' + re.text)
        filej.write(re.text)
        filej.close()
    print('[info] File Save')
def nocon():
        print(' You Can Use >>> $IPINFO-kira.py {ip} or {my}')
        ip = input(' ipv4]} ')
        if '.' in ip:
            ipssl(ip=ip)
        else:
            if ip == 'my':
                ipssl(ip='')
            else:
                print('This is{',ip ,'}not ip addras  quit(0110010)')
try:
    yip = str(sys.argv[1])
except:
    nocon()
    exit()
if '.' in yip:
    ipssl(ip=yip)
else:
    if '--help' in yip:
        print ("""
        -help '--help'   -This help print page
        -order '-A'        -print information of maker this tool and support also help page

                python3 __main__ 1.1.1.1 -f flarip.json 
            to use The script try:
                run it dirc
                run like this '' python3 IPINFO-kira.py <IP>''
            except:
                you cat select more then 2 option
            and enjoy ... 
        """)
    else:
        if '-A' in yip:
            print("""
             make this tool to be frindData reder and option
                This tool use http://ipinfo.io/ for more of this
                    request from facebook accont or call me 
                        Licenc Enterprise Edition.
            """)
        else:
            nocon()
