import pytest
from count import Count
from ascii_games import bit


def test_count_counts():
    count = Count(model=0)
    count.cycle()
    count.cycle()
    count.cycle()
    assert count.display == [[bit(3, 'MAGENTA')]]
    count.run()
    assert count.display == [[bit(60, 'RED')]]