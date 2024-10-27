import pytest
from multiprocessing import Process
from server import app
from video_translation_client import VideoTranslationClient

def run_server():
    app.run(port=8000)

@pytest.fixture(scope='module', autouse=True)
def server():
    server_process = Process(target=run_server)
    server_process.start()
    yield
    server_process.terminate()

def test_video_translation_client(server):
    client = VideoTranslationClient("http://localhost:8000")
    client.check_status()
