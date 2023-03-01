from functions.level_2.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field
import pytest


def test__fetch_extra_fields_configuration__eval_processed_argument():
    assert fetch_extra_fields_configuration('settings.ini') == {'test': eval('str')}


def test__fetch_extra_fields_configuration__eval_not_processed_argument():
    with pytest.raises(NameError):
        fetch_extra_fields_configuration('settings_3.ini')


def test__fetch_app_config_field__file_contains_extra_field_or_tool_app_config():
    assert fetch_app_config_field('settings.ini', 'extra_fields') == 'test: str'


def test__fetch_app_config_field__file_not_contains_extra_field_or_tool_app_config():
    assert fetch_app_config_field('settings_2.ini', 'extra_fields') == None
