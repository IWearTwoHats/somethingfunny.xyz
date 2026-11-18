#!/usr/bin/python3

import os

from minks.client import request, send_response, Response
from minks.html import HTML

if request.method not in ['GET', 'HEAD']:
	send_response(Response(405, {}, None))

f = HTML()

f.start('html')
f.start('head')
f.tags('title', text_content='Anti Cromulent Drawing Competition')
f.tags('link', attrs={'rel': 'stylesheet', 'href': '/style.css'})
f.end()
f.start('body')

f.tags('h1', text_content='Anti Cromulent Drawing Competition')
f.tags('a', attrs={'href': '..'}, text_content='Back')
f.tag('hr')
f.tags('p', attrs={'class': 'center'}, html_content='<b>Cromulent</b>')
f.tags('p', attrs={'class': 'center'}, text_content='Adjective - Humorous')
f.tags(
	'p',
	attrs={'class': 'center', 'style': 'font-size: .75em;'},
	text_content='Acceptable or adiquate.'
)
f.tags(
	'p',
	attrs={'class': 'center', 'style': 'font-size: .75em;'},
	html_content=f.mktags(
		'i',
		text_content='My morning coffee was perfectly cromulent.'
	)
)
f.tag('hr')
f.tags('p', attrs={'class': 'center'}, text_content='The ACDC is a drawing "competition" between TwoHats and their friends.')
f.tag('hr')

f.tags('h1', text_content='Rules')
f.start('div', attrs={'class': 'center-box'})
f.start('ol')
f.tags('li', text_content='You must not create anything spectacular.')
f.tags('li', text_content='Have fun!')
f.end()
f.end()
f.tag('hr')
f.tags('h1', text_content='Archive')
f.tag('hr')

dir_path = os.path.dirname(__file__) + '/years'

for year in reversed(sorted([int(name) for name in os.listdir(dir_path) if os.path.isdir(dir_path + '/' + name)])):
	f.tags(
		'p',
		attrs={'class': 'center'},
		html_content=f.mktags(
			'a',
			attrs={'href': f'years/{year}'},
			text_content=str(year)
		)
	)
f.tag('hr')

f.end()
f.end()

send_response(Response(200, {'content-type': 'text/html'}, bytes(f)))
