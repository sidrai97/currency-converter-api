import os
import bottle

def allow_cors(func):
	def wrapper(*args, **kwargs):
		bottle.response.headers['Access-Control-Allow-Origin'] = '*' # * in case you want to be accessed via any website
		return func(*args, **kwargs)
	return wrapper

@bottle.get('/api')
@allow_cors
def index_page():
	amount=bottle.request.query.a
	from_am=bottle.request.query.f
	to_am=bottle.request.query.t
	print amount
	print from_am
	print to_am
	return bottle.template('./views/api.tpl',a=amount,f=from_am,t=to_am)

@bottle.error(404)
def error404(error):
	return bottle.template('./views/error.tpl')

if os.environ.get('APP_LOCATION') == 'heroku':
	bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
else:
	bottle.run(host='localhost', port=8082, debug=True)

#bottle.debug(True)
#bottle.run(host='localhost', port=8082)
#localhost:8082/api?a=300&f=INR&t=USD