import requests
import urllib.parse
import json
import time


with open("token.txt", 'r', encoding="utf8") as token_txt:
    summoner_token, summoner_name, exceptions = token_txt.read().split('\n')
exceptions = list(exceptions.replace(' ', '').split(','))
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": summoner_token
}

riot_url1 = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/" + urllib.parse.quote(summoner_name)
res1 = requests.get(riot_url1, headers=custom_headers)
time.sleep(0.05)
summoner_puuid = res1.json()["puuid"]

riot_url2 = "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/" + summoner_puuid + "/ids?count=20"
res2 = requests.get(riot_url2, headers=custom_headers)
time.sleep(0.05)
match_ids = res2.json()

for match_id in match_ids:
    riot_url3 = "https://asia.api.riotgames.com/tft/match/v1/matches/" + match_id
    res3 = requests.get(riot_url3, headers=custom_headers)
    time.sleep(0.05)
    res3 = res3.json()

    with open("bot_players.json", 'r', encoding="utf8") as bot_players_json:
        bot_players = json.load(bot_players_json)

    for player in res3["info"]["participants"]:
        if player["time_eliminated"] < 780:
            riot_url4 = "https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/" + player["puuid"]
            res4 = requests.get(riot_url4, headers=custom_headers)
            time.sleep(0.05)
            player_name = res4.json()["name"].replace(' ', '')
            if (player_name in bot_players
                    and player_name not in exceptions):
                pass
            elif player_name not in exceptions:
                bot_players[player_name] = [player["time_eliminated"]]

    with open("bot_players.json", 'w', encoding="utf8") as bot_players_json:
        json.dump(bot_players, bot_players_json, indent=4, ensure_ascii=False)
        # dump = json.dumps(bot_players, indent=4, ensure_ascii=False)
        # bot_players_json.write(dump)
