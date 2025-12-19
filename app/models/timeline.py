from app.extensions import db
from .mixins import TimestampMixin

class Timeline(TimestampMixin, db.Model):
    __tablename__ = 'timeline'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.Enum('learning', 'project', 'role', 'certificate'), nullable=True, default=None)
    highlight = db.Column(db.Boolean, default=False, nullable=True)
    order = db.Column(db.Integer, nullable=True, default=None)

