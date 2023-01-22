import requests
import random
import string
import time
import re

def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

a = int(input("Masukan Jumlah Reff: "))
x = 0
uuid = open("uuid.txt", "r").readlines()
for line in uuid:
    udin = line.split("\n")
    uuid = udin[0]
    for i in range(a):
    #GENERATE USERNAME
        name = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(name) for i in range(10))

    #RANDOM DOMAIN
        API = 'https://www.1secmail.com/api/v1/'
        domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
        domain = random.choice(domainList)

    #GET NEW MAIL
        newMail = f'{API}?login='+username+'&domain='+domain
        reqMail = requests.get(newMail)
        mail = f"{extract()[0]}@{extract()[1]}"

        print("[EMAIL] "+mail)

    #DAFTAR
        ngen = "https://user.atlasvpn.com/v1/request/join"
        headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Origin": "https://account.atlasvpn.com", "Referer": "https://account.atlasvpn.com/", "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "X-Client-Id": "Web", "Content-Type": "application/json;charset=UTF-8"}
        json={"email": ""+mail+"", "marketing_consent": True, "referral_offer": "initial", "referrer_uuid": ""+uuid+""}
        tod  = requests.post(ngen, headers=headers, json=json)
        print("[RESPONSE REGIST] "+str(tod))
        time.sleep(2)
        print("[GET CODE]")
        reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
        req = requests.get(reqLink).json()
        length = len(req)
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'textBody':
                    content = v
            data = re.search('token=(.*) ', content).group(1)
            sms = data
            print(data)
        print("[SUCCES GET CODE]")
        print("[LANJUT DAFTAR]")
        ngen = "https://user.atlasvpn.com/v1/auth/confirm"
        tod = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer "+str(data)+"", "Origin": "https://account.atlasvpn.com", "Referer": "https://account.atlasvpn.com/", "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
        ahh = requests.get(ngen, headers=tod)
        print("[RESPONSE LOGIN] "+str(ahh))
        x+=1
        print("[+]==============[DONE REFF "+str(x)+"]==============[+]\n")
    