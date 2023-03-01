from functions.level_2.four_lines_counter import count_lines_in
import pytest


@pytest.mark.parametrize(
    'mutable_argument, expected_result',
    [
        ('#', 2),
        ('2', 3),
        (None, None),
    ], 
    ids=[
        'correctly_counts_rows_with_lattice',
        'correctly_counts_rows_without_lattice',
        'handles_bad_links_correctly',
    ],
)
def test__count_lines_in(create_text, mutable_argument, expected_result):
    assert count_lines_in(create_text('1', mutable_argument, '1')) == expected_result
