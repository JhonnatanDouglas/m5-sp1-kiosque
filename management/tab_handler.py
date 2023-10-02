from management.product_handler import get_product_by_id
import math


def calculate_tab(orders_list: list) -> dict:

    total = 0

    for item in orders_list:
        id_order, amount_ordered = item.values()

        get_item_ordered = get_product_by_id(int(id_order))
        item_price = float(get_item_ordered['price'])

        total_item = amount_ordered * item_price
        total = total + total_item

    total_ordered = {
        'subtotal': f'${math.trunc(total * 100) / 100}'
    }

    return total_ordered
