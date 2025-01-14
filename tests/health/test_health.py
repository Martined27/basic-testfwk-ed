import requests
from config import LOG

def test_health():
    LOG.info("test_health")
    response = requests.get("http://host.docker.internal:8080/health")
    assert response.ok 
    