import math

import pytest
from kreis_funktion import calc_area
from kreis_funktion import calc_diameter
from kreis_funktion import circumference


def test_durchmesser():
    assert calc_diameter(5) == 10
    assert calc_diameter(0) == 0
    assert calc_diameter(2.5) == 5.0


def test_umfang():
    # approx statt ==, da math.pi nur eine Annäherung ist und Multiplikation damit
    # winzige Rundungsfehler erzeugen kann
    assert circumference(1) == pytest.approx(2 * math.pi)
    assert circumference(0) == pytest.approx(0)
    assert circumference(5) == pytest.approx(2 * math.pi * 5)
    with pytest.raises(TypeError):
        circumference("Irgendein Text, statt einer Zahl.")


def test_flaeche():
    # gleicher Grund wie oben: math.pi macht == unzuverlässig, wegen winziger Rundungsfehler
    assert calc_area(1) == pytest.approx(math.pi)
    assert calc_area(0) == pytest.approx(0)
    assert calc_area(3) == pytest.approx(3**2 * math.pi)
