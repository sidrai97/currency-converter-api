import os
import bottle
import urllib
from BeautifulSoup import *

@bottle.get('/api')
def index_page():
	try:
		amount=bottle.request.query.a
		from_am=bottle.request.query.f
		to_am=bottle.request.query.t
		url='https://www.xe.com/currencyconverter/convert/?Amount='+amount+'&From='+from_am+'&To='+to_am
		#url='https://finance.google.com/finance/converter?a='+amount+'&from='+from_am+'&to='+to_am
		html_resp=urllib.urlopen(url).read()
		soup = BeautifulSoup(html_resp)
		#json_resp=soup.find('div', id='currency_converter_result')
		json_resp=soup.find('span', class_='converterresult-toAmount')
		json_resp=map(str, json_resp.contents)
		sp_str=json_resp[1]
		#sp_str=sp_str[18:sp_str.index('<',18)]
		#fp_str=json_resp[0].split(' ')
		#sp_str=sp_str.split(' ')
		return '{"data":[{"from":["'+from_am+'","'+amount+'"]},{"to":["'+to_am+'","'+sp_str+'"]}]}'
	except:
		return bottle.redirect('https://sidrai97.github.io/currency-converter-api/')	

@bottle.route('/')
@bottle.route('/documentation')
def documentation_page():
	return bottle.redirect('https://sidrai97.github.io/currency-converter-api/')

@bottle.error(404)
def error404(error):
	return bottle.template('./views/error.tpl')

if os.environ.get('APP_LOCATION') == 'heroku':
	bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
else:
	bottle.run(host='localhost', port=8082, debug=True)
