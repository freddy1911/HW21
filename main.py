from courier import Courier
from request import Request
from shop import Shop
from store import Store
from exceptions import BaseError

shop = Shop(
    items={
        'собачки': 2,
        'коробки': 5
    }
)
store = Store(
    items={
        'печеньки': 3,
        'собачки': 2,
        'коробки': 5
    }
)

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    while True:
        # Содержимое склада и магазина
        for storage in storages:
            print(f'В {storage} хранится {storages[storage].get_items()}')

        # запрос от пользователя
        user_input = input(
            'Введите команду в формате "Доставить 3 печеньки из склад в магазин".\n'
            'Введите "стоп" или "stop" чтобы прервать программу\n'
        )

        if user_input == "стоп" or user_input == "stop":
            break

        try:
            request = Request(user_input, storages)

            courier = Courier(request=request, storages=storages)
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
