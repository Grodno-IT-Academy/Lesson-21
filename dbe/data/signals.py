from django.core.signals import request_finished
from django.dispatch import receiver
from .models import Request


@receiver(request_finished)
def finished_request(sender, **kwargs):
    print("REQUEST FINISHED")
    # Request.object.create()