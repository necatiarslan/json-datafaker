import sys, os
sys.path.append(os.path.abspath("."))

from jsondatafaker import jsondatafaker
from faker_education import SchoolProvider
from faker import Faker

fake = Faker()
def get_level():
    return f"level {fake.random_int(1, 5)}"



directory_path = 'tests/exports'
[os.remove(os.path.join(directory_path, file)) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

#print(fake.school_name())

#jsondatafaker.to_json("tests/test_json.yaml", "./tests/exports", fake_provider=SchoolProvider, custom_function=get_level)

json_data = jsondatafaker.generate_json("tests/test_json.yaml", fake_provider=SchoolProvider, custom_function=get_level)
print(json_data["first_name"])