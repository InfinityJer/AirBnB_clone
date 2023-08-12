#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Args:
        place_id (str): Place id
        user_id (str): User id
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
