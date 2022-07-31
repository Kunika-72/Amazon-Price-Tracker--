import bs4
from bs4 import BeautifulSoup
import urllib
import requests
import time
import smtplib

def check_price(url):
    header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept Lang":"en"
    }
    r=requests.get(url,headers=header)
    soup=BeautifulSoup(r.text,"lxml")
    #Finding name
    pname = soup.find("span",id="productTitle").text
    pname =pname.strip()
    #Finding price
    price = soup.find("span",class_="a-offscreen").text
    temp = price[1:].replace(",","")
    price = float(temp)
    return  price




def price_decrease_check(price_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False


def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('receiver@gmail.com', 587)
    s.starttls()
    s.login("sample@gmail.com", "12345")
    s.sendmail("sample@gmail.com", "12345", message)
    s.quit()


price_list = []
#url = input("Enter url ")
url = 'https://www.amazon.in/DIKANG-Octopus-Plushie-Reversible-Plush/dp/B09GYSTYFN?ref_=Oct_d_orecs_d_1378446031&pd_rd_w=LRXwd&content-id=amzn1.sym.621e1bcb-8a01-4ac0-9db2-263e5798bda1&pf_rd_p=621e1bcb-8a01-4ac0-9db2-263e5798bda1&pf_rd_r=NFK4R3B1Q81D9EVB90P2&pd_rd_wg=56zpd&pd_rd_r=71beb01a-2d00-468a-9d33-568335f80289&pd_rd_i=B09GYSTYFN'


count = 1
while True:
    current_price = check_price(url)
    price_list.append(current_price)

    if count > 1:
        flag = price_decrease_check(price_list)
        if flag:
            decrease = price_list[-1] - price_list[-2]
            message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            send_email(message) #ADD THE OTHER AGRUMENTS sender_email, sender_password, receiver_email
    time.sleep(86400)
    count += 1




