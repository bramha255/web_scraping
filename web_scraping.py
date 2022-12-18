import requests
from bs4 import BeautifulSoup

departure = ['Bangalore', 'Chennai']
destination = ['Maldives', 'Thailand']
day = '18'
month = '01'
# in number
year = '2023'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}


# == == == == == == =  "https://holidayz.makemytrip.com/holidays/india/search?depCity=Bangalore&dateSearched=18%2F1%2F2023&dest=Thailand&destValue=Thailand&affiliate=MMT"
# tourist_site = "https://www.trivago.in/en-IN/srl?__wr=21&iViewType=0&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&search=200-64991;dr-20190417-20190418;rc-1-2;so-0"
# tourist_site = str(
#     f"https://holidayz.makemytrip.com/holidays/india/search?depCity={departure[0]}&dateSearched={day}%2F{month}%2F{year}&dest={destination[0]}&destValue={destination[0]}&affiliate=MMT")
tourist_site = "https://www.google.com/travel/hotels/Google%20Park%20Ventures?q=google%20thailand%20hotel&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4308227%2C4597339%2C4718358%2C4723331%2C4731329%2C4757164%2C4814050%2C4861688%2C4864715%2C4874190%2C4886082%2C4886480%2C4891509%2C4893075%2C4902277%2C4903082%2C4905351%2C4906050%2C4912819%2C4920622%2C4923195%2C4928751&hl=en-IN&gl=in&cs=1&ssta=1&ts=CAESCgoCCAMKAggDEAAaIAoCGgASGhIUCgcI5g8QDBgUEgcI5g8QDBgVGAEyAhAAKgkKBToDSU5SGgA&rp=EIu34aqForiEARDGisyroI-Aw2AQ-eDEuOiIi_KFARDo4LeOyrWE_gQ4AUAASAKiARRHb29nbGUgUGFyayBWZW50dXJlc5oCAggA&ap=aAE&ictx=1&sa=X&ved=0CAAQ5JsGahcKEwigwfGMiP77AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls"


def getdata(url):
    html = requests.get(url, headers=HEADERS)
    print(html)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


soup = getdata(tourist_site)

lists = soup.find('div', class_="GyAeWb")

print(lists)


# graphlabel = soup.find_all(
#     'div', class_="uk-margin-top graph-grid")

# script_list = []
# for i in graphlabel:
#     graphdata = i.find_all('script', class_=False)
#     # since the script we are looking for <script> that dont have class
#     for j in graphdata:
#         list = j.find(text=lambda text: text and "renderChart" in text)
#         script_list.append(list)
#         for k in script_list:
#             print(k.split('\n'), '\n')
#             print('New line')

# we are collecting all the content inside the script as list - I dont think this is the best thing we can do but lets use
# till we find a good alternative
