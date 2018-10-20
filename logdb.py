import psycopg2


def most_accessed_article():
  """Return the most accessed articles of all time sorted in descending other."""
  db = psycopg2.connect("dbname=news")  # connect to database
  cursor = db.cursor()
  try:
    # query - retrieve articles and the amount of time they have been accessed
    cursor.execute("select title, count(*) as views from articles, log where log.path like '/article/' ||  articles.slug and status = '200 OK' group by title order by views desc limit 3;")
    rows = cursor.fetchall()  # fetch results from database
    # loop through to display retrieved records
    for i in rows:
      # query - retrieve article titles via known path in log
      print('"{}" - {} views'.format(i[0], i[1]))  # output string format
  finally:
    db.close()  # close database connection

def most_popular_authors():
  """Return the most popular authors sort by highest number of article views."""
  db = psycopg2.connect("dbname=news")
  cursor = db.cursor()
  try:
    cursor.execute("select authors.name, count(*) as views from authors inner join articles on authors.id = articles.author inner join log on status = '200 OK' and '/article/' || articles.slug = log.path group by authors.name order by views desc;")
    leaderboard = cursor.fetchall()
    for i in leaderboard:
      print('{} - {} views'.format(i[0], i[1]))  # output string format
  finally:
    db.close()

# def days_with_errors():
#   db = psycopg2.connect("dbname=news")
#   cur = db.cursor()
#   db.close()
#   article_name = "Lorem Ipsum Test Article"
#   views = 405
#   print('"{}" - {} views'.format(article_name, views))


print("\n")
print('The most popular three articles of all time:')
print(80*"_")
most_accessed_article()


print("\n")
print('The most popular article authors of all time:')
print(80*"_")
most_popular_authors()

# print("\n")
# print('Days with more than 1% of requests leading to errors:')
# print(80*"_")
# print("\n")
# days_with_errors()
