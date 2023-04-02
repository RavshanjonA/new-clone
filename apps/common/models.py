from django.db.models import Model, SlugField, DateTimeField


class Base(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True
