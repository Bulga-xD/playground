from typing import List


from pydantic import BaseModel, validator


class BankTransaction(BaseModel):
    amount: float
    description: str


class BankAccount(BaseModel):
    account_number: int
    balance: float
    transaction_history: List[BankTransaction] = []

    def deposit(self, amount):
        self.balance = amount
        self.transaction_history.append(
            BankTransaction(amount=amount, description='Deposit'))

    @validator('account_number')
    def account_number_must_not_be_negative(cls, v):
        if v < 100:
            raise ValueError('Must not be negative')
        return v

    def withdraw(self, amount):
        if amount >= self.balance:
            raise ValueError('Not enough funds')
        self.balance -= amount
        self.transaction_history.append(
            BankTransaction(amount=amount, description='Withdrawal'))

    def get_transaction_history(self):
        print(f"Current balance: ${self.balance}")
        for transaction in self.transaction_history:
            print(f"{transaction.description} - ${transaction.amount}")
