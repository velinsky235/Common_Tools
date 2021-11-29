from multiprocessing import Pool, cpu_count
import time
import signal
import re
import mysql.connector
import os
import sys
from getpass import getuser
import datetime as dt
import csv


def db_commit_sql(query, db, con):
	con.execute(query)
	db.commit()


def connect_mysql(creds_path):
	db = mysql.connector.connect(option_files=[creds_path], option_groups=['some_server'])
	con = db.cursor(dictionary=True, buffered=True)
	return db, connector


def read_in_values(file):
	values = []
	# read them in somehow
	return values 


items_per_map = 100
processes_to_start = (cpu_count())


def chunks(iterable, chunksize):
	for i in range(0, len(iterable), chunksize):
		yield iterable[i:i + chunksize]


def process_range(range_object):
	final_values = []
	query = """select column1, colmn2
		from db.table
		where colmn in ({0})""".format(",".join(["%s"]*len(range_object)))
	db = connect_mysql(creds_path, server)
	con = db.cursor()
	con.execute(query, range_object)
	results = con.fetchall()
	for row in results:
		value = row[0], row[1], row[2]
		final_values.append(value)
	return final_values


def multiprocess_the_values(values):
	final_values = []
	pool = Pool(processes=processes_to_start)
	itemstoprocess = chunks(values, items_per_map)
	final_results = pool.map(process_range, itemstoprocess)
	pool.close()
	pool.join()
	for x in final_results:
		for row in x:
			final_values.append(row)
	print(f"Instances found: {len(final_values)}")
	return final_values


def do_something(final_values, out_file):
	# do something if you want


creds_path = os.path.join(os.getcwd(), "db.cnf")

server = "some_server"
file = "some_file"
out_file = "some_out_file"

if __name__ == '__main__':
	values = read_in_values(file)
	final_values = multiprocess_the_values(values)
	do_something(final_values)