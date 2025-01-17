from rest_framework.serializers import ValidationError



class UnsolicitedLinksValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        data_serializers = dict(value).get(self.field)

        if not data_serializers:
            return None
        elif "youtube" not in data_serializers:
            raise ValidationError(f"The field must '{data_serializers}' contain a valid YouTube link")

        return True
