from Monstr.Core import Runner
import mock 


def test_CMSJobStatus_withRunner():
    import datetime
    import Monstr.Modules.CMSJobStatus
    
    modules = Runner.get_modules()
    assert 'CMSJobStatus' in modules
    if 'CMSJobStatus' in modules:
        module = modules['CMSJobStatus']
        with mock.patch("module.Utils.get_UTC_now") as MockClass:
            MockClass.return_value = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(hours=1)
            modules['CMSJobStatus'].InsertToDB()

