from functions.level_2.two_students import get_student_by_tg_nickname
import pytest


@pytest.mark.parametrize(
    'tg_account, expected_result',
    [
        ('PetR', pytest.lazy_fixture('student_ivanov')),
        ('Nikita', None),
    ], 
    ids=[
        'when there is a tg account',
        'when there is no tg account',
    ],
)
def test__get_student_by_tg_nickname(tg_account, students, expected_result):
    assert get_student_by_tg_nickname(tg_account, students) == expected_result