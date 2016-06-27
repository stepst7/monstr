from Monstr.Core import Runner

def test_PhedexErrors_initial():
    modules = Runner.get_modules()
    assert 'PhedexErrors' in modules
    if 'PhedexErrors' in modules:
         modules['PhedexErrors'].InsertToDB()
