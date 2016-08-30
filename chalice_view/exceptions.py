
from chalice.app import ChaliceError, ChaliceViewError

class InvalidChaliceSetting(ChaliceError):
    pass

class ApplicatonLoadingError(ChaliceError):
    pass

class BadResponseError(ChaliceViewError):
    STATUS_CODE = 500
