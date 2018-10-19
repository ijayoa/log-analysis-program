import psycopg2


def most_accessed_article():
	"""Return the most accessed articles of all time sorted in descending other."""
	db = psycopg2.connect("dbname=news") # connect to database
	cursor = db.cursor()
	try:
		# query - retrieve articles and the amount of time they have been accessed
		cursor.execute("select path, count(*) as views from log where path like '/article/%' group by path order by views desc limit 3;")
		rows = cursor.fetchall() # fetch results from database
		if rows:
			# loop through to display retrieved records
			for i in rows:
				# query - retrieve article titles via known path in log
				cursor.execute("select title from articles where slug like '{}'".format(i[0][9:]))
				record = cursor.fetchall()
				print('"{}" - {} views'.format(record[0][0], i[1])) #output format
	finally:
		db.close() #close database connection

# def most_popular_authors():
# 	db = psycopg2.connect("dbname=news")
#   cur = db.cursor()
#   db.close()
# 	article_name = "Lorem Ipsum Test Article"
# 	views = 405
# 	print('"{}" - {} views'.format(article_name, views))

# def days_with_errors():
# 	db = psycopg2.connect("dbname=news")
#   cur = db.cursor()
#   db.close()
# 	article_name = "Lorem Ipsum Test Article"
# 	views = 405
# 	print('"{}" - {} views'.format(article_name, views))


print("\n")
print('The most popular three articles of all time:')
print(80*"_")
most_accessed_article()


# print("\n")
# print('The most popular article authors of all time:')
# print(80*"_")
# print("\n")
# most_popular_authors()

# print("\n")
# print('Days with more than 1% of requests leading to errors:')
# print(80*"_")
# print("\n")
# days_with_errors()