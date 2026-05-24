import psycopg2

conn = psycopg2.connect(
    host="database-1.c32s00aqy976.ap-south-2.rds.amazonaws.com",
    database="newsdb",
    user="postgres",
    password="Nenenandu",
    port="5432"
)

print("Database connected successfully!")

conn.close()