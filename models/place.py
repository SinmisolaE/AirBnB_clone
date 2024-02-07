#!/usr/bin/python3
""" Defines class Place """
from base_model import BaseModel


class Place(BaseModel):
    """ Inherits BaseModel
        unique attribute
    """
    city_id = 0
    user_id = 0
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    max_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
