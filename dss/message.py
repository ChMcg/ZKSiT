
from email import message
from dss.identifier import Identifier, IdentifierFactory


class Message():
    sender_identifier: Identifier
    receiver_identifier: Identifier
    message: str

