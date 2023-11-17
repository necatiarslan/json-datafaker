import yaml
from os import path
from . import util

class Config:
    _instance = None
    file_path:str

    def __new__(cls, file_path:str):
            if cls._instance is None:
                cls._instance = super(Config, cls).__new__(cls)
                if not path.isabs(file_path):
                    file_path = path.abspath(file_path)

                util.log(f"received config is {file_path}")
                cls._instance.file_path = file_path
                cls._instance.load_config_file()
                cls._instance.validate_config()

            return cls._instance
    
    @staticmethod
    def get_current():
        if Config._instance is None:
            raise Exception(f"Config is not initialized yet")
        
        return Config._instance

    def load_config_file(self):
        if path.isfile(self.file_path):
            with open(self.file_path, "r") as file:
                self.config = yaml.safe_load(file)
        else:
            raise Exception(f"{self.file_path} file not found")
    
    def validate_config(self):
        if "json" not in self.config:
            raise Exception(f"Config file should have json node")
        
        util.log(f"config file is validated")


    def get_locale(self):
        if "config" in self.config and "locale" in self.config["config"]:
            return self.config["config"]["locale"]
        else:
            return "en_US"

