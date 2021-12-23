from configparser import ConfigParser
import psycopg2
import pandas as pd

query = """ 

select "Name","TotalRevenue" , "RecordDate" from "ContentItemData" CD  JOIN "PillarItems" PI
ON CD."PillarItemId" = PI."Id"
WHERE "Name" = 'GOP3'

"""

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
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('Getting data from database:')
        cur.execute(query)

        # display the PostgreSQL database server version
        GOP3 = pd.read_sql(query,conn)

        print(GOP3)

        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    connect()