from exceptions import InvailidRequestError, UnknownStorageError


class Request:
    def __init__(self, user_input, storages: dict):
        split_request = user_input.lower().split(' ')
        if len(split_request) != 7 or not split_request[1].isdigit():
            raise InvailidRequestError

        self.quantity = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.destination not in storages and self.departure not in storages:
            raise UnknownStorageError
