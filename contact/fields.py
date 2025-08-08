# fields.py
from django.db import models
from utils.snowflake import generate_snowflake_id

class SnowflakeIDField(models.BigIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['primary_key'] = kwargs.get('primary_key', False)
        kwargs['editable'] = True
        kwargs['unique'] = True
        kwargs['default'] = generate_snowflake_id
        super().__init__(*args, **kwargs)