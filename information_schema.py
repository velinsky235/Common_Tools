### queries for accessing the information schema

query = "show databases"

query = "select table_name, TABLE_ROWS from information_schema.talbes wehre table_schema = {some_scheme}"

query = "select column_name from information_schema.columns where table-schema = {} and table_name = {}"