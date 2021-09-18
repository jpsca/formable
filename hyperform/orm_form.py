from .form import Form


__all__ = ("PonyForm", "SQLAForm")


class PonyForm(Form):
    def create_object(self, data):
        return self._model(**data)


class SQLAForm(Form):
    def create_object(self, data):
        object = self._model(**data)
        self._session.add(object)
        self._session.flush()
        return object
