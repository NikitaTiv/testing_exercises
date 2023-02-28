from functions.level_2.four_lines_counter import count_lines_in
import pytest


@pytest.mark.parametrize(
    'filepath, first_row, second_row, third_row, expected_result',
    [
        (pytest.lazy_fixture('create_text'), '1', '#', '1', 2),
        (pytest.lazy_fixture('create_text'), '1', '2', '1', 3),
        (pytest.lazy_fixture('create_text'), '1', None, '1', None),
    ], 
    ids=[
        'correctly_counts_rows_with_lattice', 'correctly_counts_rows_without_lattice',
        'handles_bad_links_correctly',
    ],
)
def test__count_lines_in(filepath, first_row, second_row, third_row, expected_result):
    assert count_lines_in(filepath(first_row, second_row, third_row)) == expected_result
