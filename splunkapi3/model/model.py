class Model(object):
    name_map = {}

    def map(self, key: str) -> str:
        return self.name_map.get(key) or key

    @property
    def dict(self) -> dict:
        return {map(k): v for k, v in self.__dict__.items() if v is not None}


