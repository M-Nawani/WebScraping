import requests
import smtplib
from bs4 import BeautifulSoup

EMAIL_SENDER = "inserttestemailhere"
EMAIL_RECEIVER = "inserttestemailhere"
SENDER_PASSWORD = "inserttestpasswordhere"

URL = "https://www.amazon.in/s?k=kindle&crid=GWEKJQ0PFZ50&sprefix=%2Caps%2C2146&ref=nb_sb_noss"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.51 Safari/537.36}",
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
amazon_html = response.text
soup = BeautifulSoup(amazon_html, "html.parser")
product_price = soup.find(name="span", class_="a-price-whole")
price = product_price.getText()
updated_price = int(price.replace(",", ""))
if updated_price <= 8000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_SENDER, password=SENDER_PASSWORD)
        connection.sendmail(from_addr=EMAIL_SENDER,
                            to_addrs=EMAIL_RECEIVER,
                            msg=f"Subject:ALERT: Kindle Price Drop!!\n\nKindle's price is now {updated_price}")
