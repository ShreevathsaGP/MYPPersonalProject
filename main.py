import mysql.connector
from flask import Flask, render_template, url_for, redirect, request
from bs4 import BeautifulSoup
import requests
import time
import random
from password import password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome
from tabulate import tabulate
import pandas as pd
import datetime

search_quereies = []

Snapdeal_Names = []
Snapdeal_Prices = []
Snapdeal_imagelinks = []
Snapdeal_Prices_2 = []

Flipkart_Names = []
Flipkart_Prices = []
Flipkart_Prices_2 = []
Flipkart_ImageLinks = []

Amazon_Names = []
Amazon_Prices = []
Amazon_Prices_2 = []
Amazon_ImageLinks = []


def clear(list):
    list.clear()


clear(search_quereies)

clear(Snapdeal_Names)
clear(Snapdeal_Prices)
clear(Snapdeal_Prices_2)
clear(Snapdeal_imagelinks)

clear(Flipkart_Names)
clear(Flipkart_Prices)
clear(Flipkart_Prices_2)
clear(Flipkart_ImageLinks)

clear(Amazon_Names)
clear(Amazon_Prices)
clear(Amazon_Prices_2)
clear(Amazon_ImageLinks)


time_variable = random.uniform(0,0)

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd=str(password),
                               database="scrape_database")
