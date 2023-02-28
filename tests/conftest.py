import datetime
from decimal import Decimal
import os
import pytest

from functions.level_1.four_bank_parser import SmsMessage, Expense, BankCard
from functions.level_2.two_students import Student


@pytest.fixture
def long_string():
    return ''.join('s' for n in range(100))


@pytest.fixture
def sms_text():
    return '1020 руб, 4400430255123326 20.02.23 16:20 7/11 authcode 3034'


@pytest.fixture
def sms_message(sms_text):
    return SmsMessage(
        text=sms_text,
        author="Sberbank",
        sent_at=datetime.datetime(2023, 2, 20, 16, 20, 20),
    )


@pytest.fixture
def bank_cards(bank_card):
    return [
        bank_card,
        BankCard(last_digits='1815', owner='Olga N.'),
        BankCard(last_digits='1855', owner='Roman G.'),
    ]

@pytest.fixture
def bank_card():
    return BankCard(
        last_digits='3326',
        owner='Nikita T.',
    )


@pytest.fixture
def expense(bank_card):
    return Expense(
        amount=Decimal('1020'),
        card=bank_card,
        spent_in='7/11',
        spent_at=datetime.datetime(2023, 2, 20, 16, 20),
    )


@pytest.fixture
def today():
    return datetime.date.today()


@pytest.fixture
def tomorrow(today):
    return today + datetime.timedelta(days=1)


@pytest.fixture
def create_text():
    def create_text_function(
            num1: str | None, num2: str | None, num3: str | None
        ) -> str:
        if num1 == None or num2 == None or num3 == None:
            return 'C:\empty_path'
        text = f'{num1}\n{num2}\n{num3}'
        with open('textfile.txt', 'w') as f:
            f.write(text)
        file_path = os.path.abspath(os.path.dirname('textfile')) + os.path.join(r'\textfile.txt')
        return file_path
    return create_text_function


@pytest.fixture
def student_petrov():
    return Student(
        first_name='Petrov', last_name='Ivan', telegram_account='@III'
    )


@pytest.fixture
def student_ivanov():
    return Student(
        first_name='Ivanov', last_name='Petr', telegram_account='@PetR'
    )


@pytest.fixture
def students(student_ivanov, student_petrov):
    return [
        student_ivanov, student_petrov
    ]
