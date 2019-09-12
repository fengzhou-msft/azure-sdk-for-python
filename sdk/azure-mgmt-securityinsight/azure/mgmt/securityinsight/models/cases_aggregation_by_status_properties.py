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


class CasesAggregationByStatusProperties(Model):
    """Aggregative results of cases by status property bag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar total_dismissed_status: Total amount of open cases with status
     Dismissed
    :vartype total_dismissed_status: int
    :ivar total_in_progress_status: Total amount of open cases with status
     InProgress
    :vartype total_in_progress_status: int
    :ivar total_new_status: Total amount of open cases with status New
    :vartype total_new_status: int
    :ivar total_resolved_status: Total amount of open cases with status
     Resolved
    :vartype total_resolved_status: int
    """

    _validation = {
        'total_dismissed_status': {'readonly': True},
        'total_in_progress_status': {'readonly': True},
        'total_new_status': {'readonly': True},
        'total_resolved_status': {'readonly': True},
    }

    _attribute_map = {
        'total_dismissed_status': {'key': 'totalDismissedStatus', 'type': 'int'},
        'total_in_progress_status': {'key': 'totalInProgressStatus', 'type': 'int'},
        'total_new_status': {'key': 'totalNewStatus', 'type': 'int'},
        'total_resolved_status': {'key': 'totalResolvedStatus', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(CasesAggregationByStatusProperties, self).__init__(**kwargs)
        self.total_dismissed_status = None
        self.total_in_progress_status = None
        self.total_new_status = None
        self.total_resolved_status = None
