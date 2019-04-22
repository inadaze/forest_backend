import os
import tempfile

import pytest

from forest_backend.api import app
from forest_backend.database.sql_db import db
from forest_backend.database.models.seed_model import Seed


@pytest.fixture
def client():
    app.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jasons:password@localhost/forest_test"
    app.app.config['TESTING'] = True
    test_client = app.app.test_client()

    with app.app.app_context():
        db.create_all()
        seed = Seed(word="floral")
        db.session.add(seed)
        db.session.commit()

    yield test_client

    with app.app.app_context():
        db.drop_all()
