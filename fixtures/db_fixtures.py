import pytest
import psycopg2

@pytest.fixture
def cursor():
    conn = psycopg2.connect('host=localhost dbname=test_db user=postgres password=XXXXXXXX')
    cur = conn.cursor()
    yield cur
