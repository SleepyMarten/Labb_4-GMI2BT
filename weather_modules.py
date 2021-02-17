import sqlite3
    
def db_connect():
    conn = None
    try:
        conn = sqlite3.connect('weather.db')
    except sqlite3.Error as e:
        print(e)
    return conn

    
def create_db():
    conn = db_connect()
    c = conn.cursor()
    
    #c.execute("CREATE TABLE Weather(sensor, temp, humidity, pressure)")
    w_data = """CREATE TABLE Weather(
        sensor text NOT NULL,
        temp text NOT NULL,
        humidity text NOT NULL,
        pressure text NOT NULL) """
    
    c.execute(w_data)
    
    conn.commit()
    conn.close()

def save_data(data):
    conn = db_connect()
    
    """Inserting data into the Weather table"""
    insert = """ INSERT INTO Weather (sensor, temp, humidity, pressure) VALUES (?,?,?,?) """
    values = (data['sensor'],data['temp'],data['humidity'],data['pressure'])
    conn.execute(insert, values)
    conn.commit()
    conn.close()
    print("Data was added to the database: SUCCESS!!")

