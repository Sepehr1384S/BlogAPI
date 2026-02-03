from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField
from django.conf import settings



class Post(Model):
    title = CharField(max_length=50)
    body = TextField()
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


