import catgodbotlib
import threading
import time
import pandas as pd


def get_scores():
    link = 'http://www.espn.com/nba/schedule/_/date/20170422'
    data = pd.read_html(link)

    scores = ''
    for i in range(0, len(data[0]), 2):
        scores += '{}\n'.format(data[0].loc[i]['result'])

    return scores


def get_schedule():
    link = 'http://www.espn.com/nba/schedule/_/date/20170422'
    data = pd.read_html(link)

    schedule = ''
    for i in range(0, len(data[1]), 2):
        schedule += '{} @ {}\n'.format(data[1].loc[i][0].split()[0], data[1].loc[i][1].split()[0])

    return schedule


def update_info():
    global scores, schedule
    while True:
        scores = get_scores()
        schedule = get_schedule()
        print('---\nInfo updated\n---')
        time.sleep(300)

scores = get_scores()
schedule = get_schedule()
print('---\nInfo updated\n---')

TOKEN = '341653921:AAEd3_iWZSby16uHaT1we17E0lIw4Pv9IXg'

bot = catgodbotlib.Bot(TOKEN, default_parse_mode='HTML')

request = bot.get_me()
result = request.json()['result']
print('Username: @{}\nName: {}\nid: {}'.format(result['username'], result['first_name'], result['id']))

last_handled_update = bot.get_updates().json()['result'][-1]['update_id']
print('Last handled update: {}'.format(last_handled_update))

print('------\n')

threading.Thread(target=update_info, args=()).start()

while True:
    request = bot.get_updates()
    result = request.json()['result']

    for update in result:
        if update['update_id'] > last_handled_update:
            message = update['message']
            print('@{}@{} "{}"'.format(message['from']['username'],
                                       message['chat']['username' if message['chat']['type'] == 'private' else 'title'],
                                       message['text']))

            if '/scores' in message['text']:
                bot.send_message(message['chat']['id'], scores)
                print('Scores sent to {}'.format(message['from']['username']))

            if '/schedule' in message['text']:
                bot.send_message(message['chat']['id'], schedule)
                print('Schedule sent to {}'.format(message['from']['username']))
            print('------\n')

            last_handled_update = update['update_id']