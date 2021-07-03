from lps36.header.command import Command
from lps36.header.transaction import Transaction
from lps36.header.status import Status
from lps36.header.encoder import Encoder
from lps36.header.scan import Scan
from lps36.header.type import Type
from lps36.header.data import Data


class Header():

    command: Command
    transaction: Transaction
    status: Status
    encoder: Encoder
    scan: Scan
    _type: Type
    dataSize: Data
