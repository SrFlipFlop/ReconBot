from sqlite3 import connect

#Platforms: | id | name | url |
#Assets: | id | name | url | platform | android | ios | reward | scope |
#Scope: | asset | url | time |

def create_db(db_path):
    connection = connect()
    c = connection.cursor()
    
    c.execute("CREATE TABLE platforms (name text, url text)")
    c.execute("CREATE TABLE assets (id text, name text, hash text, timestamp real)")

    
    connection.commit()
    connection.close()

def connect_db(db_path)
    return connect(db_path)

def save_platforms_db(platforms):
    pass

def save_assets_db(assets):
    pass

def save_assets_local(assets):
    pass
