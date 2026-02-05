import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os


def send_mail(title, price, page) :
    """this function will create the secure connection between sender and receiver using smtp module  and send the mail whenever price goes beyond the certain amount of product."""

    EMAIL_ADDRESS = os.environ["my_email"]
    EMAIL_PASSWORD = os.environ["password"]
    SMTP_ADDRESS = os.environ["smtp_server"]

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with SMTP(SMTP_ADDRESS, smtp_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS, msg=f"Subject: Amazon Price Alert!\n\n {title.encode(encoding='utf-7')} INR{price}\n {page}")


url = f"https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
"Priority": "u=0, i",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
}


# requests
response = requests.get(url, headers= header)
product_webpage = response.text

# soup
soup = BeautifulSoup(product_webpage, "html.parser")
product_price = soup.find_all(name="span", class_ = "a-price-whole")
product_title = soup.find_all(name="span", class_ = "a-size-large product-title-word-break")
product_page  = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

amazon_price = product_price[0].text.replace(",", "") # this wil remove ","
amazon_price  = int(amazon_price.split(".")[0]) # this will split the the number

lowest_price = 9000

# this will remove the unwanted things from the title
title_list = [title.text.split("\r\n                                        ") for title in product_title]

title_string = ""
for str in title_list[0]:
    title_string += str

# if current price is lower than this price than this function get called and email get send on provided email ID
if amazon_price < lowest_price:
    send_mail(title_string, amazon_price, product_page)