print(mydb)
cursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['u']
    processed_text = text.lower()

    search_quereies.append(processed_text)

    if len(search_quereies) >= 1:

        Product_search = search_quereies[0]

        def Integrated():
            def Amazon():
                time.sleep(time_variable)
                URL = "https://www.amazon.in/s?k=" + str(Product_search) + "&ref=nb_sb_noss_2"
                headers = {
                    'authority': 'www.amazon.in',
                    'cache-control': 'max-age=0',
                    'rtt': '50',
                    'downlink': '10',
                    'ect': '4g',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    'sec-fetch-user': '?1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'referer': 'https://www.amazon.in/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,nl;q=0.7',
                    'cookie': 'session-id=258-1636592-3456905; i18n-prefs=INR; ubid-acbin=257-5529898-5487600; x-wl-uid=1ir5E8+OGhMOBpYNk5vAaB/JiH6qK69EwafO54hquG79/1zQlrhpNsM5nmNrkgP7e/m69DA9SWNY=; lc-acbin=en_IN; session-token=RNXDMxPntpb6YB4qLb/SPv+B2D0zCLft5u0EuG4qsBl5C7QyxS8Vu28Sm2iu9j1LS73JtkQsBpHnu6bYxStohPe6gNbEvpgHsJ7m8ld188mgFVDm8Wtjri7Iaq9R5TvjF4zgFmwEP21zD9hf8zmSmODV/8yDxYZ5lTS5McKbQossGXMLNLHZxSopMuq3jN4A; visitCount=28; session-id-time=2082758401l; csm-hit=tb:s-D9EHD2TB6FW1FS29NDVB|1577817064939&t:1577817066038&adb:adblk_yes',
                }
                time.sleep(time_variable)

                try:
                    recieve = requests.get(URL, headers=headers, timeout=10)
                except:
                    "One or more of the websites are unresponsive, please retry later."
                    exit()

                soup = BeautifulSoup(recieve.content, 'html.parser')

                def initial_viability_test():
                    test_count = 0
                    The_Whole_Page = soup.prettify()
                    while test_count < 2:
                        print(The_Whole_Page)
                        test_count += 1
                        time.sleep(time_variable)

                def name_scrape():
                    time.sleep(time_variable)

                    outlines = soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"})

                    for outline in outlines:
                        name = outline.text
                        Amazon_Names.append(name)

                    if len(Amazon_Names) is 0:
                        outlines_2 = soup.findAll("span", {"class": "a-size-base-plus a-color-base a-text-normal"})

                        for outline_2 in outlines_2:
                            name_2 = outline_2.text
                            Amazon_Names.append(name_2)

                    # print(Amazon_Names)

                def price_scrape():
                    time.sleep(time_variable)

                    outlines = soup.findAll("span", {"class": "a-price-whole"})

                    for x in range(len(outlines)):
                        outline = outlines[x]
                        price = outline.text
                        Amazon_Prices.append(price)

                    # print(Amazon_Prices)

                def image_scrape():
                    time.sleep(time_variable)
                    outlines = soup.findAll("img", {"class": "s-image"})

                    for x in outlines:
                        image_link = x['src']
                        Amazon_ImageLinks.append(image_link)

                    # print(Amazon_ImageLinks)

                    # print(outlines)

                # initial_viability_test()
                name_scrape()
                price_scrape()
                image_scrape()

            def Snapdeal():
                try:
                    retrieve = requests.get(
                        "https://www.snapdeal.com/search?keyword=" + str(Product_search) + "&sort=plrty", timeout=2)
                except:
                    "One or more of the websites are unresponsive, please retry later."
                    exit()

                retrieve = retrieve.text

                data = BeautifulSoup(retrieve, 'lxml')

                def initial_viability_test():
                    time.sleep(time_variable)
                    test_count = 0
                    The_Whole_Page = data.prettify()
                    while test_count <= 100:
                        print(The_Whole_Page)
                        test_count += 1

                def name_scrape():
                    time.sleep(time_variable)
                    names = data.select('.product-desc-rating')
                    for name in names:
                        product_identification = name.select('.product-title ')
                        product_name = product_identification[0].getText()

                        Snapdeal_Names.append(product_name)
                    # print(Snapdeal_Names)

                def price_scrape():
                    time.sleep(time_variable)
                    prices = data.select('.product-desc-rating')
                    for price in prices:
                        price_identification = price.find_all('span', 'lfloat product-price')
                        price_values = price_identification[0].getText()

                        Snapdeal_Prices.append(price_values)

                    for x in range(len(Snapdeal_Prices)):
                        Snapdeal_Prices[x].strip()
                    # print(Snapdeal_Prices)

                def image_scrape():
                    time.sleep(time_variable)
                    images = data.select('.picture-elem')

                    for x in images:
                        image = x.find_all('img')
                        for y in image:
                            image = y.get('data-src')
                            Snapdeal_imagelinks.append(image)

                    # print(Snapdeal_imagelinks)

                name_scrape()
                price_scrape()
                image_scrape()

                # for x in range(len(Snapdeal_Names)):
                # output = "Name:" + str(Snapdeal_Names[x]) + ", Price:" + str(Snapdeal_Prices[x]) + ", Image:" + str(Snapdeal_imagelinks[x])
                # print(output)

            def Flipkart():
                headers = {
                    'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    'Sec-Fetch-User': '?1',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,nl;q=0.7',
                }

                URL = "https://www.flipkart.com/search?q=" + str(
                    Product_search) + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

                try:
                    recieve = requests.get(URL, headers=headers)
                    recieve = recieve.text

                except:
                    options = Options_Chrome()
                    options.headless = True
                    browser = webdriver.Chrome(options=options)
                    browser.get(URL)
                    time.sleep(60)
                    recieve = browser.page_source
                    browser.close()

                soup = BeautifulSoup(recieve, 'lxml')

                def initial_viability_test():
                    test_count = 0
                    The_Whole_Page = soup.prettify()
                    while test_count <= 100:
                        print(The_Whole_Page)
                        test_count += 1

                def name_scrape():
                    time.sleep(time_variable)
                    outlines = soup.findAll("div", {"class": "_1UoZlX"})

                    for x in range(len(outlines)):
                        outline = outlines[x]
                        identify = outline.find("div", {"class": "_3wU53n"})
                        name = identify.text
                        Flipkart_Names.append(name)

                    if len(Flipkart_Names) is 0:
                        outlines_2 = soup.findAll("div", {"class": "_3liAhj"})

                        for y in range(len(outlines_2)):
                            outline_2 = outlines_2[y]
                            identify_2 = outline_2.find("a", {"class": "_2cLu-l"})
                            name_2 = identify_2.text
                            Flipkart_Names.append(name_2)
                    else:
                        pass
                    # print(Flipkart_Names)

                def price_scrape():
                    time.sleep(time_variable)
                    outlines = soup.findAll("div", {"class": "_1UoZlX"})

                    for x in range(len(outlines)):
                        outline = outlines[x]
                        identify = outline.find("div", {"class": "_1vC4OE _2rQ-NK"})
                        price = identify.text
                        Flipkart_Prices.append(price)

                    if len(Flipkart_Prices) is 0:
                        outlines_2 = soup.findAll("div", {"class": "_3liAhj"})

                        for y in range(len(outlines_2)):
                            outline_2 = outlines_2[y].find("div", {"class": "_1vC4OE"})
                            price_2 = outline_2.text
                            Flipkart_Prices.append(price_2)

                    else:
                        pass
                    # print(Flipkart_Prices)

                def image_scrape():
                    time.sleep(time_variable)
                    outlines = soup.findAll("div", {"class": "_1UoZlX"})

                    for x in range(len(outlines)):
                        outline = outlines[x]
                        identify = outline.find("div", {"class": "_3BTv9X"})
                        image = identify.find("img")
                        image_link = image['src']
                        Flipkart_ImageLinks.append(image_link)

                    if len(Flipkart_ImageLinks) is 0:
                        outlines_2 = soup.findAll("div", {"class": "_3liAhj"})

                        for y in range(len(outlines_2)):
                            outline_2 = outlines_2[y]
                            identify_2 = outline_2.find("div", {"class": "_3BTv9X"})
                            image_2 = identify_2.find("img")
                            image_link_2 = image_2['src']
                            Flipkart_ImageLinks.append(image_link_2)

                    else:
                        pass
                    # print(Flipkart_ImageLinks)

                name_scrape()
                price_scrape()
                image_scrape()
                # initial_viability_test()

            Amazon()
            Flipkart()
            Snapdeal()

        Integrated()

        def Data():
            for price in Snapdeal_Prices:
                updated_price = price.strip("Rs. ")
                updated_price_2 = updated_price.replace(",", "")
                Snapdeal_Prices_2.append(updated_price_2)

            for price in Flipkart_Prices:
                price_2 = price.strip("₹")
                price_3 = price_2.replace(",", "")
                Flipkart_Prices_2.append(price_3)

            for price in Amazon_Prices:
                comma_less = price.replace(",", "")
                Amazon_Prices_2.append(comma_less)

        def SQL():
            def create_tables():

                # If you want to change the settings of a table you must use --> "ALTER TABLE x

                try:
                    cursor.execute("CREATE TABLE snapdeal (name TEXT, price INTEGER(20), image TEXT)")
                except:
                    "Table already created"

                try:
                    cursor.execute("CREATE TABLE flipkart (name TEXT, price INTEGER(20), image TEXT)")
                except:
                    "Table already created"

                try:
                    cursor.execute("CREATE TABLE amazon (name TEXT, price INTEGER(20), image TEXT)")
                except:
                    "Table already created"

            def insert_data():

                def snapdeal():
                    sqlFormula = "INSERT INTO snapdeal (name, price, image) VALUES (%s, %s, %s)"
                    data = []

                    for x in range(len(Snapdeal_Names)):
                        data_installment = (Snapdeal_Names[x], Snapdeal_Prices_2[x], str(Snapdeal_imagelinks[x]))
                        data.append(data_installment)

                    try:
                        cursor.execute("TRUNCATE TABLE snapdeal")
                    except:
                        print("Table already empty")

                    print(data)

                    try:
                        cursor.executemany(sqlFormula, data)
                    except:
                        print("YOU FAILED")
                    mydb.commit()

                def flipkart():
                    sqlFormula = "INSERT INTO flipkart (name, price, image) VALUES (%s, %s, %s)"
                    data = []

                    for x in range(len(Flipkart_Names)):
                        data_instance = (Flipkart_Names[x], Flipkart_Prices_2[x], str(Flipkart_ImageLinks[x]))
                        data.append(data_instance)

                    try:
                        cursor.execute("TRUNCATE TABLE flipkart")
                    except:
                        print("Table already empty")

                    print(data)
                    try:
                        cursor.executemany(sqlFormula, data)
                    except:
                        print("YOU FAILED")
                    mydb.commit()

                def amazon():
                    sqlFormula = "INSERT INTO amazon (name, price, image) VALUES (%s, %s, %s)"
                    data = []

                    upper_limit = [len(Amazon_Prices_2), len(Amazon_ImageLinks), len(Amazon_Names)]
                    upper_limit.sort()

                    limit = min(upper_limit)

                    for x in range(limit):
                        data_instance = (Amazon_Names[x], Amazon_Prices_2[x], str(Amazon_ImageLinks[x]))
                        data.append(data_instance)

                    try:
                        cursor.execute("TRUNCATE TABLE amazon")
                    except:
                        print("Table already empty")

                    print(data)
                    try:
                        cursor.executemany(sqlFormula, data)
                    except:
                        print("YOU FAILED")

                    mydb.commit()

                snapdeal()
                flipkart()
                amazon()

            create_tables()
            insert_data()

        Data()
        SQL()

        def clear(list):
            list.clear()

        clear(search_quereies)

        clear(Snapdeal_Names)
        clear(Snapdeal_Prices)
        clear(Snapdeal_Prices_2)
        clear(Snapdeal_imagelinks)

        clear(Flipkart_Names)
        clear(Flipkart_Prices)
        clear(Flipkart_Prices_2)
        clear(Flipkart_ImageLinks)

        clear(Amazon_Names)
        clear(Amazon_Prices)
        clear(Amazon_Prices_2)
        clear(Amazon_ImageLinks)

        flipkart_upload = []
        amazon_upload = []
        snapdeal_upload = []

        cursor.execute("SELECT * FROM scrape_database.flipkart")
        my_results = cursor.fetchall()

        for result in my_results:
            flipkart_upload.append(result)

        cursor.execute("SElECT * FROM scrape_database.amazon")
        my_results_2 = cursor.fetchall()

        for result in my_results_2:
            amazon_upload.append(result)

        cursor.execute("SELECT * FROM scrape_database.snapdeal")
        my_results_3 = cursor.fetchall()

        for result in my_results_3:
            snapdeal_upload.append(result)

        #print(flipkart_upload)
        #print(amazon_upload)
        #print(snapdeal_upload)

        return render_template("result.html", flipkart=flipkart_upload, amazon=amazon_upload, snapdeal=snapdeal_upload)

    else:
        print("The user messed something up.")
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
