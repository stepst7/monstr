from Monstr.Core import Runner
import mock 



def test_CMSJobStatus_withRunner():
    import datetime
    import pytz
    import Monstr.Modules.CMSJobStatus.CMSJobStatus as testedModule
    

    with mock.patch("Monstr.Modules.CMSJobStatus.CMSJobStatus.Utils.get_UTC_now") as MockClass:
        MockClass.return_value = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(hours=1)
        testedModule.InsertToDB()

