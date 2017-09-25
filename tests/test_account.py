import pytest
from exercises.oo import BankAccount, MinimumBalanceAccount


@pytest.mark.skip('Not implemented yet.')
def test_bank_account():
    account = BankAccount()
    assert hasattr(account, 'balance')
    assert account.balance == 0
    assert account.deposit(100) == 100
    assert account.withdraw(75) == 25
    assert account.withdraw(50) == -25


@pytest.mark.skip('Not implemented yet.')
def test_minimum_balance_account():
    account = MinimumBalanceAccount(100)
    assert hasattr(account, 'balance')
    assert account.balance == 0
    assert account.deposit(25) == 25
    assert account.deposit(100) == 125
    assert account.withdraw(20) == 105
    with pytest.raises(ValueError):
        account.withdraw(10)
    assert account.balance == 105


@pytest.mark.skip('Not implemented yet.')
def test_minimum_balance_account_is_subclass():
    assert issubclass(MinimumBalanceAccount, BankAccount)
