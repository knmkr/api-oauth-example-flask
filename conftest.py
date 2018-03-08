import os
import pytest
from app import create_app


@pytest.fixture
def app():
    os.environ['GENOMELINK_CLIENT_ID'] = 'x'
    os.environ['GENOMELINK_CLIENT_SECRET'] = 'x'
    os.environ['GENOMELINK_CALLBACK_URL'] = 'x'
    app = create_app()
    app.debug = True
    return app
