from configparser import ConfigParser


class Config:

    def __init__(self, env):
        self.env = env
        self.config = ConfigParser()
        property_path = f"./resource/config/application-{self.env}.ini"
        self.config.read(property_path)

    def get_config(self, section, key):
        return self.config.get(section, key)
