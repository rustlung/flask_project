from .public import public_bp
from .admin import admin_bp

def register_blueprints(app):
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)