import ConfigParser
Config = ConfigParser.ConfigParser()

import os
print os.getcwd()
Config.read('default.cfg')

def get_section(section):
    result = {}
    if section in Config.sections():
        options = Config.options(section)
        for option in options:
            result[option] = Config.get(section, option)
        return result
    else:
        raise 'Requested section is absent in configuration'