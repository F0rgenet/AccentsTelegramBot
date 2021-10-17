import sqlite3
import logging

logger = logging.getLogger("database")


class DataBase(object):

	# Написать CRUD

	def __init__(self, path: str):
		connection = sqlite3.connect(path)
		cursor = connection.cursor()
		cursor.execute(f"CREATE TABLE IF NOT EXISTS users (user_id integer, state text)")
		logger.info("database created")