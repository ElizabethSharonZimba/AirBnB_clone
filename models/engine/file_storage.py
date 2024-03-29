<<<<<<< HEAD
=======
#!/usr/bin/python3
"""Defines the FileStorage class."""
>>>>>>> c10fc33cbdb9f130fd31f3abf6864652d4bbe2ee
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
<<<<<<< HEAD
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)
=======
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
>>>>>>> c10fc33cbdb9f130fd31f3abf6864652d4bbe2ee

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
<<<<<<< HEAD
            with open(self.__file_path) as f:
                obj_dict = json.load(f)
                for key, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**obj_data)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error while reloading:", e)
            self.__objects = {}

=======
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
>>>>>>> c10fc33cbdb9f130fd31f3abf6864652d4bbe2ee
