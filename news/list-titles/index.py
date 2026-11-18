#!/usr/bin/env python3

import sys
import json

from minks.client import request, Response, send_response
from minks.html import HTML
from thpath import Path

if request.method != 'GET':
	send_response(Response(405, {}, None))
	sys.exit(0)

f = HTML()

f.start('html')
f.start('head')
f.tags('title', text_content='News list')
f.tag('link', attrs={'rel': 'stylesheet', 'href': '/style.css'})
f.end()
f.start('body')

f.tags('h1', text_content='News List')
f.tags('h2', text_content='By Title')

f.tags('a', attrs={'href': '..'}, text_content='Back')

f.tag('hr')

with open((Path(__file__)[:-2] + Path('news.json')).path) as file:
	news = json.load(file)

for date, data in news.items():
	f.tags('p', attrs={'class': 'center'}, html_content=f.mktags('a', attrs={'href': f'..?date={date}'}, text_content=data['title']))
f.tag('hr')
f.end()
f.end()

send_response(Response(200, {'content-type': 'text/html'}, bytes(f)))
