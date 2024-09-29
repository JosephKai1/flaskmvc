from App.database import db

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(30), nullable=False)

    def __init__(self, companyName):
        self.companyName = companyName

    def __repr__(self):
        return f'<Employer {self.id} - {self.companyName}>'