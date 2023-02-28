from functions.level_2.two_students import get_student_by_tg_nickname
import pytest


@pytest.mark.parametrize(
    'list_students, tg_account, expected_result',
    [
        (pytest.lazy_fixture('students'), 'PetR', pytest.lazy_fixture('student_ivanov')),
        (pytest.lazy_fixture('students'), 'Nikita', None),
    ], ids=['when there is a tg account', 'when there is no tg account']
)
def test__get_student_by_tg_nickname(tg_account, list_students, expected_result):
    assert get_student_by_tg_nickname(tg_account, list_students) == expected_result