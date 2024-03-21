import os
from config import ROOT_DIR
from src.utils import get_filtered_list, print_message
from src.utils import get_sorted_list
from src.utils import load_json
from src.utils import print_source_correct


def test_load_json():
    assert load_json(os.path.join(ROOT_DIR, 'tests', 'operations_for_tests.json'))[:1] == [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]


def test_get_filtered_list(list_with_dict):
    assert get_filtered_list(list_with_dict)[0] == {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }


def test_get_sorted_list(list_with_dict):
    assert get_sorted_list(get_filtered_list(list_with_dict))[0] == {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        }


def test_check_source(list_with_dict):
    assert print_source_correct(list_with_dict[0]['from']) == "Maestro 1308 79** **** 7170"
    assert print_source_correct(list_with_dict[0]['to']) == "Счет **8612"


def test_print_message(list_with_dict):
    assert print_message(list_with_dict[0]) is None
    assert print_message(list_with_dict[1]) is None
