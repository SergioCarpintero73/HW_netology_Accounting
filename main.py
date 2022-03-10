from datetime import date
from Application.salary import calculate_salary
from Application.db.people import get_employees


if __name__ == '__main__':
    print(f'{date.today()}')
    calculate_salary()
    get_employees()