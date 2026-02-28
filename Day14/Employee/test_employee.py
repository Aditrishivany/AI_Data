import pytest
from employee import Employee


# =========================
# FIXTURE
# =========================

@pytest.fixture
def employee():
    # Fresh employee object for every test
    return Employee(emp_id=1, name="Aditri", salary=40000)


# =========================
# BUSINESS LOGIC TESTING
# =========================

def test_increase_salary(employee):
    assert employee.increase_salary(5000) == 45000


def test_decrease_salary(employee):
    assert employee.decrease_salary(10000) == 30000


def test_annual_salary(employee):
    assert employee.get_annual_salary() == 40000 * 12


def test_high_earner_false(employee):
    assert employee.is_high_earner() is False


# =========================
# PARAMETERIZED TESTS
# =========================

@pytest.mark.parametrize("start_salary, increase_amount, expected", [
    (30000, 5000, 35000),
    (45000, 5000, 50000),
    (10000, 10000, 20000),
])
def test_increase_salary_param(start_salary, increase_amount, expected):
    emp = Employee(2, "Test", start_salary)
    assert emp.increase_salary(increase_amount) == expected


@pytest.mark.parametrize("salary, expected", [
    (60000, True),
    (50000, True),
    (49999, False),
])
def test_is_high_earner_param(salary, expected):
    emp = Employee(3, "Param", salary)
    assert emp.is_high_earner() == expected


# =========================
# EXCEPTION TESTING
# =========================

def test_increase_salary_negative(employee):
    with pytest.raises(ValueError):
        employee.increase_salary(-500)


def test_decrease_salary_negative(employee):
    with pytest.raises(ValueError):
        employee.decrease_salary(-100)


def test_decrease_more_than_salary(employee):
    with pytest.raises(ValueError):
        employee.decrease_salary(100000)
