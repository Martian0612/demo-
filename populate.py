import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo.settings")

import django
django.setup()

import random
from app1.models import Employee
from faker import Faker

fake = Faker()

def populate(value):
    for i in range(value):
        eid = random.randint(1,188)
        ename = fake.name()
        city = fake.city()
        esal = random.randint(15000,80000)

        obj = Employee.objects.get_or_create(eid = eid, ename = ename, city = city , esal = esal)

def main():
    no = int(input("how many records you want to send: "))
    populate(no)

if __name__ == "__main__":
    main()