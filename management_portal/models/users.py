from ..utils import db
from datetime import datetime

class User(db.Model ):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    identifier = db.Column(db.String(50), unique=True , nullable=False )
    first_name = db.Column(db.String(50), nullable=False )
    last_name = db.Column(db.String(50), nullable=False )
    email =  db.Column( db.String(60) , nullable=False , unique=True )
    password_hash = db.Column(db.String(70) , nullable=False )
    password_reset_token = db.Column(db.String(70) , nullable=True )
    created_at = db.Column(db.DateTime() , nullable=False , default=datetime.utcnow)

    
    def __repr__(self):
        return f"<User {self.username}>"

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)
