from app.extensions import db
from .mixins import TimestampMixin

class Experience(TimestampMixin, db.Model):
    __tablename__ = 'experience'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    category = db.Column(db.Enum('project', 'role', 'certificate'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    highlights = db.Column(db.JSON, nullable=True)
    tags = db.Column(db.JSON, nullable=True)
    public = db.Column(db.Boolean, default=True, nullable=False)
    link = db.Column(db.String(255), nullable=True)
    