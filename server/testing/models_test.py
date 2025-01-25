from models import Animal, Enclosure, Zookeeper  # Explicit imports for clarity


class TestAnimal:
    '''Class Animal in models.py'''

    def test_converts_to_dict(self):
        '''can convert Animal objects to dictionaries.'''
        a = Animal(id=1, name="Leo", species="Lion", age=5, zookeeper_id=None, enclosure_id=None)
        animal_dict = a.to_dict()
        assert animal_dict == {
            'id': 1,
            'name': "Leo",
            'species': "Lion",
            'age': 5,
            'zookeeper_id': None,
            'enclosure_id': None
        }
        assert isinstance(animal_dict, dict)


class TestEnclosure:
    '''Class Enclosure in models.py'''

    def test_converts_to_dict(self):
        '''can convert Enclosure objects to dictionaries.'''
        e = Enclosure(id=1, environment="Forest", open_to_visitors=True)
        enclosure_dict = e.to_dict()
        assert enclosure_dict == {
            'id': 1,
            'environment': "Forest",
            'open_to_visitors': True,
            'animals': []
        }
        assert isinstance(enclosure_dict, dict)


class TestZookeeper:
    '''Class Zookeeper in models.py'''

    def test_converts_to_dict(self):
        '''can convert Zookeeper objects to dictionaries.'''
        z = Zookeeper(id=1, name="John Doe", birthday="1990-01-01")
        zookeeper_dict = z.to_dict()
        assert zookeeper_dict == {
            'id': 1,
            'name': "John Doe",
            'birthday': "1990-01-01",
            'animals': []
        }
        assert isinstance(zookeeper_dict, dict)
