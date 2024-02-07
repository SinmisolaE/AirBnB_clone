#!/usr/bin/python3
""" Deines class Review """
from base_model import BaseModel


class Review(BaseModel):
    """ Class attributes, inherrits basemodel"""

    place_id = ""
    user_id = ""
    text = ""
