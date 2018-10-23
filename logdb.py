#!/usr/bin/env python2.7
import psycopg2


def db_connect():
    """initiate connection to database"""
    db = psycopg2.connect("dbname=news")
    return db


def most_accessed_article():
    """Most accessed articles of all time sorted in descending other."""
    try:
        db = db_connect()  # create database connection
        cursor = db.cursor()
        # query : articles and the amount of time they have been accessed
        cursor.execute("select title, count(*) as views from articles, log where log.path like '/article/' ||  articles.slug and status = '200 OK' group by title order by views desc limit 3;")  # NOQA
        rows = cursor.fetchall()  # fetch results from database
        # loop through to display retrieved records
        for i in rows:
            # query : retrieve article titles via known path in log
            print('"{}" - {} views'.format(i[0], i[1]))  # output text
    finally:
        db.close()  # close database connection


def most_popular_authors():
    """Most popular authors based on total article views per author."""
    try:
        db = db_connect()  # create database connection
        cursor = db.cursor()
        # query : retrieve author, find articles by them and count
        cursor.execute("select authors.name, count(*) as views from authors inner join articles on authors.id = articles.author inner join log on status = '200 OK' and '/article/' || articles.slug = log.path group by authors.name order by views desc;")  # NOQA
        leaderboard = cursor.fetchall()  # fetch results from database
        # loop through to display retrieved records
        for i in leaderboard:
            print('{} - {} views'.format(i[0], i[1]))  # output text
    finally:
        db.close()  # close database connection


def days_with_errors():
    """Percentage error of total requests per day."""
    try:
        db = db_connect()  # create database connection
        cursor = db.cursor()
        # query:use log_report view to calculate percent daily errors > than 1
        cursor.execute("select day, round(error * 100.0 / requests, 1) as percent from log_report group by  day,error,requests having round(error * 100.0 / requests, 1) > 1 order by percent desc;")  # NOQA
        rows = cursor.fetchall()  # fetch results from database
        # loop through to display retrieved records
        for i in rows:
            print('{} - {}% errors'.format(i[0], i[1]))  # output text
    finally:
        db.close()  # close database connection


# report header format
print("\n")
print(54*"*")
print('**************** NEWS DATABASE REPORT ****************')
print(54*"*")
# call method to display most accessed articles
print("\n")
print('The most popular three articles of all time:')
print(54*"_")
most_accessed_article()
# call method to display most popular authors
print("\n")
print('The most popular article authors of all time:')
print(54*"_")
most_popular_authors()
# call method to display days with over 1% error requests
print("\n")
print('Days with more than 1% of requests leading to errors:')
print(54*"_")
days_with_errors()
print("\n")
