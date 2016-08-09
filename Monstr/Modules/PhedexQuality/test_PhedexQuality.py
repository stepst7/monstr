from Monstr.Core import Runner

def test_PhedexErrors_initial():
    modules = Runner.get_modules()
    assert 'PhedexQuality' in modules
    if 'PhedexQuality' in modules:
        modules['PhedexQuality'].main()
