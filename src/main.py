import os.path
from src.utils import load_json, get_filtered_list, get_sorted_list, print_message
from config import ROOT_DIR

PATH_TO_OPERATIONS = os.path.join(ROOT_DIR, "src", "operations.json")


def main():
    response=load_json(PATH_TO_OPERATIONS)
    filtered_list=get_filtered_list(response)
    sorted_list=get_sorted_list(filtered_list)
    for operation in sorted_list[:5]:
        print_message(operation)


if __name__ == "__main__":
    main()
