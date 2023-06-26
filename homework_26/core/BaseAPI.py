from homework_26.core.Singleton import Singleton


class BaseAPI(Singleton):
    base_url = "https://petstore.swagger.io/v2/"
    headers = {"Content-Type": "application/json"}
