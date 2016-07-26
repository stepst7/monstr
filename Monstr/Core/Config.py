import ConfigParser
Config = ConfigParser.ConfigParser()

import os
print os.getcwd()
try:
    Config.read('/opt/monstr/current.cfg')
except Exception as e:
    print 'WARNING! Configuration is missing. Using test_conf.cfg'
    Config.read('test.cfg')    

def get_section(section):
    result = {}
    if section in Config.sections():
        options = Config.options(section)
        for option in options:
            result[option] = Config.get(section, option)
        return result
    else:
        raise 'Requested section is absent in configuration'
