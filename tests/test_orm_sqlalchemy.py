import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import hyperform as f


engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


Base.metadata.create_all(engine)


class PersonForm(f.SQLAForm):
    _model = Person

    name = f.Text(required=True)
    age = f.Integer(required=True)


@pytest.fixture(scope="session")
def session():
    _session = Session()
    yield _session
    _session.close()


def test_orm_save(session):
    input_data = {
        "name": "Jesse Montgomery III",
        "age": 23,
    }
    form = PersonForm(input_data)
    form._session = session

    assert form.validate()

    obj = form.save()
    session.commit()

    assert isinstance(obj, Person)
    assert obj.name == input_data["name"]


def test_orm_save_update(session):
    input_data = {
        "name": "John",
        "age": 20,
    }

    p1 = Person(name="John", age=20)
    session.add(p1)
    session.commit()

    form = PersonForm(input_data, p1)
    form._session = session

    assert form.validate()
    obj = form.save()
    session.commit()

    assert isinstance(obj, Person)
