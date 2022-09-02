from tests.application.app import d

class Colleges(d.Model):
    college_id=d.Column(d.Integer,nullable=False,primary_key=True)
    college_name=d.Column(d.String(100),nullable=False)
    address=d.Column(d.String(1000),nullable=False)
    director_name=d.Column(d.String(20),nullable=True)
    programs=d.relationship('Programs',backref='all_programs')

class Programs(d.Model):
    program_id=d.Column(d.Integer,nullable=False,primary_key=True)
    program_name=d.Column(d.String(100),nullable=False)
    fees=d.Column(d.Integer,nullable=False)
    college_id=d.Column(d.Integer,d.ForeignKey('colleges.college_id'),nullable=False)   