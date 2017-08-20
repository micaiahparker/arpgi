from pony.orm import db_session

from arpgi.models import Game

@db_session
def test_create_game():
    sample_game = {
        "schema": {},
        "title": "Test Game"
    }
    game = Game(**sample_game)
    assert game.created_date == game.last_modified
    assert game.title = sample_game['title']
    assert game.schema = sample_game['schema']
