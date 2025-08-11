import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings
from snowflake import snowflake

from snowflake import generate_snowflake_id

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        code = generate_snowflake_id()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone_number = fake.phone_number()
        created_at: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                code=code,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                created_at=created_at,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)