from django.utils.text import slugify

def unique_slug_generator(model_instance,user_name,slug_field):
    slug = slugify(user_name)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug