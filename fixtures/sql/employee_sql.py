
employee_sql = """
insert into employee (name, birthdate, hire_date, salary, status) 
values (%(name)s, %(birthdate)s, %(hire_date)s,
%(salary)s, %(status)s)
"""
