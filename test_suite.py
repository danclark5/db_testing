from fixtures.db_fixtures import cursor
from fixtures.employee_fixtures import red_dan_clark, red_natalie_clark

def test_first_test(cursor, red_dan_clark, red_natalie_clark):
    cursor.execute("""begin;
select total_salaries_greater_than('test', cast(600.00 as money));

fetch all in "test";
""")
    rs = cursor.fetchall()
    for r in rs:
        print(r)
    assert len(rs) == 1 


