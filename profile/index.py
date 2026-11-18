#!/usr/bin/env python3

import os
import sys

from minks.client import request, send_response, Response
from minks.html import HTML

if request.method not in ['GET', 'HEAD']:
	send_response(405, {}, None)
	sys.exit(0)

home = os.path.dirname(__file__)

f = HTML()

f.start('html')
f.start('head')
f.tags('link', attrs={'rel': 'stylesheet', 'href': '/style.css'})
f.end()
f.start('body')
f.tags('h1', text_content='Profiles')
f.tags('a', attrs={'href': '..'}, text_content='Back')
f.tag('hr')
profiles = os.listdir(home)
print(profiles, file=sys.stderr)
for delete in os.listdir(home):
	if os.path.isfile(home + '/' + delete):
		del profiles[profiles.index(delete)]
for profile in profiles:
	f.tags('p', attrs={'class': 'nomargin'}, html_content=f.mktags('a', attrs={'href': profile}, text_content=profile))
	f.tag('img', attrs={'src': f'{profile}/pfp.png', 'width': '64'})
f.end()
f.end()

send_response(Response(200, {'content-type': 'text/html'}, bytes(f)))
