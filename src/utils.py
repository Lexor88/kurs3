import json
from datetime import datetime


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_filtered_list(list_with_dict):
    filtered_list = []
    for dictionary in list_with_dict:
        if dictionary and dictionary["state"] == "EXECUTED":
            filtered_list.append(dictionary)
    return filtered_list
def get_sorted_list(list_with_dict):
    return sorted(list_with_dict, key=lambda x: x["date"], reverse=True)

def print_source_correct(info_about_source):
    """
    :param info_about_source: содержит строку с описанием источника(карта или счет) и его номер
    :return: готовое, отредактированное сообщение с замаскированными элементами номера
    """
    if not info_about_source.startswith("Счет"):
        number = info_about_source[-16:]
        first_block = f"{number[:4]}"
        second_block = f"{number[4:6]}**"
        third_block = "****"
        fourth_block = f"{number[-4:]}"
        return f"{info_about_source[:-16]}{first_block} {second_block} {third_block} {fourth_block}"
    else:
        return f"Счет **{info_about_source[-4:]}"
def print_message(operation):
    date = datetime.fromisoformat(operation['date'])
    date = date.strftime('%d.%m.%Y')
    description = operation['description']
    from_info = operation.get('from')
    to_info = operation['to']
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    print(f"{date} {description}")
    if from_info:
        print(f"{print_source_correct(from_info)} -> {print_source_correct(to_info)}")
    else:
        print(f"{print_source_correct(to_info)}")
    print(f"{amount} {currency}\n")
