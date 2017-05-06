import catgodbotlib
import threading
import time
from datetime import date
import datetime
import pandas as pd
import bs4 as bs
import requests

TOKEN = ''
CHAT_FOR_LOGS = 0

bot = catgodbotlib.Bot(TOKEN, default_parse_mode='HTML')


def get_scores(delta=1):
    log_it('begin get_scores')
    day = (date.today() - datetime.timedelta(delta)).strftime("%Y%m%d")
    link = 'http://www.espn.com/nba/schedule/_/date/' + day
    print(link)

    sauce = requests.get(link).text
    soup = bs.BeautifulSoup(sauce, 'lxml')
    game_links = soup.find_all('a', {'name': '&lpos=nba:schedule:score'})

    overall = ''
    game_number = 1
    for game_link in game_links:
        url = 'http://www.espn.com' + str(game_link['href']).replace('game', 'boxscore', 1)
        dfs = pd.read_html(url)
        overall += '/game{} {} {}:{} {}\n'.format(game_number,
                                                  dfs[0].loc[0][0], dfs[0].loc[0]['T'],
                                                  dfs[0].loc[1]['T'], dfs[0].loc[1][0])
        game_number += 1

    log_it('end get_scores')
    if overall == '':
        return get_scores(delta + 1)
    else:
        return overall


def get_schedule():
    log_it('begin get_schedule')
    day = date.today().strftime("%Y%m%d")
    link = 'http://www.espn.com/nba/schedule/_/date/' + day
    print(link)

    sauce = requests.get(link).text
    soup = bs.BeautifulSoup(sauce, 'lxml')
    tds = soup.find_all('td')
    if tds[0].text == 'No games scheduled':
        return 'No games scheduled for today'

    data = pd.read_html(link)

    schedule = ''
    for i in range(0, len(data[0]), 2):
        schedule += '{} @ {}\n'.format(data[0].loc[i][0].split()[-1], data[0].loc[i][1].split()[-1])

    log_it('end get_schedule')
    return schedule


def update_info():
    log_it('begin update_info')
    global scores, schedule, bot
    while True:
        scores = get_scores()
        schedule = get_schedule()
        log_it('end update_info')
        time.sleep(3600)


def log_it(message):
    print(message)
    bot.send_message(CHAT_FOR_LOGS, message)


request = bot.get_me()
result = request['result']
log_it('Username: @{}\nName: {}\nid: {}'.format(result['username'], result['first_name'], result['id']))

last_handled_update = bot.get_updates()[-1].update_id
log_it('Last handled update: {}'.format(last_handled_update))

scores = ''
schedule = ''

print('------\n')

threading.Thread(target=update_info, args=()).start()

while True:
    request = bot.get_updates()
    result = None if len(request) == 0 else request

    for update in result:
        if update.update_id > last_handled_update:
            if 'message' in update.__dict__:
                if 'text' in update.message.__dict__:
                    message = update.message
                    log = '{}@{}({}): "{}"'.format(message.sender.username,
                                                   message.chat.username if message.chat.type == 'private' else message.chat.title,
                                                   message.chat.id,
                                                   message.text)
                    log_it(log)

                    if '/scores' in message.text:
                        bot.send_message(message.chat.id, scores)

                        log = 'Scores sent to {}'.format(
                            message.chat.username if message.chat.type == 'private' else message.chat.title)
                        log_it(log)

                    if '/schedule' in message.text:
                        bot.send_message(message.chat.id, schedule)

                        log = 'schedule sent to {}'.format(
                            message.chat.username if message.chat.type == 'private' else message.chat.title)
                        log_it(log)
                    print('------\n')

                    last_handled_update = update.update_id
