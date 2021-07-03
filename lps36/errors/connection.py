from lps36.errors.error import LPS36Error


class ConnectionError(LPS36Error):

    retriable = True
