import requests
from bs4 import BeautifulSoup
from kavenegar import *
import smtplib
import time

URL = 'https://www.digikala.com/product/dkp-4418812/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-%D9%85%D8%AF%D9%84-redmi-9t-m2010j19sg-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(attrs='c-product__seller-price-pure js-price-value').get_text().strip()
    replaced_price = price.replace(",", ".")
    converted_price = float(replaced_price[0:5])
    if converted_price < 4.200:
        send_mail()
        send_msg()

    print(converted_price)
    #print(price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('darkrape69@gmail.com', 'rafe1380')

    subject = 'less price Redmi 9t'
    body = 'buy now'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('darkrape69@gmail.com', 'rafeshahraki@gmail.com', msg)
    print("Email Sent")
    server.quit()


def send_msg():
    try:
        api = KavenegarAPI('3059314933335A655274382F6541776F3544454B5759436C63793956627353703479484538685953572F453D')
        params = {'sender': '10008663', 'receptor': '09915734147', 'message': 'رافع: گوشی Redmi 9t ارزان شد.'}
        response = api.sms_send(params)
        print(response)
        print("Msg sent")

    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)


while(True):
    check_price()
    time.sleep(60*5)