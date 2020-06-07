from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/NewsDB"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class HeadlinesModel(db.Model):
    __tablename__ = 'TamilNews'

    title = db.Column(db.Text, primary_key=True)
    link = db.Column(db.Text)
    pubdate = db.Column(db.Text)
    imagelink = db.Column(db.Text)
    description = db.Column(db.Text)
    sitename = db.Column(db.Text)
    category = db.Column(db.Text)
    

    def __init__(self, title, link,pubdate,imagelink, description,sitename,category):
        self.title = title
        self.link = link
        self.pubdate = pubdate
        self.imagelink = imagelink
        self.description = description
        self.sitename = sitename
        self.category = category

    def __repr__(self):
        return f"<Headlines {self.title}>"
    

    

       
@app.route('/tamil/<id>', methods=['GET'])
def handle_category(id):
    
            hl = HeadlinesModel.query.filter_by(category=id).all()
            results = [
                {
                    "title": headline.title,
                    "link": headline.link,
                    "pubDate": headline.pubdate,
                    "imagelink": headline.imagelink,
                    "description": headline.description,
                    "sitename": headline.sitename,
                    "category": headline.category
                } for headline in hl]
            print (results)
            return {"count": len(results), "headlines": results}      
        
        
@app.route('/tamil', methods=['GET'])
def handle_all_category():
    
            hl = HeadlinesModel.query.all()
            results = [
                {
                    "title": headline.title,
                    "link": headline.link,
                    "pubDate": headline.pubdate,
                    "imagelink": headline.imagelink,
                    "description": headline.description,
                    "sitename": headline.sitename,
                    "category": headline.category
                } for headline in hl]
            print (results)
            return {"count": len(results), "headlines": results}   

        
if __name__ == '__main__':
    app.run(debug=True)