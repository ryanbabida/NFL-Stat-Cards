import requests
from bs4 import BeautifulSoup
import re
import urllib.request

def search(name):
    results = dict()
    url = ('http://www.nfl.com/players/search?category=name&filter=' + str(name) 
    + '&playerType=current')
    search_req = requests.get(url)
    soup_req = BeautifulSoup(search_req.content, 'lxml')
    for link in soup_req.findAll('a', attrs={'href': re.compile("/player/")}):
        results.update({link.text : "http://www.nfl.com" + link.get('href')})
    return results


def getLog(url):
    player_req = requests.get(url)
    player_soup = BeautifulSoup(player_req.content, 'lxml')
    for link in player_soup.findAll('a', attrs={'href': re.compile("/gamelogs")}):
        return "http://www.nfl.com" + link.get('href')


def getPos(url):
    player_req = requests.get(url)
    player_soup = BeautifulSoup(player_req.content, 'lxml')
    for link in player_soup.findAll('span'):
        if link.text.find('#') == 0:
            return link.text.split()


def getTeam(url):
    player_req = requests.get(url)
    player_soup = BeautifulSoup(player_req.content, 'lxml')
    for link in player_soup.findAll('a', attrs={'href': re.compile("/teams")}):
        return link.text

def getImg(url):
    player_req = requests.get(url)
    player_soup = BeautifulSoup(player_req.content, 'lxml')
    for link in player_soup.findAll('img'):
        if link.get('src').find('200x200') != -1:
           return link.get('src')

