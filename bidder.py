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
timec = datetime.datetime.now().strftime("%M:%S")
cookie = input(f"({clr_magenta}-{clr_reset}) Cookie: ")
xsrf = input(f"({clr_magenta}-{clr_reset}) Token: ")


class code():

    def main():
        global headers,bod,item_id,message,link
        asci =  clr_magenta + f"""
                                                    
              _____ ______   ___________ _____   ______
             /     \ ____ \ /  ___/____ \ __  \ /      \ 
            |  | |  \  |_\ \ ___ \|  |_\ \/ __ \_  | |  \ 
            |__|_|  /   ___/____  \   ___/____  /__|_|  /
                  \/|__|        \/|__|        \/      \/ 
        {clr_reset}
        """
        print(asci)
        link = input(f"({clr_magenta}-{clr_reset}) Link: ")
        bod = input(f"({clr_magenta}-{clr_reset}) Bod: €")
        item_id = input(f"({clr_magenta}-{clr_reset}) Item ID: ")
        message = input(f"({clr_magenta}-{clr_reset}) Bericht: ")
        threads = input(f"({clr_magenta}-{clr_reset}) Threads: ")
        for i in range(int(threads)):
            threading.Thread(target=code.requests).start()


    def requests():
        while True:
            try:
                agent = UserAgent().chrome
                headers = {
                    "authority": "www.marktplaats.nl",
                    "method": "POST",
                    "scheme": "https",
                    "accept": "application/json",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                    "content-type": "application/json",
                    "cookie": f"{cookie}",
                    "origin": "https://www.marktplaats.nl",
                    "referer": f"{link}",
                    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": str(agent),
                    "x-mp-xsrf": f"{xsrf}",
                }
                proxylist = open("proxies.txt", "r").read().splitlines()
                proxy = random.choice(proxylist)
                proxies = {
                    "http://": f"http://{proxy}",
                    "https://": f"http://{proxy}",
                }
                payload = {
                    "bidAmountCents": f"{bod}",
                    "itemId": f"{item_id}",
                    "message": f"{message}",
                    "phoneNumber": ""
                }
                with httpx.Client(proxies=proxies) as client:
                    x = client.post("https://www.marktplaats.nl/v/api/place-bid", headers=headers, json=payload)
                    if x.status_code == 200:
                        print(f"({clr_magenta}+{clr_reset}) Bid Sent {clr_magenta}€{clr_reset}{bod}  {clr_magenta}|{clr_reset}{timec}{clr_magenta}|{clr_reset}")
                    else:
                        print(f"({clr_red}-{clr_reset}) failed: ", x.text)

            except Exception as err:
                print(err)

code.main()
