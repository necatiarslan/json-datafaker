# json Faker
jsondatafaker is a versatile Python package that empowers you to effortlessly create realistic but synthetic json data for a wide range of applications. If you need to generate test data for software development, this tool simplifies the process with an intuitive schema definition in YAML format.

### Key Features
**Schema Definition:** Define your target schema using a simple YAML file. Specify the structure of your JSON, attribute names and fake data generation code.

**Faker and Randomization:** Leverage the power of the Faker library and random data generation to create authentic-looking fake data that mimics real-world scenarios.

### Installation
```bash 
pip install jsondatafaker
```

### Sample Yaml File
```
version: 1
config:
  locale: en_US #faker locale Default:en_US
json:
  first_name: fake.first_name()
  last_name: fake.last_name()
  is_alive: fake.pybool()
  age: fake.random_int(18, 90)
  dob: fake.date_of_birth()
  address:
    street_address: fake.street_address()
    city: fake.city()
    state: fake.state_abbr()
    postal_code: fake.postcode()
  phone_numbers:
    - type: "\"home\""
      number: fake.phone_number()
    - type: "\"office\""
      number: fake.phone_number()
  children:
    - fake.first_name()
    - fake.first_name()
    - fake.first_name()
  spouse: null
```
[full yml example](tests/test_json.yaml)

### Sample Code
```python
import jsondatafaker

#generate json only to work with
json_data = jsondatafaker.generate_json("tests/test_json.yaml")
print(json_data["first_name"])

# export in json format
jsondatafaker.to_json("test_json.yaml", "./target_folder")
```

### Sample CLI Command
You can use jsondatafaker in your terminal for adhoc needs or shell script to automate fake data generation. \
Faker custom providers and custom functions are not supported in CLI.
```bash

# exports to current folder in json format
jsondatafaker --config test_json.yaml

# exports to target folder in json format
jsondatafaker --config test_json.yaml --target ./target_folder 

# exports to target file in json format 
jsondatafaker --config test_json.yaml --target ./target_folder/target_file.json
```

### Sample JSON Output
```json
{
    "first_name": "Michael",
    "last_name": "Cunningham",
    "is_alive": false,
    "age": 55,
    "dob": "1954-01-04",
    "address": {
        "street_address": "68878 Stephanie Walk",
        "city": "Port Jeremy",
        "state": "MT",
        "postal_code": "47702"
    },
    "phone_numbers": [
        {
            "type": "home",
            "number": "(792)887-9048"
        },
        {
            "type": "office",
            "number": "+1-901-428-8816x568"
        }
    ],
    "children": [
        "Katelyn",
        "Jenna",
        "Barbara"
    ],
    "spouse": null
}
```

### Custom Functions and Faker Providers
With json Faker, you have the flexibility to provide your own custom functions to generate column data. This advanced feature empowers developers to create custom fake data generation logic that can pull data from a database, API, file, or any other source as needed. You can also supply multiple functions in a list, allowing for even more versatility. The custom function you provide should return a single value, giving you full control over your synthetic data generation.

```python
from jsondatafaker import jsondatafaker
from faker import Faker
from faker_education import SchoolProvider #import custom faker provider

fake = Faker()
def get_level():
    return f"level {fake.random_int(1, 5)}"


jsondatafaker.to_json("test_json.yaml", "./target_folder", fake_provider=SchoolProvider, custom_function=get_level)
#multiple fake provider or custom function in a list is also works
```
Add get_level() function and custom faker provider to your yaml file
```
version: 1
config:
  locale: en_US #faker locale Default:en_US
json:
  first_name: fake.first_name()
  last_name: fake.last_name()
  is_alive: fake.pybool()
  age: fake.random_int(18, 90)
  dob: fake.date_of_birth()
  level: get_level()            # custom function
  school: fake.school_name()    # customer faker provider
```


### Faker Functions List
https://faker.readthedocs.io/en/master/providers.html#

### Bug Report & New Feature Request
https://github.com/necatiarslan/json-datafaker/issues/new 


### Todo
- 

### Nice To Have
- 

Follow me on linkedin to get latest news \
https://www.linkedin.com/in/necati-arslan/

Thanks, \
Necati ARSLAN \
necatia@gmail.com