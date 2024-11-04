from rest_framework.serializers import ValidationError

allowed_link = ("https://www.youtube.com/watch",)


class VideoLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if allowed_link not in value:
            raise ValidationError('Ссылка должна быть на ютуб')
