#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):

    name = ""

    def __init__(se4lf, *args, **kwargs):

        super().__init__(*args, **kwargs)
