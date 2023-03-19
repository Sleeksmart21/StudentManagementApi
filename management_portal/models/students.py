from ..utils import db
from datetime import datetime
from ..models.users import User


class Student(User):
    __tablename__ = 'students'

    id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    Reg_no = db.Column(db.String(50), nullable=False )
    courses =  db.relationship( 'Course' , secondary='student_course')
    score = db.relationship('Score', back_populates='student_score', lazy=True)
    
    def __repr__(self):
        return f"<User {self.username}>"

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)
