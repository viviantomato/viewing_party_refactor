import pytest
from viewing_party.person import Person


def test_1():
    # Arrange & Act
    #name = "Peggy"
    #watched =["Harry Potter", "Dune", "Ada"]
    person1 = Person("Peggy", ["Harry Potter", "Dune", "Ada"], ["Wanjun", "Tami"], ["Hulu", "HBO"])

    # Assert
    assert person1.name == "Peggy"
    assert person1.watched == ["Harry Potter", "Dune", "Ada"]
    assert person1.friends == ["Wanjun", "Tami"]
    assert person1.subscriptions == ["Hulu", "HBO"]