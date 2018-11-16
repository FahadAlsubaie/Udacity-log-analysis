#!/usr/bin/env python
# encoding: utf-8

import psycopg2

print "Starting"



def topArticles():

	try:
		db = psycopg2.connect(database="news")
		print "Database is connceted now"
		cur=db.cursor()
		firstQuery='''select articles.title, count(*) as Views
		from articles, log
		where articles.slug = substr(log.path, 10)
		and log.status = '200 OK'
		group by articles.title
		order by Views desc
		limit 3;'''
		cur.execute(firstQuery)
		rows = cur.fetchall()

		print ('\n\nTop Most Viewed Articles ')

		j=1
		for i in rows:
			print( str(j)+'-'+i[0]+' has '+ str(i[1]) +' views')
			j += 1
	finally:
		db.close

def topAuthors():
	try:
		db = psycopg2.connect(database="news")
		cur=db.cursor()
		secondQuery='''
		SELECT authors.name, count(*) as views
		FROM articles, log, authors
		WHERE articles.author = authors.id
		and articles.slug = substr(log.path, 10)
		GROUP BY authors.name
		ORDER BY views DESC
		LIMIT 3;
		'''
		cur.execute(secondQuery)
		rows = cur.fetchall()
		print ('\nMost Viewed Authors')

		j=1
		for i in rows:
			print( str(j)+'-'+i[0]+' has '+ str(i[1]) +' views')
			j += 1

	finally:
		db.close












if __name__ == '__main__':
	topArticles()
	topAuthors()
