from src.utils import load_json, get_filtered_list, get_sorted_list, print_message


def main():
    response=load_json("operations.json")
    filtered_list=get_filtered_list(response)
    sorted_list=get_sorted_list(filtered_list)
    for operation in sorted_list[:5]:
        print_message(operation)


if __name__ == "__main__":
    main()
