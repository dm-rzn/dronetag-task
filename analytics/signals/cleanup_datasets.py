from django.db.models.signals import post_delete
from django.dispatch import receiver
from analytics.models import FlightAnalyticsDataset


@receiver(post_delete, sender=FlightAnalyticsDataset)
def post_delete_cleanup_handler(sender, instance, *args, **kwargs):
    instance.telemetry.delete()
    instance.statuses.delete()
