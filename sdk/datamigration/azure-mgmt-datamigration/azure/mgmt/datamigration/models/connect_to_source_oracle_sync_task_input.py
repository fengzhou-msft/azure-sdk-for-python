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


class ConnectToSourceOracleSyncTaskInput(Model):
    """Input for the task that validates Oracle database connection.

    All required parameters must be populated in order to send to Azure.

    :param source_connection_info: Required. Information for connecting to
     Oracle source
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.OracleConnectionInfo
    """

    _validation = {
        'source_connection_info': {'required': True},
    }

    _attribute_map = {
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'OracleConnectionInfo'},
    }

    def __init__(self, **kwargs):
        super(ConnectToSourceOracleSyncTaskInput, self).__init__(**kwargs)
        self.source_connection_info = kwargs.get('source_connection_info', None)