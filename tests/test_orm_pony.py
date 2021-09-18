try:
    from pony import orm
except ImportError:
    orm = None

import hyperform as f


if orm:
    db = orm.Database()

    class Person(db.Entity):
        name = orm.Required(str)
        age = orm.Required(int)

    db.bind(provider="sqlite", filename=":memory:")
    db.generate_mapping(create_tables=True)
    orm.set_sql_debug(True)

    class PersonForm(f.PonyForm):
        _model = Person

        name = f.Text(required=True)
        age = f.Integer(required=True)

    @orm.db_session
    def test_orm_save():
        input_data = {
            "name": "Jesse Montgomery III",
            "age": 23,
        }
        form = PersonForm(input_data)

        assert form.validate()
        obj = form.save()
        assert isinstance(obj, Person)
        assert obj.name == input_data["name"]

    @orm.db_session
    def test_orm_save_update():
        input_data = {
            "name": "John",
            "age": 20,
        }

        p1 = Person(name="John", age=20)
        orm.commit()

        form = PersonForm(input_data, p1)

        assert form.validate()
        obj = form.save()
        assert isinstance(obj, Person)
