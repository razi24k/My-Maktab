import re
from datetime import datetime


class Store:
    stores = []

    def __new__(cls, *args, **kwargs):
        assert isinstance(args[0], str) or isinstance(kwargs["name"], str), "Name of drugstore must be string"
        assert isinstance(args[1], str) or isinstance(kwargs["address"], str), "address of drugstore must be string"
        assert (isinstance(args[2], str) and args[2].isdigit() and args[2].startswith("0")) or isinstance(args[2], int)\
            or (isinstance(kwargs["call_number"], str) and kwargs["call_number"].isdigit() and
                kwargs["call_number"].startswith("0")) or isinstance(kwargs["call_number"], int), \
            "Call number must be a number"
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        assert isinstance(args[3], str) and re.match(regex, args[3])\
            or isinstance(kwargs["email"], str) and re.match(regex, kwargs["email"]), "Invalid Email address"
        assert (isinstance(args[4], (int, float)) and args[4] >= 0) or \
            isinstance(kwargs["balance"], (int, float)) and kwargs["balance"] >= 0, "Invalid Balance"
        instance = object.__new__(cls)
        return instance

    def __init__(self, name, address, call_number, email, balance=0):
        self.name = name
        self.address = address
        self.call_number = call_number
        self.email = email
        self.balance = balance
        self.shelves = {
            "health and medicine": [],
            "electricals": [],
            "vitamins": [],
            "toiletries": [],
            "baby and child": [],
            "men's": [],
            "skin-care": [],
            "stock up and save": []
        }
        self.__class__.stores.append(self)


class Drug:
    drugs = []

    def __new__(cls, *args, **kwargs):
        assert isinstance(args[0], str) or isinstance(kwargs["name"], str), "Name of drug must be string"
        assert isinstance(args[1], str) or isinstance(kwargs["company"], str), "company of drug must be string"
        for category in args[2]:
            assert isinstance(category, str), "category of drug must be string"
        for category in kwargs["categories"]:
            assert isinstance(category, str), "category of drug must be string"
        # assert isinstance(args[2], str) or isinstance(kwargs["category"], str), "category of drug must be string"
        assert isinstance(args[3], datetime) or isinstance(kwargs["exp_date"], datetime), \
            "exp date must be a date object"
        assert (isinstance(args[4], (int, float)) and args[4] > 0) or \
            (isinstance(kwargs["price"], (int, float)) and kwargs["price"] > 0), \
            "price must be a positive number"
        assert (isinstance(args[5], (int, float)) and args[5] > 0) or \
               (isinstance(kwargs["qty"], (int, float)) and kwargs["qty"] > 0), "quantity must be a positive number"
        instance = object.__new__(cls)
        return instance

    def __init__(self, name, company, categories, exp_date, price, qty):
        self.name = name
        self.company = company
        self.category = categories
        self.exp_date = exp_date
        self.price = price
        self.qty = qty
        self.is_expired = True if datetime.now() > self.exp_date else False

    def __str__(self):
        return f"Name: {self.name}, Company: {self.company}, category: {self.category}, price: {self.price}"

