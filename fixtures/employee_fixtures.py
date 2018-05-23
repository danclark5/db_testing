import pytest
from .db_fixtures import cursor
from .sql.employee_sql import employee_sql

@pytest.fixture
def red_dan_clark(cursor):
    cursor.execute(employee_sql, {'name':'Dan Clark', 
                                  'birthdate':'19850305', 
                                  'hire_date':'20121227', 
                                  'salary':500,
                                  'status':'Active'})

@pytest.fixture
def red_natalie_clark(cursor):
    cursor.execute(employee_sql, {'name':'Natalie Clark', 
                                  'birthdate':'19850305', 
                                  'hire_date':'20121227', 
                                  'salary':5000,
                                  'status':'Active'})

