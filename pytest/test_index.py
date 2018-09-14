import pytest
from sql_runner import SQLRunner
from sql_selects import *

sql_runner = SQLRunner()
table = sql_runner.execute_create_file()
table = sql_runner.execute_seed_file()

def test_select_all_columns_and_rows():
    result = [(1, 'Mercury', 'gray', 0, 0.55, 0.0), (2, 'Venus', 'yellow', 0, 0.82, 0.0), (3, 'Earth', 'blue', 1, 1.0, 0.0), (4, 'Mars', 'red', 2, 0.11, 0.0), (5, 'Jupiter', 'orange', 67, 317.9, 0.0), (6, 'Saturn', 'hazel', 62, 95.19, 1.0), (7, 'Uranus', 'light blue', 27, 14.54, 1.0), (8, 'Neptune', 'dark blue', 14, 17.15, 1.0)]
    assert table.execute(select_all_columns_and_rows()).fetchall() == result

def test_select_name_and_color_of_all_planets():
    result = [('Mercury', 'gray'), ('Venus', 'yellow'), ('Earth', 'blue'), ('Mars', 'red'), ('Jupiter', 'orange'), ('Saturn', 'hazel'), ('Uranus', 'light blue'), ('Neptune', 'dark blue')]
    assert table.execute(select_name_and_color_of_all_planets()).fetchall() == result

def test_select_all_planets_with_mass_greater_than_one():
    result = [(5, 'Jupiter', 'orange', 67, 317.9, 0.0), (6, 'Saturn', 'hazel', 62, 95.19, 1.0), (7, 'Uranus', 'light blue', 27, 14.54, 1.0), (8, 'Neptune', 'dark blue', 14, 17.15, 1.0)]
    assert table.execute(select_all_planets_with_mass_greater_than_one()).fetchall() == result

def test_select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    result = [('Mercury', 0.55), ('Venus', 0.82), ('Earth', 1.0), ('Mars', 0.11)]
    assert table.execute(select_name_and_mass_of_planets_with_mass_less_than_equal_to_one()).fetchall() == result

def test_select_name_and_color_of_planets_with_more_than_10_moons():
    result = [('Jupiter', 'orange'), ('Saturn', 'hazel'), ('Uranus', 'light blue'), ('Neptune', 'dark blue')]
    assert table.execute(select_name_and_color_of_planets_with_more_than_10_moons()).fetchall() == result

def test_select_all_planets_with_moons_and_mass_less_than_one():
    result = [(4, 'Mars', 'red', 2, 0.11, 0.0)]
    assert table.execute(select_all_planets_with_moons_and_mass_less_than_one()).fetchall() == result

def test_select_name_and_color_of_all_blue_planets():
    result = [('Earth', 'blue'), ('Uranus', 'light blue'), ('Neptune', 'dark blue')]
    assert table.execute(select_name_and_color_of_all_blue_planets()).fetchall() == result
