
import psycopg2




dbSession       = psycopg2.connect(user="postgres",
                               password="password",
                               host="localhost",
                               port="5432",
                               database="NewsDB")
 #link_var = link
dbCursor = dbSession.cursor();
 
 #with open("data_file.json", "w") as write_file:
  #json.dump(payload, write_file)
# with open("data_file.json", "r") as read_file:
  #payload1 = json.load(read_file)
  
 #sqlCreateTable  = "CREATE TABLE public.test2(title_feed text, link_feed text, payload_feed json[]);"
sqlCreateTable  = "CREATE TABLE public.\"TamilNews\"(title text NOT NULL,link text,pubdate text,imagelink text,description text,sitename text,category text NOT NULL,CONSTRAINT PK_TamilNews PRIMARY KEY (title,category))";
dbCursor.execute(sqlCreateTable);
dbSession.commit();
dbCursor.close();
dbSession.close();
    
    