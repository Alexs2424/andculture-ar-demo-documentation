import logging
import urllib2, base64
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
from urlparse import urlparse
from hashlib import sha1, md5
from hmac import new as hmac
import json

#This is an all out built vuforia web services python api,
#but the only parts that are important are at the bottom
# SKIP to main()

#It's a nice resource to have in case you might wanna interact with
#Vuforia in these ways

class VuforiaBaseError(Exception):
    def __init__(self, exc, response):
        self.transaction_id = response['transaction_id']
        self.result_code = response['result_code']
        self.exc = exc


class VuforiaRequestQuotaReached(VuforiaBaseError):
    pass


class VuforiaAuthenticationFailure(VuforiaBaseError):
    pass


class VuforiaRequestTimeTooSkewed(VuforiaBaseError):
    pass


class VuforiaTargetNameExist(VuforiaBaseError):
    pass


class VuforiaUnknownTarget(VuforiaBaseError):
    pass


class VuforiaBadImage(VuforiaBaseError):
    pass


class VuforiaImageTooLarge(VuforiaBaseError):
    pass


class VuforiaMetadataTooLarge(VuforiaBaseError):
    pass


class VuforiaDateRangeError(VuforiaBaseError):
    pass


class VuforiaFail(VuforiaBaseError):
    pass


class Vuforia(object):
    def __init__(self, access_key, secret_key, host="https://vws.vuforia.com"):
        self.access_key = access_key
        self.secret_key = secret_key
        self.host = host

    def _get_rfc1123_date(self):
        now = datetime.now()
        stamp = mktime(now.timetuple())
        return format_date_time(stamp)

    def _get_request_path(self, req):
        o = urlparse(req.get_full_url())
        return o.path

    def _hmac_sha1_base64(self, key, message):
        return base64.b64encode(hmac(key, message, sha1).digest())

    def _get_content_md5(self, req):
        if req.get_data():
            return md5(str(req.get_data())).hexdigest()
        return "d41d8cd98f00b204e9800998ecf8427e"

    def _get_content_type(self, req):
        if req.get_method() in ["POST", "PUT"]:
            return "application/json"
        return ""

    def _get_authenticated_response(self, req):
        rfc1123_date = self._get_rfc1123_date()
        string_to_sign =\
            req.get_method() + "\n" +\
            self._get_content_md5(req) + "\n" +\
            self._get_content_type(req) + "\n" +\
            rfc1123_date + "\n" +\
            self._get_request_path(req)
        signature = self._hmac_sha1_base64(self.secret_key, string_to_sign)

        req.add_header('Date', rfc1123_date)
        auth_header = 'VWS %s:%s' % (self.access_key, signature)
        req.add_header('Authorization', auth_header)
        try:
            return urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            response = json.loads(e.read())
            result_code = response['result_code']
            if result_code == 'RequestTimeTooSkewed':
                raise VuforiaRequestTimeTooSkewed(e, response)
            elif result_code == 'TargetNameExist':
                raise VuforiaTargetNameExist(e, response)
            elif result_code == 'RequestQuotaReached':
                raise VuforiaRequestQuotaReached(e, response)
            elif result_code == 'UnknownTarget':
                raise VuforiaUnknownTarget(e, response)
            elif result_code == 'BadImage':
                raise VuforiaBadImage(e, response)
            elif result_code == 'ImageTooLarge':
                raise VuforiaImageTooLarge(e, response)
            elif result_code == 'MetadataTooLarge':
                raise VuforiaMetadataTooLarge(e, response)
            elif result_code == 'DateRangeError':
                raise VuforiaDateRangeError(e, response)
            elif result_code == 'Fail':
                raise VuforiaFail(e, response)
            else:
                logging.error("Couldn't process %s response from Vuforia" % response)

            raise e  # re-raise the initial exception if can't handle it

    def get_target_by_id(self, target_id):
        url = '%s/targets/%s' % (self.host, target_id)
        req = urllib2.Request(url)
        response = self._get_authenticated_response(req)
        return json.loads(response.read())['target_record']

    def get_target_ids(self):
        url = '%s/targets' % self.host
        req = urllib2.Request(url)
        response = self._get_authenticated_response(req)
        return json.loads(response.read())['results']

    def get_summary(self):
        url = '%s/summary' % self.host
        req = urllib2.Request(url)
        response = self._get_authenticated_response(req)
        return json.loads(response.read())

    def get_targets(self):
        targets = []
        for target_id in self.get_target_ids():
            targets.append(self.get_target_by_id(target_id))
        return targets

    def add_target(self, data):
        url = '%s/targets' % self.host
        data = json.dumps(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json; charset=utf-8'})
        response = self._get_authenticated_response(req)
        return json.loads(response.read())

    def update_target(self, target_id, data):
        # Takes time to process
        url = '%s/targets/%s' % (self.host, target_id)
        data = json.dumps(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json; charset=utf-8'})
        req.get_method = lambda: 'PUT'
        response = self._get_authenticated_response(req)
        return json.loads(response.read())

    def delete_target(self, target_id):
        # Takes time to process
        url = '%s/targets/%s' % (self.host, target_id)
        req = urllib2.Request(url)
        req.get_method = lambda: 'DELETE'
        response = self._get_authenticated_response(req)
        return json.loads(response.read())

def main():
    #REPLACE THE KEYS WITH YOURS!!!  THESE SHOULD BE THE SERVER KEYS NOT CLIENT
    v = Vuforia(access_key="ba4f9ae9e187e1354d03f1e4826beb10821533c2",
                secret_key="9d3cca8f383c282afcade9d6a117b8b4ad6c00d8")

    #implementation of adding multiple targets to the project
    train_path_str = '' # this is the path to the image target

    #Create this many image targets
    for train_num in range(0, 100):
        #all image targets have the same path and named sequentially on the system
        train_path_str = ("trainingdata_%i" %(train_num))
        print(train_path_str)
        #read the image data, so that we can add it onto the request
        image_file = open("trainingdata/%s.jpg" %(train_path_str))
        image = base64.b64encode(image_file.read())
        # If you are adding a metadata package from the code uncomment the lines below
        # metadata_file = open('PATH_TO_METADATAFILE')
        # metadata = base64.b64encode(metadata_file.read())

        #Calls the add_target function and prints out the result once finished.
        print v.add_target({"name": train_path_str, "width": 0.127,"image": image, "active_flag": 1}) # include this if you are using metadata: "application_metadata": metadata,

if __name__ == "__main__":
    main()
