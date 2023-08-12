#!/usr/bin/python3
"""Example of empty class.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    A base model with common attributes and methods.

    Public instance attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was last updated.

    Methods:
        save(): Updates the updated_at attribute with the current datetime.
        to_dict(): Returns a dictionary containing the instance attributes.

    Usage:
        base_model = BaseModel()
        base_model.save()
        data = base_model.to_dict()
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        This method assigns a unique ID, sets the created_at attribute to the current datetime,
        and initializes the updated_at attribute with the same value as created_at.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing the instance attributes.

        The dictionary includes all the keys and values from __dict__ of the instance.
        The created_at and updated_at attributes are converted to string objects
        in the ISO format (e.g., '2017-06-14T22:31:03.285259').
        The dictionary also includes a '__class__' key with the class name of the object.

        Returns:
            dict: A dictionary representation of the instance attributes.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
