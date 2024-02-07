#!/usr/bin/python3
""" Defines class User """


class User(BaseModel):
    """ Inherits from BaseModel and has unique attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
