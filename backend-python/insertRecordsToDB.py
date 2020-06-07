import psycopg2



def insertIntoDB(title,link,pubdate,imagelink,description,sitename,category):

    dbSession       = psycopg2.connect(user="postgres",
                                      password="password",
                                      host="localhost",
                                      port="5432",
                                      database="NewsDB")
    try:
                    
        #link_var = link
        dbCursor = dbSession.cursor();
            
        try:
            print ('Strted to insert')
            
            sqlSelect = "select * from public.\"TamilNews\" where title ='"+title+"' and category ='"+category+"'" ;
            dbCursor.execute(sqlSelect);
            rows = dbCursor.rowcount;
            
           # print (rows)
            
            
            #Count Rows and exit function
            if rows > 0:
                print('skipped insert')
                return None
            
            sqlInsertRow1  = "INSERT INTO public.\"TamilNews\" VALUES ('"+title+"','"+link+"','"+pubdate+"','"+imagelink+"','"+description+"','"+sitename+"','"+category+"');"
            dbCursor.execute(sqlInsertRow1);
            print ('Complete Insert')
        except psycopg2.IntegrityError:   
            dbSession.rollback()
        else:    
            dbSession.commit();
        dbCursor.close();
                  
                       
    except psycopg2.Error as e:
                  print (e)       
    dbSession.close()




