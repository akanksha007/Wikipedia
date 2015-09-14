import wikipedia
import operator
import requests
import re
import urllib2

requests.packages.urllib3.disable_warnings()
def Geturl(url):
    count={}
    try:
        
        # to check whether url exist
        url_info=urllib2.urlopen(url)
        link=url.rsplit('/',1)
        
        #open the wikipedia page
        details=wikipedia.page(link[1])
        
        #find all the link for the given url
        link=details.links
        
        #find the count of pages that contain the link
        for l in link:
            k=wikipedia.search(l,max=10000,suggestion=False)
            
            count={l:len(k)}
            
        #to get the link which has the max count
        c=[]
        c.append(max(stats.iteritems(), key=operator.itemgetter(1))[0])
        
        return c
    except:
        exceptlist="Error:Invalid URL"
        return exceptlist
	    

