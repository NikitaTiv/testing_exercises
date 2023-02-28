import pytest

from functions.level_2.three_promocodes import generate_promocode


@pytest.mark.parametrize(
    'meaning, expected_result_num',
    [
        (4, 4),
        (None, 8),
    ],
    ids=['value_is_set', 'no_value_set']
)
def test__generate_promocode(meaning, expected_result_num):
    if meaning:
        assert all(
            [
                len(generate_promocode(meaning)) == expected_result_num, 
                generate_promocode(meaning).isupper(), 
                generate_promocode(meaning).isalpha(),
            ]
        )
    else:
        assert all(
            [
                len(generate_promocode()) == expected_result_num,
                generate_promocode().isupper(),
                generate_promocode().isalpha(),
            ]
        )
