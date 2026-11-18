#!/usr/bin/python3

import json
from sys import exit

from minks.client import request, Response, send_response
from minks.html import HTML
from thpath import Path

if request.method not in ['GET', 'HEAD']:
	send_response(Response(405, {}, None))
	exit(0)

f = HTML()

f.start('html')
f.start('head')
f.tags('title', html_content='News')
f.tag('link', attrs={'rel': 'stylesheet', 'href': '/style.css'})
f.end()
f.start('body')

f.tags('h1', html_content='News')
f.tags('p', attrs={'class': 'nomargin'}, html_content=f.mktags('a', attrs={'href': '..'}, text_content='Back'))
f.tags('p', attrs={'class': 'nomargin'}, html_content=f.mktags('a', attrs={'href': './list-titles'}, text_content='By title'))
f.tags('p', attrs={'class': 'nomargin'}, html_content=f.mktags('a', attrs={'href': './list-dates'}, text_content='By date'))
if 'date' in request.query:
	f.tags('p', attrs={'class': 'nomargin'}, html_content=f.mktags('a', attrs={'href': '.'}, text_content='Show all'))
f.tag('hr')

news_dir = Path(__file__)[:-1]
with open((news_dir / Path('news.json')).path) as file:
	news = json.load(file)

if 'date' in request.query:
	req_date = request.query['date']
	if req_date in news:
		news = {req_date: news[req_date]}
	else:
		f.tags('p', text_content='Nothing found.')
		f.tag('hr')
		news = {}

for date, data in news.items():
	f.tags('h4', text_content=date)
	source = data.get('source')
	if source == 'body':
		body = data['body']
	elif source == 'file':
		with open((news_dir / Path(data['file'])).path) as file:
			body = file.read()
	else:
		body = '[no source]'

	f.tags('h2', attrs={'id': date}, text_content=data['title'])
	f.start('div', attrs={'class': 'text-container'})
	f.tags('p', attrs={'class': 'center'}, html_content=body)
	f.end()
	f.tags('p', attrs={'class': 'center'}, html_content=f.mktags('a', attrs={'href': f'/profile/{data['author']}'}, text_content=data['author']))
	f.tags('hr')

f.end()
f.end()

send_response(Response(200, {'content-type': 'text/html'}, bytes(f)))
