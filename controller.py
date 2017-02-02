import bottle

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

bottle.debug(True)
bottle.run(host='localhost', port=8082)
#localhost:8082/api?a=300&f=INR&t=USD