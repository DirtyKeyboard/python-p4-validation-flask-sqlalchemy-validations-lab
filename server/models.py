from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, val):
        if len(val) == 0:
            raise ValueError("NO!!")
        return val

    @validates('phone_number')
    def validate_number(self, key, val):
        if len(val) != 10:
            raise ValueError("d")
        return val

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
"""
Post content is at least 250 characters long.
Post summary is a maximum of 250 characters.
"""
class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, val):
        if len(val) == 0 or "top" not in val.lower() or "guess" not in val.lower() or "secret" not in val.lower() or "won't believe" not in val.lower():
            raise ValueError("d")
        return val
    
    @validates('category')
    def validate_category(self, key, val):
        if val.lower() == 'fiction' or val.lower() == 'non-fiction':
            return val
        else:
            raise ValueError("nope")
        
    @validates('content')
    def validate_content(self, key, val):
        if len(val) < 250:
            raise ValueError("no")
        return val
            

    @validates('summary')
    def validate_summary(self, key, val):
        if len(val) >= 250:
            raise ValueError("no")
        return val
            

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
