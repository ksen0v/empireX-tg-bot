import sqlite3
from datetime import datetime, timedelta
from .logger import logger

database_path = 'database.db'


async def init_db():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        is_download BOOLEAN DEFAULT 0,
        next_notification TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()


async def add_user(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO users (user_id, next_notification)
        VALUES (?, ?)
        ''', (user_id, (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')))

        conn.commit()
    except sqlite3.Error as e:
        logger.info(e)
    finally:
        conn.close()


async def get_notification_user():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute('''
                SELECT user_id FROM users 
                WHERE next_notification <= ?
            ''', (now,))
        
        return cursor.fetchall()
    except sqlite3.Error as e:
        logger.info(e)
    finally:
        conn.close()


async def set_next_notification(user_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    try:
        next_time = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute('''
                UPDATE users  
                SET next_notification = ? WHERE user_id = ?
            ''', (next_time, user_id))
        
        conn.commit()
    except sqlite3.Error as e:
        logger.info(e)
    finally:
        conn.close()


async def get_all_users():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT user_id FROM users''')
        user_ids = [row[0] for row in cursor.fetchall()]
        return user_ids
    except sqlite3.Error as e:
        logger.info(e)
    finally:
        conn.close()


async def set_is_download(user_id, key):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''UPDATE users 
                SET is_download = ? WHERE user_id = ?
                ''', (key, user_id))

        conn.commit()
    except sqlite3.Error as e:
        logger.info(e)
    finally:
        conn.close()