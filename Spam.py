import httpx,json,os,datetime,random,threading
from fake_useragent import UserAgent
clr_yellow  = '\033[33m'
clr_cyan    = '\033[36m'
clr_blue    = '\033[34m'
clr_green   = '\033[32m'
clr_magenta = '\033[35m'
clr_red     = '\033[31m'
clr_reset   = '\033[39m'
os.system("cls||clear")



asci =  clr_magenta + f"""
                                             
      _____ ______   ___________ _____   ______
     /     \ ____ \ /  ___/____ \ __  \ /      \ 
    |  | |  \  |_\ \ ___ \|  |_\ \/ __ \_  | |  \ 
    |__|_|  /   ___/____  \   ___/____  /__|_|  /
          \/|__|        \/|__|        \/      \/ 
{clr_reset}
"""
timec = datetime.datetime.now().strftime("%D:%M:%S")
print(asci)
cookie = input(f"({clr_magenta}-{clr_reset}) Cookie: ")
xsrf = input(f"({clr_magenta}-{clr_reset}) Token: ")
os.system("cls||clear")
agent = UserAgent().chrome
headers = {
    "authority": "www.marktplaats.nl",
    "method": "POST",
    #"path": f"/messages/api/conversations/{channel_id}/message",
    "scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "cookie": f"{cookie}",
    "origin": "https://www.marktplaats.nl",
    "referer": "https://www.marktplaats.nl/messages/2thh:208pbl8:2hsxhlw7l",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": str(agent),
    "x-mp-xsrf": f"{xsrf}",
}



class main():
    

    def inputs():
        global channel_id,message
        
        print(asci)
        channel_id = input(f"({clr_magenta}-{clr_reset}) Channel ID: ")
        message = input(f"({clr_magenta}-{clr_reset}) Message: ")
        threads = input(f"({clr_magenta}-{clr_reset}) Threads: ")
        for i in range(int(threads)):
            threading.Thread(target=main.requests).start()


    def requests():
        while True:
            try:
                proxylist = open("proxies.txt", "r").read().splitlines()
                proxy = random.choice(proxylist)
                proxies = {
                    "http://": f"http://{proxy}",
                    "https://": f"http://{proxy}",
                }
                payload = {
                    "text": f"{message} | {random.randint(1000,3000)}" 
}
                with httpx.Client(proxies=proxies) as client:
                    x = client.post(f"https://www.marktplaats.nl/messages/api/conversations/{channel_id}/message", headers=headers, json=payload)
                    if x.status_code == 200:
                        print(f"({clr_magenta}+{clr_reset}) Message Sent {clr_magenta}|{clr_reset}{timec}{clr_magenta}|{clr_reset}")
                    else:
                        print(f"({clr_red}-{clr_reset}) failed: ", x.text)
                
            except Exception as err:
                print(err)


main.inputs()
