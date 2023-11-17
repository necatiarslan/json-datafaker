from faker import Faker
import random
import json
from os import path
import datetime
from . import config, util

def to_json(config_file_path, target_file_path=None, **kwargs) -> str :
    json_data = generate_json(config_file_path, **kwargs)

    file_type = "json"
    if path.isdir(target_file_path):
            temp_file_path = path.join(target_file_path, util.get_temp_filename() + util.get_file_extension(file_type))
            write_to_file(json_data, temp_file_path)
            util.log(f"data is exported to {temp_file_path} as {file_type}")
            result = temp_file_path 
    else:
        write_to_file(json_data, target_file_path)
        util.log(f"data is exported to {target_file_path} as {file_type}")
        result = target_file_path
    
    return result

def write_to_file(json_data, target_file_path):
    with open(target_file_path, mode="w") as file:
        json.dump(json_data, file, indent=4)

def generate_json(config_file_path, **kwargs):
    configurator = config.Config(config_file_path)
    json_config = configurator.config["json"]

    locale = configurator.get_locale()
    fake = Faker(locale)

    if "fake_provider" in kwargs:
        if not isinstance(kwargs["fake_provider"], list):
            fake.add_provider(kwargs["fake_provider"])
        else:
            for provider in kwargs["fake_provider"]:
                fake.add_provider(provider)

    def generate_data(node):
        if isinstance(node, dict):
            return {key: generate_data(value) for key, value in node.items()}
        elif isinstance(node, list):
            return [generate_data(item) for item in node]
        elif isinstance(node, str) and node == 'None':
            return None
        elif isinstance(node, str):
            return generate_fake_value(fake, node, **kwargs)
        else:
            return node

    fake_data = generate_data(json_config)
    util.log(f"json data is generated")
    
    return fake_data

def generate_fake_value(fake: Faker, command, **kwargs):
    result = None

    variables = {
        "random": random,
        "fake": fake,
        "result": result,
        "command": command
        }
    
    if "custom_function" in kwargs:
        if isinstance(kwargs["custom_function"], list):
            for func in kwargs["custom_function"]:
                variables[func.__name__] = func
        else:
            func = kwargs["custom_function"]
            variables[func.__name__] = func
    
    exec(f"result = {command}", variables)
    result = variables["result"]

    if isinstance(result, (datetime.date, datetime.datetime)):
        result = result.isoformat()

    return result
