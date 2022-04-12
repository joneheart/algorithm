shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menu_list = set(menus)
    for order in orders:
        if order not in menu_list:
            return False
        return True
    # order_list = set(orders)
    #
    # if menu_list & order_list == order_list:
    #     return True
    # else:
    #     return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
