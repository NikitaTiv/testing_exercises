from functions.level_2.three_promocodes import generate_promocode


def test__generate_promocode__value_is_set():
    assert all(
        [
            len(generate_promocode(4)) == 4, 
            generate_promocode(4).isupper(), 
            generate_promocode(4).isalpha(),
        ]
    )


def test__generate_promocode__no_value_set():
    assert all(
        [
            len(generate_promocode()) == 8,
            generate_promocode().isupper(),
            generate_promocode().isalpha(),
        ]
    )
