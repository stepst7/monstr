from Monstr.Core import Runner

modules = Runner.get_modules()
assert 'PhedexQuality' in modules
if 'PhedexQuality' in modules:
     modules['PhedexQuality'].InsertToDB()