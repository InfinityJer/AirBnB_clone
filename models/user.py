#!/usr/bin/python3
"""contains class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class

    Args:
        email (str): user's email
        password (str): user's password
        first_name (str): user's 1st name
        last_name (str): user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
