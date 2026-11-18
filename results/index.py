#!/usr/bin/python3

import sys
import json

from minks.client import request, send_response, Response
from minks.html import HTML
from thpath import Path

if request.method not in ['GET', 'HEAD']:
	send_response(Response(405, {}, None))
	sys.exit(0)

def search(query: str):
	with open((Path(__file__)[:-1] / Path('search.json')).path) as f:
		db = json.load(f)

	sections = {}

	for section, term in db.items():
		sections[section] = {}
		for name, location in term.items():
			if query.lower() in name.lower():
				sections[section][name] = location
	return sections

f = HTML()

f.start('html')
f.start('head')
f.tags('title', text_content='Search')
f.tag('link', attrs={'rel': 'stylesheet', 'href': '/style.css'})
f.end()
f.start('body')

f.tags('h1', html_content=f.mktags('a', attrs={'class': 'hidden', 'href': '/'}, text_content='Something funny.'))
f.tags('h2', text_content='Search results')
f.tags('a', attrs={'href': '/search'}, text_content='Search again')
f.tag('hr')

searchq = request.query.get('q')
searchsection = request.query.get('category')
if not searchq and not searchsection:
	send_response(Response(303, {'location': '/search'}, None))

for section, term in search(searchq if searchq is not None else '').items():
	if searchsection and section.lower() != searchsection.lower():continue
	if len(term) == 0:continue
	f.tags('h3', text_content=section)
	for name, location in term.items():
		f.tags('p', attrs={'class': 'center'}, html_content=f.mktags('a', attrs={'href': location}, text_content=name))
f.tag('hr')

f.end()
f.end()

send_response(Response(200, {'content-type': 'text/html'}, bytes(f)))
