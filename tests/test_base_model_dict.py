#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print("ID:", my_model.id)
print("Instance:", my_model)
print("Type of 'created_at':", type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print("Dictionary representation:", my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")

my_new_model = BaseModel(**my_model_json)
print("ID of the new instance:", my_new_model.id)
print("New instance:", my_new_model)
print("Type of 'created_at' in the new instance:", type(my_new_model.created_at))

print("--")

print("Are they the same instance?", my_model is my_new_model)
