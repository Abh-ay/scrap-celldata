

from urllib import response
from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
urlmi = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi&page=1"
urloppo = "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3D15000&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=sort%3Dpopularity&sid=tyy%2F4io&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk9wcG8gTW9iaWxlcyB1bmRlciDigrkyMEsiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=3.productCard.PMU_V2_3&page=1"
urlsamsung = "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1&page=1"
urlvivo = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DVivo&otracker=nmenu_sub_Electronics_0_Vivo&page=1"
urlrealme = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&page=1"


url_list = [urlmi, urloppo, urlsamsung, urlvivo, urlrealme]
company_list = ["mi", "oppo", "samsung", "vivo", "realme"]
page_count = []


def getPageCount(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    element = soup.find('div', attrs={'class': '_2MImiq'})
    page_count.append(int(element.span.text[10:len(element.span.text)]))


sumi = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi&page={pc}"
suoppo = "https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3D15000&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=sort%3Dpopularity&sid=tyy%2F4io&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk9wcG8gTW9iaWxlcyB1bmRlciDigrkyMEsiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=3.productCard.PMU_V2_3&page={pc}"
susamsung = "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1&page={pc}"
suvivo = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DVivo&otracker=nmenu_sub_Electronics_0_Vivo&page={pc}"
surealme = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&page={pc}"

scrap_url_list = [sumi, suoppo, susamsung, suvivo, surealme]
for i in range(0, len(url_list)):
    getPageCount(url_list[i])


conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

# c.execute('''DROP TABLE flipkartcelldata''')
c.execute('''CREATE TABLE flipkartcelldata(site TEXT,company TEXT,title TEXT,price REAL,ratingreview TEXT,url TEXT,status TEXT,redirect_url TEXT)''')

for i in range(0, len(page_count)):
    print(company_list[i])
    for j in range(1, page_count[i]+1):
        # print(scrap_url_list[i].format(pc=str(j)))
        response = requests.get(scrap_url_list[i].format(pc=str(j)))
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        mainelement = soup.find_all('a', attrs={'class': '_1fQZEK'})
        # NOW MAKING ALL VARIBLE THAT STORE IN A DATABSE
        for ele in mainelement:
            try:
                company = company_list[i]
                title = ele.find(
                    'div', attrs={'class': '_4rR01T'}).text
                print(title)
                price = ele.find(
                    'div', attrs={'class': '_30jeq3 _1_WHN1'}).text
                r_r = ele.find('div', attrs={'class': '_3LWZlK'}).text
                status = ele.find('div', attrs={'class': '_3G6awp'})
                if status == None:
                    status = "Available"
                else:
                    status = status.span.text
                url = ele.find('img', attrs={'class': '_396cs4 _3exPp9'})
                redirect_url="https://www.flipkart.com"+ele['href']
                c.execute('''INSERT INTO flipkartcelldata VALUES(?,?,?,?,?,?,?,?)''',
                          ("flipkart", company, title, price, r_r, url['src'], status,redirect_url))

            except Exception as e:
                print(e)


df = pd.read_sql_query('''select * from flipkartcelldata''', conn)
df.to_csv(r'D:\flipkart\cell.csv')


conn.commit()
# c.execute('''SELECT * FROM celldata''')
# result = c.fetchall()
# print(result)
conn.close()
