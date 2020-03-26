#!/usr/bin/python3
import requests, time
from bs4 import BeautifulSoup
from colorama import Fore,Back
from colorama import init
init(autoreset = True)
import argparse
def a_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--URL' ,help='The address of the site you want to scan .')
    parser.add_argument('-p','--PROXY' ,help='Set Proxy Socks : -p 127.0.0.1:9150 or -p 127.0.0.1:9050' )
    return parser.parse_args()


class Hidden_Param(object):
    def __init__(self, url, proxy):
        self.url = url
        self.proxy = proxy

    def banner(self):
        print(Fore.GREEN + """     

                +++++++++++++++++++++++++++++++++++++++++++++++++++++
                #    Find Hidden Parameter In The Site              #
                #    Version 1.0                                    #
                #    Github : https://github.com/reza-tanha/        #
                #    Telegram : T.me/S3CURITY_GARY                  #
                #    Code By : Haji (Reza)                          #
                #                                                   #
                #    Gray Security Team                             #
                +++++++++++++++++++++++++++++++++++++++++++++++++++++

        """)

    def check_http(self):
        if("http://" not in self.url and "https://" not in self.url):
            return "http://%s" %self.url
        return self.url


    def user_agent(self):
        user_a = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
         'Accept-Language': 'en-US;',
         'Accept-Encoding': 'gzip, deflate',
         'Accept': 'text/html,application/xhtml+xml,application/xml;',
         'Connection': 'close'}
        return user_a


    def scan_site(self):
        if self.proxy !=None:
            proxies = {
            'http': 'socks5h://{}'.format(self.proxy),
            'https': 'socks5h://{}'.format(self.proxy)
            }
        else:
            proxies = None
        try:
            req = requests.get(self.check_http(), proxies=proxies, headers=self.user_agent() , timeout=5)
            soup = BeautifulSoup(req.text, features='html.parser')
            c = 0
            ch = 0
            print(Fore.RED +"--"*len(self.check_http()))
            print(Fore.CYAN+ "site : "+Fore.GREEN+self.check_http())
            print(Fore.RED + "--" * len(self.check_http())+"\n")
            for i in soup.find_all():
                c+=1
                if i.get('type') == "hidden":
                    ch+=1
                    print(Fore.LIGHTGREEN_EX + "[+] Find Hidde Parameter in Line "+Fore.LIGHTYELLOW_EX+str(c) +" "+  Fore.LIGHTCYAN_EX + str(i))
                    time.sleep(0.1)
                    print(Fore.BLUE+'='*80)
            if ch == 0 :
                print(Fore.LIGHTYELLOW_EX+"[-] Hidden Field Not Found . Please check the other path of the site !!!")
        except:
            print(Fore.LIGHTRED_EX + "[-] Network Error . Pleas Check The Internet Connection !" )
if __name__ == '__main__':

    h = Hidden_Param(a_parse().URL, a_parse().PROXY)
    if a_parse().URL:
        time.sleep(1)
        h.banner()
        h.scan_site()
    else:
        h.banner()
        print(Fore.YELLOW+"Python3 hidden.py -h ")
