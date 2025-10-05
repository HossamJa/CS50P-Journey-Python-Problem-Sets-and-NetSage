import sys
from datetime import date
import inflect
p = inflect.engine()


def main():
    print(get_date(input('Date of Birth: ')))


def get_date(birth_date):
        return age_in_min(birth_date.strip())


def age_in_min(birth_date):
    try:
        age = date.today() - date.fromisoformat(birth_date)
        age = age.days * 24 * 60
        return f'{p.number_to_words(age, andword='').capitalize()} minutes'
    except ValueError:
            sys.exit('Invalid date')




if __name__ == "__main__":
    main()
