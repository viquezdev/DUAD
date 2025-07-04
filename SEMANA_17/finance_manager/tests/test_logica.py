import pytest
from finance_manager.logic.transaction import Transaction
from finance_manager.logic.category import Category
from finance_manager.logic.finance_manager import FinanceManager


def test_transaction_valid():
    object_transaction = Transaction("income", "Salary", "1200", "Salary")
    assert object_transaction.to_list() == ["Salary", "1200", "Salary", "income"]


def test_transaction_invalid_type():
    with pytest.raises(ValueError):
        Transaction("gift", "Bonus", 500, "Other")


def test_transaction_invalid_amount_type():
    with pytest.raises(TypeError):
        Transaction("income", "Salary", "mil", "Salary")


def test_add_category():
    object_category = Category()
    object_category.add_new_category("Food")
    assert object_category.get_categories() == ["Food"]

def test_no_duplicate_categories():
    object_category= Category(["Food"])
    object_category.add_new_category("Food")
    assert object_category.get_categories() == ["Food"]


def test_extract_attributes_empty():
    object_finance_manager = FinanceManager()
    params = object_finance_manager.extract_attributes(object_finance_manager.transactions)
    assert params == []


def test_create_list_of_categories():
    object_finance_manager = FinanceManager()
    object_finance_manager.add_income("Bono", 400, "Work")
    object_finance_manager.add_expense("Groceries", 100, "Food")
    object_finance_manager.create_list_of_categories(object_finance_manager.transactions)
    assert object_finance_manager.categories == ["Work", "Food"]


def test_add_income_transaction():
    object_finance_manager = FinanceManager()
    object_finance_manager.add_income("Bono", 400, "Work")
    assert len(object_finance_manager.transactions) == 1
    assert object_finance_manager.transactions[0].transaction_type == "income"


def test_add_expense_transaction():
    object_finance_manager = FinanceManager()
    object_finance_manager.add_expense("Rent", 700, "Home")
    assert len(object_finance_manager.transactions) == 1
    assert object_finance_manager.transactions[0].transaction_type == "expense"