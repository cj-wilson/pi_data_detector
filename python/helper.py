import random
import re
import os
from faker import Faker

fake = Faker()
fake.seed(123456)

def words(n = 10):
    words = fake.words(n)
    return words

def dob():
    p = random.choices(population = ["%m/%d/%y", "%m/%d/%y", "%Y-%m-%d"],
            weights = [60, 30, 10])
    d = fake.date_between(start_date="-99y", end_date="-18y")
    return d.strftime(p.pop())

def phone():
    p = fake.phone_number()
    return re.sub('x.*$', '', p)

def name():
    return "{} {}".format(fake.first_name(), fake.last_name())

def zip_code():
    z = random.choices(population = [fake.zipcode_in_state(), 
        fake.zipcode_plus4()], weights = [80, 20])
    return z.pop() 

def gen_fake():
    choices = ['ssn', 'dob', 'phone',
            'name', 'street', 'city',
            'state', 'zip'] 

    x = random.choice(choices)

    def f(x):
        return {
                'ssn': {'value': fake.ssn(), 'label': 'ssn'},
                'dob': {'value': dob(), 'label': 'dob'},
                'phone': {'value': phone(), 'label': 'phone'},
                'name': {'value': name(), 'label': 'name'},
                'street': {'value': fake.street_address(),
                    'label': 'address'},
                'city': {'value': fake.city(), 'label': 'city'},
                'state': {'value': fake.state(), 'label': 'state'},
                'zip': {'value': zip_code(), 'label': 'zip_code'},
        }.get(x, None)

    return f(x)
