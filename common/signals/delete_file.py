from django.db.models.signals import post_delete
from django.dispatch import receiver
from common.models import Dataset


for subclass in Dataset.__subclasses__():
    @receiver(post_delete, sender=subclass, dispatch_uid=f'post_delete_{subclass._meta.model_name}_file_delete')
    def post_delete_cleanup_file_handler(sender, instance, *args, **kwargs):
        instance.data.delete()
