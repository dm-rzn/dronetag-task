from django.db.models.signals import post_delete
from django.dispatch import receiver
from analytics.models import FlightAnalyticsDataset


@receiver(post_delete, sender=FlightAnalyticsDataset, dispatch_uid='post_delete_flight_analytics_dataset_cleanup')
def post_delete_cleanup_handler(sender, instance, *args, **kwargs):
    instance.telemetry.delete()
    instance.statuses.delete()
