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


def fetch_one_sql(column_name, query, db, con):
	return_value = None
	con.execute(query)
	results = con.fetchone()
	if results is not None:
		return_value = results[f'{column_name}']
	return return_value


def connect_mysql(creds_path):
	db = mysql.connector.connect(option_files=[creds_path], option_groups=['some_server'])
	con = db.cursor(dictionary=True, buffered=True)
	return db, connector


PROC_LOCAL_DB_CON = None


def chunks_of_records(range_iterable, chunk_size):
	for range_index in range(0, len(range_iterable)+1, chunk_size):
		yield range_iterable[range_index: range_index + chuck_size - 1]


def signal_handler(signum, frame):
	print("Signal {} Received To Shutdown".format(signum))


def init_process_connection():
	global PROC_LOCAL_DB_CON
	PROC_LOCAL_DB_CON = mysql.connector.connect(option_files=[creds_path], option_groups=["qsentry"])


def multiprocess_info(start_id, end_id):
	chunk_size=1000
	chunks_per_map=1
	processes_to_start=cpu_count()*2
	total_records=0
	signal.signal(signal.SIGTERM, signal_handler)
	singal.signal(signal.SIGINT, signal_handler)
	range_to_process = chunks_of_records(range(start_id, end_id), chunk_size)
	pool = Pool(processes=processes_to_start, initializer=init_process_connection)
	rows_affected = pool.map(process_range, range_to_process, chunks_per_map)
	pool.close()
	pool.join()
	total_records = [sum(x for x in rows_affected if x is not None)]
	print(f"Total_Records: {total_records}")


def process_range(range_object):
	sql_statement = """select field1, field2, field3
		from db.table
		where id between {id_start} and {id_end}""".format(id_start=range_object.start, id_stop=range_object.stop)
	target_dbcon = PROC_LOCAL_DB_CON
	target_dbcurser = target_dbcon.cursor(dictionary=True, buffered=True)
	target_dbcursor.execute("set innodb_loc_wait_timesout = 120;")
	records_updasted_messages = None
	rows_affected = 0
	percent_done = find_percent_finished(range_object.start - min_iduser, max_iduser - min_iduser)
	line_print = "Processing {}, {}%".format(range_object.start, percent_done)
	print(line_print, end="\r")
	time.sleep(1)
	target_dbcursor.execute(sql_statement)
	results = target_dbcursor.fetchall()
	with open(out_file, "a") as csvfile:
		csvwriter = csv.writer(csvfile)
		for row in results:
			value = row["field1"], row["field2"], row["field3"]
			csvwriter.writerow(value)
	rows_affected = target_dbcursor.rowcount
	target_dbcursor.close()
	return rows_affected


def find_percent_finished(current_number, total_number):
	add this module


def check_for_folder(path, the_type):


def main():
	min_id = 1
	max_id = 1000
	multiprocess_info(min_id, max_id)

	
if __name__ == '__main__':
	main()
