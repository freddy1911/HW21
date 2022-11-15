class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    message = 'недостаточно места'


class UnknownProductError(BaseError):
    message = 'неизвестный товар'


class NotEnoughProductError(BaseError):
    message = 'недостаточно товара'


class InvailidRequestError(BaseError):
    message = 'неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'неизвестный склад'


class TooMuchNamesError(BaseError):
    message = 'слишком много наименований'
