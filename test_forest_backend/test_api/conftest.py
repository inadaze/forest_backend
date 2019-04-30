import os
import tempfile

import pytest

from forest_backend.api import app
from forest_backend.database.sql_db import db
from forest_backend.database.models.seed_model import Seed
from forest_backend.database.inserts import populate, populate_test_data


@pytest.fixture
def get_client():
    app.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jasons:password@localhost/forest_test"
    app.app.config['TESTING'] = True
    test_client = app.app.test_client()

    with app.app.app_context():
        db.create_all()
        populate(db)
        populate_test_data(db)

    yield test_client, app

    with app.app.app_context():
        db.drop_all()