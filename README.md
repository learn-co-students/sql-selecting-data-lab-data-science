
# Selecting Data Lab

In this lab, we will practice querying a database with various `SELECT` statements.

## Objectives

1.  Use the `SELECT *` statement to pull all values from a table
2.  Use `SELECT` with specific `column_name(s)` to pull only certain columns from a table
3.  Use `WHERE` and conditionals to pull more specific information from a table

We will query from the same `planets` table featured in the Solar System lab.  The `planets` table is created in the `create.sql` file and already is seeded with data from the `seed.sql` file.  The relevant information is provided in the table below:

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

## Queries

Write you queries inside the `select.py` file.  To get the tests in `test/index_test.py` to pass, make sure each function returns a string containing the correct query.

* `select_all_columns_and_rows` should return all of the data featured in the `planets` table

* `select_name_and_color_of_all_planets` should return the name and color of each planet

* `select_all_planets_with_mass_greater_than_one` should return all columns for each planet whose mass is greater than 1.00


* `select_name_and_mass_of_planets_with_mass_less_than_equal_to_one` should return the name and mass of each planet whose mass is greater than or equal to 1.00

* `select_name_and_color_of_planets_with_more_than_10_moons` should return the name and color of each planets that has more than 10 moons

* `select_all_planets_with_moons_and_mass_less_than_one` should return the planet that has at least one moon and a mass less than 1.00

* `select_name_and_color_of_all_blue_planets` should return the name and color of planets that have a color of blue, light blue, or dark blue
