import pytest
from viewing_party.movie import Movie

def test_update_rating():
    # Arrange
    movie = Movie("Gone with the wind", "Classical", 9.5, "HBO")

    # Act   
    rating = movie.update_rating(100)
    
    # Assert
    assert rating == 100
    