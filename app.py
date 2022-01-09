<<<<<<< HEAD
import pandas as pd
from configparser import ConfigParser
import psycopg2
from db_last import Content
from database import Database

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        Database.initialise(**params)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    connect()
    Content_Group = {'Poker_group': ['GOP1', 'GOP2', 'GOP3', 'Poker World', 'Monopoly Poker'],
                     'Social_group': ['Habbo', 'Hotel Hideaway', 'Woozworld', 'Smeet'],
                     'Casual_group': ['Reach Games', 'Stratego', 'Operate Now', 'Agame'],
                     'Slot_games': ['Slot Games'],
                     'GD': ['GD', 'C2M', 'Tubia'],
                     'National_portals': ['National Portals', 'Hyvesgames'],
                     'Spil_portals': ['Spil Portals'],
                     'E_commerce': ['Voidu Stores'],
                     'ZoomIn': ['MCN', 'Content', 'Video Player'],
                     'Other_group': ['Others']}

    Poker_group_feed = {}
    path = '/Users/uca/PycharmProjects/MIS/data/'
    for i in Content_Group['Poker_group']:
        data = Content.load(i)
        Poker_group_feed[i] = pd.DataFrame(data,columns=['Poker_group_id',
                                                         'value',
                                                         'revenuedate'])

    for keys in Poker_group_feed:
        print(keys)
        Poker_group_feed[keys].to_csv("/Users/uca/PycharmProjects/MIS/data/{}.csv".format(keys))


