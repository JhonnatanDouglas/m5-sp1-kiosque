from menu import products


def get_product_by_id(id_param: int) -> dict:

    founded_product = {}
    empty_product = {}

    if type(id_param) != int:
        raise TypeError('product id must be an int')

    for item in products:

        value = list(item.values())
        id_value = int(value[0])

        if id_value == id_param:
            founded_product = item

    if founded_product:
        return founded_product
    else:
        return empty_product


def get_products_by_type(type_param: str) -> list:

    founded_product_list = []
    empty_product_list = []

    if type(type_param) != str:
        raise TypeError('product type must be a str')

    for item in products:

        value = list(item.values())
        title_value = value[5]

        if title_value == type_param:
            founded_product_list.append(item)

    if founded_product_list:
        return founded_product_list
    else:
        return empty_product_list


def add_product(menu: list, **kwargs: dict) -> list:

    new_id = 0
    last_id_product = 0
    total_in_list = int(len(menu))

    if total_in_list <= 0:
        new_id = 1
    else:
        for product in menu:
            last_id_product = int(product['_id'])

            if last_id_product > new_id:
                new_id = last_id_product + 1

    new_product = dict({'_id': new_id}, **kwargs)

    menu.append(new_product)
    return new_product


def menu_report() -> str:

    total_products_menu = int(len(products))
    media_menu = 0
    total_price_menu = 0
    most_common_type = ''
    item_list = 0

    for item in products:
        price_value = float(item['price'])
        total_price_menu = total_price_menu + price_value

        type_product = str(item['type'])
        total_type = int(len(get_products_by_type(type_product)))

        if total_type > item_list:
            item_list = total_type
            most_common_type = type_product

    media_menu = total_price_menu / total_products_menu
    product_media_menu = round(media_menu, 2)

    return f'Products Count: {total_products_menu} - Average Price: ${product_media_menu} - Most Common Type: {most_common_type}'
