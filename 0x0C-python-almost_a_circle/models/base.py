#!/usr/bin/python3
""" This module contain the base model of classes
"""
import json
import csv
import turtle


class Base:
    """ a base class module

    Attributes:
        __nb_objects (int): class attr. number of objects.
        id (int): instance attr. object id.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ method to initialize the class with an ID

        Args:
            id (int, optional): id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list[dict]): list of dictionaries
        Returns:
            string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """  The list of the JSON string representation json_string
        Args:
            json_string (str): string representation
        Returns:
            list: The list of the JSON string representation
        """
        if json_string is not None and json_string != '':
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs
        to a file
        Args:
            list_objs (list[obj]): list of objects
        """
        if list_objs is None or list_objs == []:
            json_str = "[]"
        else:
            json_str = cls.to_json_string([r.to_dictionary()
                                          for r in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(json.loads(json_str), f)

    @classmethod
    def create(cls, **dictionary):
        """ create an instance with all attributes
        Args:
            dictionary (
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances:
        Returns:
            list: list of instances:
        """
        filename = cls.__name__ + ".json"
        ins_list = []
        try:
            with open(filename) as f:
                ins_list = cls.from_json_string(f.read())
            for key, value in enumerate(ins_list):
                ins_list[key] = cls.create(**ins_list[key])
        except Exception:
            pass
        return ins_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the CSV string representation of list_objs
        to a file
        Args:
            list_objs (list[obj]): list of objects
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w') as csv_file:
            if len(list_objs) == 0:
                return
            fieldnames = list_objs[0].to_dictionary().keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for obj in list_objs:
                csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        loads the CSV string representation of list_objs from a file
        """
        filename = cls.__name__ + ".csv"
        ins_list = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.DictReader(f)
                for line in csv_reader:
                    for key in line:
                        line[key] = int(line[key])
                    new = cls.create(**line)
                    ins_list.append(new)
        except Exception:
            pass
        return ins_list
