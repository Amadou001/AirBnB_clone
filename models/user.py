#!/usr/bin/python3
"""
user module
"""

from .base_model import BaseModel


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
