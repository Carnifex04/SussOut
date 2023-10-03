# This file will initialize our Flask app and all fixtures that we need.


import pytest
from main import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

# Now, pytest will discover all our testing_data files, We can create some testing_data files with test_ prefix in the same directory.
