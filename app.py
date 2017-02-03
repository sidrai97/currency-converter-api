import os
import bottle

@bottle.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@bottle.get('/api')
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