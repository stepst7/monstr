from Monstr.Core import Runner

modules = Runner.get_modules()
assert 'CMSJobStatus' in modules
if 'CMSJobStatus' in modules:
     modules['CMSJobStatus'].InsertToDB()