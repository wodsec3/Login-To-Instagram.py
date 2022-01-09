import requests, json, urllib.parse
from my_fake_useragent import UserAgent as u

username = input('username: ')
password = input('Password: ')


ua=u(family='chrome')
hd=ua.random()
x='User-Agent'
hd1={x:f'{hd}'}
hd2=(f'{x}: {hd}')


r = requests.Session()
res = r.get('https://www.instagram.com/', headers=hd1)

payload = {'username':username,'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1254625879:'+password,'queryParams':'{}','optIntoOneTap':'false'}

headers_text = '''Host: www.instagram.com
%s
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRFToken: %s
X-IG-WWW-Claim: 0
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Content-Length: %s
Origin: https://www.instagram.com
Referer: https://www.instagram.com/
Cookie: ig_did=%s; csrftoken=%s; mid=%s
TE: Trailers'''%(hd2,res.cookies['csrftoken'],str(len(urllib.parse.urlencode(payload))),res.cookies['ig_did'],res.cookies['csrftoken'],res.cookies['mid'])

payload_headers = {i.split(': ')[0]:i.split(': ')[1] for i in headers_text.split('\n')}

resp = r.post("https://www.instagram.com/accounts/login/ajax/", headers=payload_headers,data=payload)

if json.loads(resp.text)['authenticated'] == True:
	print('[+] Login successfully!')
	print(json.loads(resp.text))
else:
        print('[!] Login Refused ..')
        print('Bad Password or username')
        print(json.loads(resp.text))
