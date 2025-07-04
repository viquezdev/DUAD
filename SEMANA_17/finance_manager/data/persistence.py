import csv
from finance_manager.logic.transaction import Transaction


def import_data_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file,delimiter='\t')
            list_of_transactions=[Transaction(**row) for row in reader]
            return list_of_transactions
    except FileNotFoundError as ex:
        print(f"The file does not exist.Error{ex}")   


def export_data_to_csv(file_path, data, headers):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers,delimiter='\t')
            writer.writeheader()
            for manager in data:
                writer.writerow(vars(manager))
    except FileNotFoundError as ex:
        print(f"The directory does not exist..Error{ex}")  