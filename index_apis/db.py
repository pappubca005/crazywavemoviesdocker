import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "db.sqlite3", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES
)
db_df = pd.read_sql_query("SELECT * FROM movies_popularmovies", conn)
db_df.to_csv("database.csv", index=False)
