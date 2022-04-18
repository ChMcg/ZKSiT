
from other.enum_helper import inc


class Identifier():
    _id: int
    name: str

    def __init__(self, name: str) -> None:
        self._id = inc("Identifier")
        self.name = name


class IdentifierAlreadyCreatedError(BaseException):
    pass


class IdentifierCache():
    cached_ids: set[int] = {}
    cached_names: set[str] = {}
    cached_list: list[Identifier] = []

    def append(self, identifier: Identifier):
        if identifier.name in self.cached_names:
            raise IdentifierAlreadyCreatedError()        

        self.cached_ids.add(identifier._id)
        self.cached_names.add(identifier.name)
        self.cached_list.append(identifier)


class IdentifierFactory():
    cache_id_on_create: bool = False
    cache: IdentifierCache = IdentifierCache()

    @staticmethod
    def set_use_cache(use_cache: bool):
        IdentifierFactory.cache_id_on_create = use_cache

    @staticmethod
    def create_identifier(name: str) -> Identifier:
        new_identifier_obj = Identifier(name)
        if IdentifierFactory.cache_id_on_create: 
            IdentifierFactory.cache.append(new_identifier_obj)
        return new_identifier_obj


