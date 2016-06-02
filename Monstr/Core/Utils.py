import datetime
import pytz
import urllib

def get_page(request):
    """Return html code from cmsweb.cern.ch of the page with the given request"""
    print "HTTP access: ", request
    socket_obj = urllib.urlopen(request)
    page = socket_obj.read()
    socket_obj.close()
    return page

def epoch_to_datetime(seconds):
    new_time = datetime.datetime.utcfromtimestamp(float(seconds)).replace(tzinfo=pytz.utc)
    return new_time

def get_UTC_now():
	return datetime.datetime.utcnow().replace(tzinfo=pytz.utc)