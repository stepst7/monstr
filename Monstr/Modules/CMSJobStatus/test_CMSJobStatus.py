from Monstr.Core import Runner
import mock 


def test_CMSJobStats_withRunner():
    import datetime
    modules = Runner.get_modules()
    assert 'CMSJobStatus' in modules
    if 'CMSJobStatus' in modules:
        with mock.patch("modules['CMSJobStatus'].Utils.get_UTC_now") as MockClass:
	    MockClass.return_value = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(hours=1)
            modules['CMSJobStatus'].InsertToDB()

