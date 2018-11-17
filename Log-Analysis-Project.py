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
			print( str(j)+'-'+i[0]+' has '+ str(i[1]) +' views.')
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
			print( str(j)+'-'+i[0]+' has '+ str(i[1]) +' views.')
			j += 1

	finally:
		db.close
def mostErrorsDay():
	try:
		db = psycopg2.connect(database="news")
		cur=db.cursor()
		thirdQuery='''
		select errors.day, round(((errors.not_found*1.0) / total_per_day.num)*100,1) as percent
		from (
		select date_trunc('day',time) "day", count(*) as num
		from log group by day) as total_per_day
		join (
	    select date_trunc('day',time) "day", count(*) as not_found from log
		where status = '404 NOT FOUND' group by day) as errors
		on errors.day = total_per_day.day
		where (round(((errors.not_found*1.0) / total_per_day.num)*100,1) >1)
		order by percent desc;
		'''
		cur.execute(thirdQuery)
		rows = cur.fetchall()
		print ('\nDays that has more than 1% errors')


		for i in rows:

			print( i[0].strftime('%x')+' has '+ str(i[1]) +'% errors.')


	finally:
		db.close

if __name__ == '__main__':
	topArticles()
	topAuthors()
	mostErrorsDay()
