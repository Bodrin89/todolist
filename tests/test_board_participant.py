
import logging

import pytest

from apps.goals.serializer import BoardParticipantSerializer
from tests.factories import BoardParticipantFactory

logger = logging.getLogger('main')


@pytest.mark.django_db
class TestBoardParticipant:

    def test_added_participants(self, get_auth_client, board):

        participants = BoardParticipantFactory.create_batch(3, board=board)
        part = BoardParticipantSerializer(participants, many=True)
        # TODO role = 1 проходит валидацию в сериализаторе

        logger.debug(part.data)
