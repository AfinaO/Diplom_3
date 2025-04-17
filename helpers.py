# Additional instruments
from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_email():
    email = fake.free_email()
    return email


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_name():
    username = fakeRU.first_name()
    return username


# Create user account data
def get_user_data():
    return {
        'name': create_random_name(),
        'password': create_random_password(),
        'email': create_random_email()
    }


