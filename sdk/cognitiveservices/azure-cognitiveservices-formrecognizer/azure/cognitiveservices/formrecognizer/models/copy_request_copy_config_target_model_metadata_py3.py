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


class CopyRequestCopyConfigTargetModelMetadata(Model):
    """Metadata for copied model to Target.

    :param name: Name of copied model at Target.
    :type name: str
    :param description: Description of copied model.
    :type description: str
    :param tags: Tags for copied model
    :type tags: list[str]
    """

    _validation = {
        'name': {'max_length': 128, 'min_length': 0},
        'description': {'max_length': 1024, 'min_length': 0},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
    }

    def __init__(self, *, name: str=None, description: str=None, tags=None, **kwargs) -> None:
        super(CopyRequestCopyConfigTargetModelMetadata, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.tags = tags