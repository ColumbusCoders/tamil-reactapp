

import urls as urls
import functions_Scrap as f
#import insertRecordsToDB as inserttodb




allheadlines = []


for key, url in urls.headlines_urls.items():
    
    category = 'headlines'
    
    allheadlines.extend(f.getHeadLines(url,key,category))

for key, url in urls.sports_urls.items():
    
    category = 'sports'
    
    allheadlines.extend(f.getHeadLines(url,key,category))
    

for key, url in urls.cinema_urls.items():
    
    category = 'cinema'
    
    allheadlines.extend(f.getHeadLines(url,key,category))
    
    
for key, url in urls.divine_urls.items():
    
    category = 'divine'
    
    allheadlines.extend(f.getHeadLines(url,key,category))


for key, url in urls.business_urls.items():
    
    category = 'business'
    
    allheadlines.extend(f.getHeadLines(url,key,category))    
    
    

#for h in allheadlines:
    
 #  print (h)
   
   
  # inserttodb.insertIntoDB(h.title,h.link,h.published,h.img,h.desc,h.sitename,h.category)
 