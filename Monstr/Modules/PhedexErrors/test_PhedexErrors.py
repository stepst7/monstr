from Monstr.Core import Runner

modules = Runner.get_modules()
assert 'PhedexErrors' in modules
if 'PhedexErrors' in modules:
     modules['PhedexErrors'].insertToDB()
