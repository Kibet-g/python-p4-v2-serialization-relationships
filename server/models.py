from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Zookeeper(db.Model, SerializerMixin):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    animals = db.relationship('Animal', back_populates='zookeeper', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthday": str(self.birthday),
            "animals": [animal.id for animal in self.animals] if self.animals else []
        }


class Enclosure(db.Model, SerializerMixin):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String, nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False, default=True)

    animals = db.relationship('Animal', back_populates='enclosure', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "environment": self.environment,
            "open_to_visitors": self.open_to_visitors,
            "animals": [animal.id for animal in self.animals] if self.animals else []
        }


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)
    age = db.Column(db.Integer)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    enclosure = db.relationship('Enclosure', back_populates='animals')
    zookeeper = db.relationship('Zookeeper', back_populates='animals')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "zookeeper_id": self.zookeeper_id,
            "enclosure_id": self.enclosure_id
        }

    def __repr__(self):
        return f'<Animal {self.name}, a {self.species}>'
