import ConfigParser
import os

CONFIG_PATH = '/opt/monstr/current.cfg'


Config = ConfigParser.ConfigParser()
print os.getcwd()
if os.path.isfile(CONFIG_PATH):
    Config.read(CONFIG_PATH)
else:
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
        raise Exception('Requested section is absent in configuration')
