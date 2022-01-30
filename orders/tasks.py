from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'Your order was successfully created.\n' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(
        subject,
        message,
        'gatquest@gmail.com',
        [order.email],
        fail_silently=False,
)
    return mail_sent