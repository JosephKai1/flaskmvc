from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(30), nullable=False)
    

    def __init__(self, username, password):
        self.username = username

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
