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
  locale: en_US                       #OPTIONAL faker locale Default:en_US
json:
  item_count: 10000                    #OPTIONAL Default 10
  attributes:
    - name: id                        #MANDATORY
      data: row_id                    #OPTIONAL Default fake.word()
    - name: first_name
      data: fake.first_name()
    - name: last_name
      data: fake.last_name()
    - name: age
      data: fake.random_int(18, 90)
    - name: dob
      data: fake.date_of_birth()
    - name: street_address
      data: fake.street_address()
    - name: city
      data: fake.city()
    - name: state_abbr
      data: fake.state_abbr()
    - name: postcode
      data: fake.postcode()
    - name: gender
      data: random.choice(["male", "female"])
      null_percentage: 0.3
    - name: left_handed
      data: fake.pybool()
    - name: height
      data: None
```
[full yml example](tests/test_table.yaml)

### Sample Code
```python
import jsondatafaker

# export in json format
jsondatafaker.to_json("test_table.yaml", "./target_folder")

# you can use customer faker provider
from faker_education import SchoolProvider

jsondatafaker.to_json("test_table.yaml", "./target_folder", fake_provider=SchoolProvider)
# multiple custom provider in list also works
```

### Sample CLI Command
You can use jsondatafaker in your terminal for adhoc needs or shell script to automate fake data generation. \
Faker custom providers and custom functions are not supported in CLI.
```bash

# exports to current folder in json format
jsondatafaker --config test_table.yaml

# exports to target folder in json format
jsondatafaker --config test_table.yaml --target ./target_folder 

# exports to target file in json format 
jsondatafaker --config test_table.yaml --target ./target_folder/target_file.json
```

### Sample JSON Output
```json

```

### Custom Functions
With json Faker, you have the flexibility to provide your own custom functions to generate column data. This advanced feature empowers developers to create custom fake data generation logic that can pull data from a database, API, file, or any other source as needed. You can also supply multiple functions in a list, allowing for even more versatility. The custom function you provide should return a single value, giving you full control over your synthetic data generation.

```python
from jsondatafaker import jsondatafaker
from faker import Faker

fake = Faker()
def get_level():
    return f"level {fake.random_int(1, 5)}"

jsondatafaker.to_json("test_table.yaml", "./target_folder", custom_function=get_level)
```
Add get_level function to your yaml file
```
version: 1
config:
  locale: en_US #faker locale Default:en_US
json:
  item_count: 10000
  attributes:
    - name: id
      data: row_id
    - name: first_name
      data: fake.first_name()
    - name: last_name
      data: fake.last_name()
    - name: age
      data: fake.random_int(18, 90)
    - column_name: level
      data: get_level() # custom function
```


### Faker Functions List
https://faker.readthedocs.io/en/master/providers.html#

### Bug Report & New Feature Request
https://github.com/necatiarslan/json-faker/issues/new 


### Todo
- sub items

### Nice To Have
- 

Follow me on linkedin to get latest news \
https://www.linkedin.com/in/necati-arslan/

Thanks, \
Necati ARSLAN \
necatia@gmail.com