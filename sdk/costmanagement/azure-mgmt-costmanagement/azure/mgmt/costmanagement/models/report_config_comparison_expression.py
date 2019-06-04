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


class ReportConfigComparisonExpression(Model):
    """The comparison expression to be used in the report.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the column to use in comparison.
    :type name: str
    :param operator: Required. The operator to use for comparison. Possible
     values include: 'In', 'Contains'
    :type operator: str or ~azure.mgmt.costmanagement.models.OperatorType
    :param values: Required. Array of values to use for comparison
    :type values: list[str]
    """

    _validation = {
        'name': {'required': True},
        'operator': {'required': True},
        'values': {'required': True, 'min_items': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ReportConfigComparisonExpression, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.operator = kwargs.get('operator', None)
        self.values = kwargs.get('values', None)