# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Participants(Model):
    """Details about the participant or signer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar status: The signing status
    :vartype status: str
    :ivar status_date: The date when status got changed.
    :vartype status_date: datetime
    :ivar email: The email address of the participant or signer.
    :vartype email: str
    """

    _validation = {
        'status': {'readonly': True},
        'status_date': {'readonly': True},
        'email': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'status_date': {'key': 'statusDate', 'type': 'iso-8601'},
        'email': {'key': 'email', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Participants, self).__init__(**kwargs)
        self.status = None
        self.status_date = None
        self.email = None