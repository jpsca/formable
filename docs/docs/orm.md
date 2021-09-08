
# ORM integration

HyperForm can update/create/destroy entries in your database automatically, even for the forms inside a formset.

There is built-in support por [SQLAlchemy](https://www.sqlalchemy.org/) and [PonyORM](https://ponyorm.org/) but writing your own adapter is just a few lines of code.

## SQLAlchemy

Requires that your forms:

1. Have a `_model` attribute with the Model class.
2. Inherit from `SQLAForm` instead of from `Form`.
3. Have a `_session` property or attribute that returns the database session

Example, with [SQLA-Wrapper](https://jpsca.github.io/sqla-wrapper/) or `Flask-SQLAlchemy`:

```python
from hyperform import SQLAForm, Text
from .models import dbs, MyModel, AnotherModel

class BaseForm(SQLAForm):
    # dbs is a scoped session
    _session = dbs

class MyForm(BaseForm):
    _model = MyModel
    lorem = Text()

class AnotherForm(BaseForm):
    _model = AnotherModel
    ipsum = Text()

```

## PonyORM

Requires that your forms:

1. Have a `_model` attribute with the Model class.
2. Inherit from `PonyForm` instead of from `Form`.

Example:

```python
from hyperform import PonyForm, Text
from .models import db, MyModel, AnotherModel

class BaseForm(PonyForm):
    pass

class MyForm(BaseForm):
    _model = MyModel
    lorem = Text()

class AnotherForm(BaseForm):
    _model = AnotherModel
    ipsum = Text()

```


## Writing your own adapters (a.k.a. how it works)

Your forms has three methods that an adapter can overwrite to work. These are:

```python
def create_object(self, data):
    ...

def delete_object(self):
    ...

def update_object(self, data):
    for key, value in data.items():
        setattr(self._object, key, value)
    return self._object

```

`self._object` is the original object passed as an argument. `delete_object` and `update_object` will not be called if there isn't one.

You might not need to write the three methods, in fact, the built-in adapters for SQLAlchemy an PonyORm only ovewrite the `create_object` and `delete_object` methods.

This is the *complete* (and incredible short) code for the built-in adapters:

```python
from hyperform import Form


class SQLAForm(Form):
    def create_object(self, data):
        object = self._model(**data)
        self._session.add(object)
        return object

    def delete_object(self):
        return self._session.delete(self._object)


class PonyForm(Form):
    def create_object(self, data):
        return self._model(**data)

    def delete_object(self):
        return self._object.delete()
```

Using the three methods it should be possible to write an adapter to almost *anything*, even something different than an ORM, like raw SQL, a NoSQL database, or something more exotic.
