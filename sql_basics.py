def fetch_all_sql(query, db, con):
	con.execute(query)
	results = con.fetchall()
	return results


def fetch_one_sql(column_name, query, db, con):
	return_value = None
	con.execute(query)
	results = con.fetchone()
	if results is not None:
		return_value = results[f'{column_name}']
	return return_value


def db_commit_sql(query, db, con):
	con.execute(query)
	db.commit()