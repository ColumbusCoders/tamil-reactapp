import feedparser
from dateutil.parser import parse
from bs4 import BeautifulSoup
import requests
import insertRecordsToDB as inserttoDB



class rssresult(object):
    def __init__(self, title=None, link=None,published=None,img=None,desc=None,sitename=None,category=None):
        self.title = title
        self.link = link
        self.published = published
        self.img = img
        self.desc = desc
        self.sitename = sitename
        self.category = category


def parseRSS(rss_url):
    
    return feedparser.parse(rss_url)



def getHeadLines(rss_url,key,category):

    print (key)
    headlines = []
    pubDate = ''
    sitename = ''
    
    if key == 'Google News':
        
        
        feed = feedparser.parse(rss_url)
        #print (len(feed.entries))
        # print (feed['entries'][1])
        for newitem in feed.entries:
            
                 #print ('Google Link - '+newitem.link)


                 page =  requests.get(newitem.link)    
                 #page = requests.get(enclink.get('href'))
                 soup1 = BeautifulSoup(page.content,'html.parser')
                 #images = soup1.find('link',rel="image_src")
                 
                 
                 meta_title = soup1.find('meta',property="og:title")
                 meta_published_time = soup1.find('meta',property="article:published_time")
                 meta_sitename = soup1.find('meta',property="og:site_name")
                 meta_images = soup1.find('meta',property="og:image")
                 meta_description = soup1.find('meta',property="og:description")
                 meta_articleurl = soup1.find('meta',property="og:url")
                 
                 
                 if meta_articleurl is not None:
                 
                         if 'google.com' not in meta_articleurl.get('content'):
                                 
                                 if meta_sitename is not None:
                                     #print ('Sitename  '+meta_sitename.get('content'))
                                     sitename = meta_sitename.get('content')
                                     
                                     
                                 if meta_title is not None:
                                     #print ('Title  '+meta_title.get('content'))
                                     title = meta_title.get('content')
                                 else:
                                     break
                                    
                                     
                                 
                                 if meta_published_time is not None:
                                     #print ('Pub Time  '+meta_published_time.get('content'))  
                                     d= parse(str(meta_published_time.get('content')))
                                     pubDate = d.strftime('%Y-%m-%d %H:%S')
                                     
                         
                                 if meta_images is not None:
                                     #print ('Image Link '+meta_images.get('content'))
                                     imagelink = meta_images.get('content')
                                     
                                 if meta_description is not None:
                                     #print ('Desc Link '+meta_description.get('content'))
                                     description = meta_description.get('content')
                                 
                                 if meta_articleurl is not None:
                                     #print ('Article Link '+meta_articleurl.get('content'))
                                     article_url = meta_articleurl.get('content')
                         
                             
                                 headlines.append(rssresult(title,article_url,pubDate,imagelink,description,sitename,category))
                                 inserttoDB.insertIntoDB(title,article_url,pubDate,imagelink,description,sitename,category)
    else:
        
        feed = feedparser.parse(rss_url)
        for newitem in feed.entries:
        
             soup = BeautifulSoup(newitem.summary,'html.parser')
             para_1 = soup.find('p')
             print (para_1)
          
             # Skip iteration if no description
             if para_1 is None:
                 break
             
             
             imagelink = ""
             
             if para_1 is not None:
                 description = para_1.get_text()
             images = soup.find('img')
             
             # Skip iteration if the description is invalid
             if description == '...':
                 #print (newitem.link)
                 break
             
             print (category+' desc is '+description)   
             
             if not description :
                 
                 page_desc =  requests.get(newitem.link)    
                 #page = requests.get(enclink.get('href'))
                 soup_desc = BeautifulSoup(page_desc.content,'html.parser')
                 meta_description = soup_desc.find('meta',property="og:description")
                 description = meta_description.get('content')
                
             
             if images is not None :
                 #para = soup.find('<p>')
                 imagelink = images['src']
                 
             if not images:
                 page_img =  requests.get(newitem.link)    
                 #page = requests.get(enclink.get('href'))
                 soup_img = BeautifulSoup(page_img.content,'html.parser')
                 meta_images = soup_img.find('meta',property="og:image")
                 imagelink = meta_images.get('content')
                 
             sitename = key
             article_url = newitem.link
             title = newitem.title
            
            
                
             d= parse(str(newitem.published))
             pubDate = d.strftime('%Y-%m-%d %H:%S')
             #print (newitem.title)
             headlines.append(rssresult(title,article_url,pubDate,imagelink,description,sitename,category))
             inserttoDB.insertIntoDB(title,article_url,pubDate,imagelink,description,sitename,category)


        
    headlines.sort(key=lambda r: r.published,reverse=True)                        
    return headlines                     





