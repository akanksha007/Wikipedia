import web
import wiki_url

urls = (
  '/', 'Index',
)

app = web.application(urls, globals())

render = web.template.render('templates/')
class Index(object):
    def GET(self):
        return render.index([])
    def POST(self):
    	# we take input from the form and parse the xml
    	# and according to the url return the list to the 
    	# interface
    	form = web.input(url='https://en.wikipedia.org/wiki/New_York')
    	url = str(form.url)
    	c = wiki_url.Geturl(url)
    	return render.index(c)


if __name__ == "__main__":
    app.run()
