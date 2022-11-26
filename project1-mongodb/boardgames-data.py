import pandas as pd
import numpy as np
from pymongo import MongoClient
import json


def mongoimport(csv_path, db_name, coll_name, db_url='localhost', db_port=27017):
    """ Imports a csv file at path csv_name to a mongo colection
        returns: count of the documents in the new collection
    """
    # client = MongoClient(db_url, db_port)
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)

    # ignore unnamed column, type column
    data.drop('Unnamed: 0', inplace=True, axis=1)
    data.drop('type', inplace=True, axis=1)
    data.drop('alternate', inplace=True, axis=1)
    data.drop('suggested_num_players', inplace=True, axis=1)
    data.drop('suggested_playerage', inplace=True, axis=1)
    data.drop('suggested_language_dependence', inplace=True, axis=1)
    data.drop('bayesaverage', inplace=True, axis=1)
    data.drop('stddev', inplace=True, axis=1)
    data.drop('median', inplace=True, axis=1)
    data.drop('wanting', inplace=True, axis=1)

    # rename primary column to title
    data.rename(columns={'primary': 'title'}, inplace=True)

    # if number value is 0, replace with None
    # yearpublished                int64
    # minplayers                   int64
    # maxplayers                   int64
    # playingtime                  int64
    # minplaytime                  int64
    # maxplaytime                  int64
    # minage                       int64
    data['yearpublished'] = data['yearpublished'].replace(0, np.nan)
    data['minplayers'] = data['minplayers'].replace(0, np.nan)
    data['maxplayers'] = data['maxplayers'].replace(0, np.nan)
    data['playingtime'] = data['playingtime'].replace(0, np.nan)
    data['minplaytime'] = data['minplaytime'].replace(0, np.nan)
    data['maxplaytime'] = data['maxplaytime'].replace(0, np.nan)
    data['minage'] = data['minage'].replace(0, np.nan)

    # convert string to list
    # boardgamecategory           object
    # boardgamemechanic           object
    # boardgamefamily             object
    # boardgameexpansion          object
    # boardgameimplementation     object
    # boardgamedesigner           object
    # boardgameartist             object
    # boardgamepublisher          object
    data['boardgamecategory'] = data['boardgamecategory'].str.strip(
        '[]').str.split(',')
    data['boardgamemechanic'] = data['boardgamemechanic'].str.strip(
        '[]').str.split(',')
    data['boardgamefamily'] = data['boardgamefamily'].str.strip(
        '[]').str.split(',')
    data['boardgameexpansion'] = data['boardgameexpansion'].str.strip(
        '[]').str.split(',')
    # drop boardgameimplementation
    data.drop('boardgameimplementation', inplace=True, axis=1)
    # data['boardgameimplementation'] = data['boardgameimplementation'].str.strip(
    #     '[]').str.split(',')
    data['boardgamedesigner'] = data['boardgamedesigner'].str.strip(
        '[]').str.split(',')
    data['boardgameartist'] = data['boardgameartist'].str.strip(
        '[]').str.split(',')
    data['boardgamepublisher'] = data['boardgamepublisher'].str.strip(
        '[]').str.split(',')

    # boardgameintegration
    # boardgamecompilation
    # data['boardgameintegration'] = data['boardgameintegration'].str.strip(
    #     '[]').str.split(',')
    # data['boardgamecompilation'] = data['boardgamecompilation'].str.strip(
    #     '[]').str.split(',')
    # drop
    data.drop('boardgameintegration', inplace=True, axis=1)
    data.drop('boardgamecompilation', inplace=True, axis=1)

    # if number value is 0, replace with None
    # usersrated                   int64
    # average                    float64
    data['usersrated'] = data['usersrated'].replace(0, np.nan)
    data['average'] = data['average'].replace(0, np.nan)

    # 'Board Game Rank' to integer
    # data['Board Game Rank'] = pd.to_numeric(data['Board Game Rank'], errors='coerce')
    data['Board Game Rank'] = data['Board Game Rank'].replace(0, -1)
    # Not Ranked to None
    data['Board Game Rank'] = data['Board Game Rank'].replace('Not Ranked', -1)
    # to integer if not nan
    data['Board Game Rank'] = data['Board Game Rank'].astype(int)

    # Strategy Game Rank to integer
    data['Strategy Game Rank'] = data['Strategy Game Rank'].replace(np.nan, -1)
    data['Strategy Game Rank'] = data['Strategy Game Rank'].astype(int)

    # Family Game Rank to integer
    data['Family Game Rank'] = data['Family Game Rank'].replace(np.nan, -1)
    data['Family Game Rank'] = data['Family Game Rank'].astype(int)

    # Custom Rank to integer
    # Party Game Rank            float64
    # Abstract Game Rank         float64
    # Thematic Rank              float64
    # War Game Rank              float64
    # Customizable Rank          float64
    # Children's Game Rank        object
    # RPG Item Rank              float64
    # Accessory Rank             float64
    # Video Game Rank            float64
    # Amiga Rank                 float64
    # Commodore 64 Rank          float64
    # Arcade Rank                float64
    # Atari ST Rank              float64
    data['Party Game Rank'] = data['Party Game Rank'].replace(np.nan, -1)
    data['Party Game Rank'] = data['Party Game Rank'].astype(int)

    data['Abstract Game Rank'] = data['Abstract Game Rank'].replace(np.nan, -1)
    data['Abstract Game Rank'] = data['Abstract Game Rank'].astype(int)

    data['Thematic Rank'] = data['Thematic Rank'].replace(np.nan, -1)
    data['Thematic Rank'] = data['Thematic Rank'].astype(int)

    data['War Game Rank'] = data['War Game Rank'].replace(np.nan, -1)
    data['War Game Rank'] = data['War Game Rank'].astype(int)

    data['Customizable Rank'] = data['Customizable Rank'].replace(np.nan, -1)
    data['Customizable Rank'] = data['Customizable Rank'].astype(int)

    data['Children\'s Game Rank'] = data['Children\'s Game Rank'].replace(
        np.nan, -1)
    data['Children\'s Game Rank'] = data['Children\'s Game Rank'].replace(
        'Not Ranked', -1)
    data['Children\'s Game Rank'] = data['Children\'s Game Rank'].astype(int)

    data['RPG Item Rank'] = data['RPG Item Rank'].replace(np.nan, -1)
    data['RPG Item Rank'] = data['RPG Item Rank'].astype(int)

    data['Accessory Rank'] = data['Accessory Rank'].replace(np.nan, -1)
    data['Accessory Rank'] = data['Accessory Rank'].astype(int)

    data['Video Game Rank'] = data['Video Game Rank'].replace(np.nan, -1)
    data['Video Game Rank'] = data['Video Game Rank'].astype(int)

    data['Amiga Rank'] = data['Amiga Rank'].replace(np.nan, -1)
    data['Amiga Rank'] = data['Amiga Rank'].astype(int)

    data['Commodore 64 Rank'] = data['Commodore 64 Rank'].replace(np.nan, -1)
    data['Commodore 64 Rank'] = data['Commodore 64 Rank'].astype(int)

    data['Arcade Rank'] = data['Arcade Rank'].replace(np.nan, -1)
    data['Arcade Rank'] = data['Arcade Rank'].astype(int)

    data['Atari ST Rank'] = data['Atari ST Rank'].replace(np.nan, -1)
    data['Atari ST Rank'] = data['Atari ST Rank'].astype(int)

    # print dataframe column types
    print(data.dtypes)

    payload = json.loads(data.to_json(orient='records'))

    for p in payload:
        if p['Board Game Rank'] == -1:
            p['Board Game Rank'] = None
        if p['Strategy Game Rank'] == -1:
            p['Strategy Game Rank'] = None
        if p['Family Game Rank'] == -1:
            p['Family Game Rank'] = None
        if p['Party Game Rank'] == -1:
            p['Party Game Rank'] = None
        if p['Abstract Game Rank'] == -1:
            p['Abstract Game Rank'] = None
        if p['Thematic Rank'] == -1:
            p['Thematic Rank'] = None
        if p['War Game Rank'] == -1:
            p['War Game Rank'] = None
        if p['Customizable Rank'] == -1:
            p['Customizable Rank'] = None
        if p['Children\'s Game Rank'] == -1:
            p['Children\'s Game Rank'] = None
        if p['RPG Item Rank'] == -1:
            p['RPG Item Rank'] = None
        if p['Accessory Rank'] == -1:
            p['Accessory Rank'] = None
        if p['Video Game Rank'] == -1:
            p['Video Game Rank'] = None
        if p['Amiga Rank'] == -1:
            p['Amiga Rank'] = None
        if p['Commodore 64 Rank'] == -1:
            p['Commodore 64 Rank'] = None
        if p['Arcade Rank'] == -1:
            p['Arcade Rank'] = None
        if p['Atari ST Rank'] == -1:
            p['Atari ST Rank'] = None

        # Party Game Rank
        # Abstract Game Rank
        # Thematic Rank
        # War Game Rank
        # Customizable Rank
        # Children's Game Rank
        # RPG Item Rank
        # Accessory Rank
        # Video Game Rank
        # Amiga Rank
        # Commodore 64 Rank
        # Arcade Rank
        # Atari ST Rank
        # group into object 'ranks'
        p['ranks'] = {
            'board_game_rank': p['Board Game Rank'],
            'strategy_game_rank': p['Strategy Game Rank'],
            'family_game_rank': p['Family Game Rank'],
            'party_game_rank': p['Party Game Rank'],
            'abstract_game_rank': p['Abstract Game Rank'],
            'thematic_rank': p['Thematic Rank'],
            'war_game_rank': p['War Game Rank'],
            'customizable_rank': p['Customizable Rank'],
            'childrens_game_rank': p['Children\'s Game Rank'],
            'rpg_item_rank': p['RPG Item Rank'],
            'accessory_rank': p['Accessory Rank'],
            'video_game_rank': p['Video Game Rank'],
            'amiga_rank': p['Amiga Rank'],
            'commodore_64_rank': p['Commodore 64 Rank'],
            'arcade_rank': p['Arcade Rank'],
            'atari_st_rank': p['Atari ST Rank']
        }

        # remove old rank columns
        del p['Board Game Rank']
        del p['Strategy Game Rank']
        del p['Family Game Rank']
        del p['Party Game Rank']
        del p['Abstract Game Rank']
        del p['Thematic Rank']
        del p['War Game Rank']
        del p['Customizable Rank']
        del p['Children\'s Game Rank']
        del p['RPG Item Rank']
        del p['Accessory Rank']
        del p['Video Game Rank']
        del p['Amiga Rank']
        del p['Commodore 64 Rank']
        del p['Arcade Rank']
        del p['Atari ST Rank']

        # minplayers, maxplayers, playingtime, minplaytime, maxplaytime, minage
        # group
        p['game_details'] = {
            'min_players': p['minplayers'],
            'max_players': p['maxplayers'],
            'playing_time': p['playingtime'],
            'min_play_time': p['minplaytime'],
            'max_play_time': p['maxplaytime'],
            'min_age': p['minage']
        }

        # remove old game details columns
        del p['minplayers']
        del p['maxplayers']
        del p['playingtime']
        del p['minplaytime']
        del p['maxplaytime']
        del p['minage']

        # usersrated, average, numweights, averageweight
        # group
        p['rating'] = {
            'users_rated': p['usersrated'],
            'average': p['average'],
            'num_weights': p['numweights'],
            'average_weight': p['averageweight']
        }

        # remove old rating columns
        del p['usersrated']
        del p['average']
        del p['numweights']
        del p['averageweight']

        # for $exists: true
        # if boardgameexpansion None, delete
        if p['boardgameexpansion'] == None:
            del p['boardgameexpansion']

    # print(payload[44]['boardgameexpansion'])
    # print(payload[44]['id'])
    # print(type(payload[44]['boardgameexpansion']))
    # print(payload[0]['boardgamecategory'])

    # save payload to final.json
    # with open('final.json', 'w') as outfile:
    #     json.dump(payload, outfile)

    coll.delete_many({})
    coll.insert_many(payload)
    return coll.count_documents({})


# Import the games_detailed_info.csv file into a MongoDB collection
filename = "games_detailed_info.csv"
mongoimport(filename, 'nosql', 'NOboardgames')
