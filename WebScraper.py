import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def create_soup(url):
    page = urllib.request.urlopen(url)
    link = BeautifulSoup(page, 'html.parser')
    return link

soup = create_soup('https://www.hockey-reference.com/leagues/NHL_2022_skaters.html#stats::points')

def get_data():
    '''

    Gets the real time stats of every NHL player who has played a game in the current NHL season and saves it to
    nhl_stats.csv

    '''

    all_data = ""
    for records in soup.select('tr[class!="over_header"]'):
        team_data = ""
        for data in records.findAll('td'):
            team_data = team_data + "," + data.text
        all_data = all_data + '\n' + team_data[1:]

    headers = "Rk,Player,Age,Tm,Pos,GP,G,A,PTS,+/-,PIM,PS,EV,PP,SH,GW,EV,PP,SH,S,S%,TOI,ATOI,BLK,HIT,FOW,FOL,FO%"
    file=open(os.path.expanduser('nhl_stats.csv'), 'wb')
    file.write(bytes(headers, encoding='ascii', errors='ignore'))
    file.write(bytes(all_data, encoding='ascii', errors='ignore'))




