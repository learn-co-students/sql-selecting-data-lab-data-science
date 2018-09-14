
# Selecting Data Lab

## Introduction
In this lab, we will practice querying a database with various `SELECT` statements. We will select different columns, and employ other SQL clauses like `WHERE` to return the data we would like.

## Objectives

1.  Use the `SELECT *` statement to pull all values from a table
2.  Use `SELECT` with specific `column_name(s)` to pull only certain columns from a table
3.  Use `WHERE` and conditionals to pull more specific information from a table

We will be querying data from the `planets` table we see below, which is also featured in the Solar System lab. The `planets` table is created in the `create.sql` file and already seeded with data from the `seed.sql` file. The table's data and structure is provided below:

|name   |color |num_of_moons|mass|rings|
|-------|-------|-------|-------|-------|
|Mercury|gray   |0      |0.55   |no     |
|Venus  |yellow |0      |0.82   |no     |
|Earth  |blue   |1      |1.00   |no     |
|Mars   |red    |2      |0.11   |no     |
|Jupiter|orange |67     |317.90 |no     |
|Saturn |hazel  |62     |95.19  |yes    |
|Uranus |light blue|27  |14.54  |yes    |
|Neptune|dark blue|14   |17.15  |yes    |

## Instructions

Write your queries inside the `sql_selects.py` file.  To get the tests in `test/index_test.py` to pass, add the correct SQL query to the empty string returned in each function. See the example below.

```python
def select_example_func():
    return "SQL SELECT STATEMENT GOES HERE"
```

* `select_all_columns_and_rows` should return all of the data featured in the `planets` table

* `select_name_and_color_of_all_planets` should return the name and color of each planet

* `select_all_planets_with_mass_greater_than_one` should return all columns for each planet whose mass is greater than 1.00


* `select_name_and_mass_of_planets_with_mass_less_than_equal_to_one` should return the name and mass of each planet whose mass is greater than or equal to 1.00

* `select_name_and_color_of_planets_with_more_than_10_moons` should return the name and color of each planets that has more than 10 moons

* `select_all_planets_with_moons_and_mass_less_than_one` should return the planet that has at least one moon and a mass less than 1.00

* `select_name_and_color_of_all_blue_planets` should return the name and color of planets that have a color of blue, light blue, or dark blue

## Summary

Great work! In this lab we practiced writing select statements that query a single table to get specific information and used other clauses and specified column names to cherry pick the data we wanted to retrieve. 
