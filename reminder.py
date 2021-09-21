#!/usr/bin/env python3

import datetime, requests, json

with open('config.json', 'r') as config_file:
    # load config
    config = json.load(config_file)
    spreadsheet_id = config['spreadsheet_id']
    spreadsheet_api_key = config['spreadsheet_api_key']
    discord_webhook_url = config['discord_webhook_url']

    spreadsheet_api_metadata = 'https://sheets.googleapis.com/v4/spreadsheets/' + spreadsheet_id + '/'
    spreadsheet_api_values = 'https://sheets.googleapis.com/v4/spreadsheets/' + spreadsheet_id + '/values/'

    params_of_get = {'key': spreadsheet_api_key}

    response = requests.get(spreadsheet_api_metadata, params=params_of_get)

    spreadsheet_info = json.loads(response.text)

    today = datetime.datetime.today()
    today_str = str(today.month) + '/' + str(today.day)

    for sheet in spreadsheet_info['sheets']:
        sheet_title = sheet['properties']['title']
        response = requests.get(spreadsheet_api_values + sheet_title + '!A:Z', params=params_of_get)
        schedule = json.loads(response.text)

        if 'values' in schedule.keys():
            for row in schedule['values']:
                if len(row) < 4:
                    continue

                if row[1] == today_str and row[3] == '有り':

                    payload = {
                            'content': '今日（' + today_str + '）は' + row[0] + '日クポ。\n特記事項: ' + row[12]
                    }
                    response = requests.post(discord_webhook_url, data=payload)

