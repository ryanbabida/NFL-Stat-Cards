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


def getStats(url, pos):
    stats = list()
    per_game = list()
    i = 0
    game_count = 0
    pos_int = getPosInt(pos)

    player_req = requests.get(url)
    player_soup = BeautifulSoup(player_req.content, 'lxml')
    for link in player_soup.findAll('td'):
        if (link.text.isdigit() or link.text == '--' or 
                link.text.find(',') != -1  or link.text.find('.') != -1 
                or link.text.find('-') == 0 or link.text == 'TOTAL'):
            per_game.append(link.text)
            i = i + 1
        s = link.text
        if link.text.find('T') == 2 or link.text.find('T') == 1:
            per_game.append(link.text)
            i = i + 1
        if i == pos_int:
            stats.append(per_game[:])
            per_game.clear()
            i = 0

    return stats


def getPosInt(pos):
    if pos == 'QB':
        return 19
    elif pos == 'RB' or pos == 'TE' or pos == 'WR':
        return 15


def getCategories(pos):
    if pos == 'QB':
        return [ 'Week', 'G', 'GS', 'Comp', 'PAtt', 'PPct',   'PYds',
                   'PAvg', 'PTD', 'Int',    'Sck', 'SckY', 'Rate', 
                   'RAtt', 'RYds', 'RAvg', 'RTD', 'FUM', 'Lost']
    elif pos == 'TE':
        return ['Week', 'G', 'GS', 'Rec', 'RecYds', 'RecAvg', 'RecLng', 
                    'RecTD', 'RAtt', 'RYds', 'RAvg', 
                    'RLng', 'RTD', 'FUM', 'Lost']
    elif pos == 'WR':
        return ['Week', 'G', 'GS', 'Rec', 'RecYds', 'RecAvg', 'RecLng', 
                    'RecTD', 'RAtt', 'RYds', 'RAvg', 
                    'RLng', 'RTD', 'FUM', 'Lost']
    elif pos == 'RB':
        return ['Week', 'G', 'GS', 'RAtt', 'RYds',   'RAvg',
                    'RLng', 'RTD', 'Rec', 'RecYds', 'RecAvg', 'RecLng', 
                    'RecTD','FUM', 'Lost']
    elif pos == 'CB':
        return ['Week']



    

