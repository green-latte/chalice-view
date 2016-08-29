
from chalice.app import ChaliceViewError

class BadResponseError(ChaliceViewError):
    STATUS_CODE = 500
