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


class ModelsSummary(Model):
    """Result of query operation to fetch summery of models.

    :param count: Current count of trained models.
    :type count: str
    :param limit: Max number of models that can be trained for this
     subscription.
    :type limit: str
    :param last_updated_date_time: Get or set the summary last updated
     datetime.
    :type last_updated_date_time: datetime
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'str'},
        'limit': {'key': 'limit', 'type': 'str'},
        'last_updated_date_time': {'key': 'lastUpdatedDateTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(ModelsSummary, self).__init__(**kwargs)
        self.count = kwargs.get('count', None)
        self.limit = kwargs.get('limit', None)
        self.last_updated_date_time = kwargs.get('last_updated_date_time', None)