from Montsr.Core import Runner

modules = Runner.get_modules(i)
assert 'PhedexErrors' in modules
if 'PhedexErrors' in modules:
     modules['PhedexErrors'].insertToDB()
