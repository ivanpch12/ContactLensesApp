import threading
import time


def send_order_notification(order):
    time.sleep(2)
    print(f'Order {order.id} processed and notification sent.')

def send_order_notification_async(order_id):
    thread = threading.Thread(
        target=send_order_notification,
        args=(order_id,)
    )
    thread.start()