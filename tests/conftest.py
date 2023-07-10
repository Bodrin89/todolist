from pytest_factoryboy import register

from tests.factories import BoardFactory, BoardParticipantFactory, UserFactory

pytest_plugins = 'tests.fixtures'


register(UserFactory)
register(BoardFactory)
register(BoardParticipantFactory)
