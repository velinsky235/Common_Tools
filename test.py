import psycopg2
import configparser
import os
import csv

def connect_sql(db_cnf, server):
	print("Connecting to postgreSQL db now...\n")
	config = configparser.ConfigParser()
	creds = config.read("db.cnf")
	conn = psycopg2.connect(
		user = config[server]["user"],
		password = config[server]["password"],
		database = config[server]["database"],
		host = config[server]["host"])
	cur = conn.cursor()
	print("Connection successful...\n")
	return conn, cur


def close_sql(cur, conn):
	cur.close()
	conn.close()
	print("Cursor and conn closed...\n")


def error_without_file(fname):
	if not os.path.isfile(fname):
		print(f"{fname} is missing!!")
		exit()


def delete_file_if_exists(file_path):
	if os.path.isfile(file_path):
		os.system(f"rm {file_path}")


def find_tables(cur, conn):
	values = []
	query = """select table_schema, table_name 
		from information_schema.tables
		order by table_schema, table_name"""
	conn.execute(query)
	results = conn.fetchall()
	for row in results:
		values.append([row[0], row[1]])
	print(f"{len(values)} db / table combinations found...\n")
	return values


def record_count(cur, conn, values):
	record_counts = []
	for database, table in values:
		query = f"""select count(*) as the_count
			from {database}.{table}"""
		conn.execute(query)
		results = conn.fetchone()
		if results is not None:
			records = results[0]
		print(f"\n{database}.{table}\tRecords: {records}")
		record_counts.append([database, table, records])
	return record_counts	


def write_results(out_file, record_counts):
	with open(out_file, "w") as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(["database", "table", "records"])
		for database, table, records in record_counts:
			csvwriter.writerow([database, table, records])

def main():
	# open a sql connection, error if db file does not exist
	server = "compass_mining"
	db_cnf = os.path.join(os.getcwd(), "db.cnf")
	error_without_file(db_cnf)
	cur, conn = connect_sql(db_cnf, server)
	# declare the out_file
	out_file = "database_table_audit.csv"
	# find all database and table combinations
	values = find_tables(cur, conn)
	# find count of records per table
	record_counts = record_count(cur, conn, values)
	write_results(out_file, record_counts)
	# close the sql connection
	close_sql(cur, conn)


if __name__ == '__main__':
	main()
