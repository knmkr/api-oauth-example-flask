try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import pytest
from flask import url_for


class TestApp:
    def test_ping(self, client):
        res = client.get(url_for('index'))
        assert res.status_code == 200

@pytest.mark.usefixtures('live_server')
class TestLiveServer:
    def test_server_is_up_and_running(self):
        res = urlopen(url_for('index', _external=True))
        assert b'GENOME LINK' in res.read()
        assert res.code == 200
