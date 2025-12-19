import os
import sys
from pathlib import Path

os.environ.setdefault("FLASK_ENV", "testing")
os.environ.setdefault("ADMIN_TOKEN", "test-token")
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest

from app import create_app
from app.extensions import db


@pytest.fixture
def app():
    app = create_app()

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def admin_headers(app):
    return {
        "X-Admin-Token": app.config["ADMIN_TOKEN"],
        "Content-Type": "application/json",
    }

