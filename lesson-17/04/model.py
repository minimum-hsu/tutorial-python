from pynamodb.attributes import NumberAttribute
from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class User(Model):
    """
    A DynamoDB User
    """

    class Meta:
        table_name = 'user'
        region = 'us-west-1'

    email = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    age = NumberAttribute()
