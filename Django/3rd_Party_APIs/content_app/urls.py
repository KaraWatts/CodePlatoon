from django.urls import path
from .views import Moderator
from urllib import parse
from django.urls import converters, register_converter


class URLDecodeConverter:
    regex = r".+"
    def to_python(self, value):
        # Perform URL decoding
        decoded_value = parse.unquote(value)
        return decoded_value

register_converter(URLDecodeConverter, "url_to_str")

urlpatterns = [
    path('<url_to_str:image>/', Moderator.as_view(), name="moderator"),
]