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


class LuisApp(Model):
    """Exported Model - An exported LUIS Application.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: The name of the application.
    :type name: str
    :param version_id: The version ID of the application that was exported.
    :type version_id: str
    :param desc: The description of the application.
    :type desc: str
    :param culture: The culture of the application. E.g.: en-us.
    :type culture: str
    :param intents: List of intents.
    :type intents:
     list[~azure.cognitiveservices.language.luis.authoring.models.HierarchicalModel]
    :param entities: List of entities.
    :type entities:
     list[~azure.cognitiveservices.language.luis.authoring.models.HierarchicalModel]
    :param closed_lists: List of list entities.
    :type closed_lists:
     list[~azure.cognitiveservices.language.luis.authoring.models.ClosedList]
    :param composites: List of composite entities.
    :type composites:
     list[~azure.cognitiveservices.language.luis.authoring.models.HierarchicalModel]
    :param pattern_any_entities: List of Pattern.Any entities.
    :type pattern_any_entities:
     list[~azure.cognitiveservices.language.luis.authoring.models.PatternAny]
    :param regex_entities: List of regular expression entities.
    :type regex_entities:
     list[~azure.cognitiveservices.language.luis.authoring.models.RegexEntity]
    :param prebuilt_entities: List of prebuilt entities.
    :type prebuilt_entities:
     list[~azure.cognitiveservices.language.luis.authoring.models.PrebuiltEntity]
    :param regex_features: List of pattern features.
    :type regex_features:
     list[~azure.cognitiveservices.language.luis.authoring.models.JSONRegexFeature]
    :param model_features: List of model features.
    :type model_features:
     list[~azure.cognitiveservices.language.luis.authoring.models.JSONModelFeature]
    :param patterns: List of patterns.
    :type patterns:
     list[~azure.cognitiveservices.language.luis.authoring.models.PatternRule]
    :param utterances: List of example utterances.
    :type utterances:
     list[~azure.cognitiveservices.language.luis.authoring.models.JSONUtterance]
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'version_id': {'key': 'versionId', 'type': 'str'},
        'desc': {'key': 'desc', 'type': 'str'},
        'culture': {'key': 'culture', 'type': 'str'},
        'intents': {'key': 'intents', 'type': '[HierarchicalModel]'},
        'entities': {'key': 'entities', 'type': '[HierarchicalModel]'},
        'closed_lists': {'key': 'closedLists', 'type': '[ClosedList]'},
        'composites': {'key': 'composites', 'type': '[HierarchicalModel]'},
        'pattern_any_entities': {'key': 'patternAnyEntities', 'type': '[PatternAny]'},
        'regex_entities': {'key': 'regex_entities', 'type': '[RegexEntity]'},
        'prebuilt_entities': {'key': 'prebuiltEntities', 'type': '[PrebuiltEntity]'},
        'regex_features': {'key': 'regex_features', 'type': '[JSONRegexFeature]'},
        'model_features': {'key': 'model_features', 'type': '[JSONModelFeature]'},
        'patterns': {'key': 'patterns', 'type': '[PatternRule]'},
        'utterances': {'key': 'utterances', 'type': '[JSONUtterance]'},
    }

    def __init__(self, **kwargs):
        super(LuisApp, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.name = kwargs.get('name', None)
        self.version_id = kwargs.get('version_id', None)
        self.desc = kwargs.get('desc', None)
        self.culture = kwargs.get('culture', None)
        self.intents = kwargs.get('intents', None)
        self.entities = kwargs.get('entities', None)
        self.closed_lists = kwargs.get('closed_lists', None)
        self.composites = kwargs.get('composites', None)
        self.pattern_any_entities = kwargs.get('pattern_any_entities', None)
        self.regex_entities = kwargs.get('regex_entities', None)
        self.prebuilt_entities = kwargs.get('prebuilt_entities', None)
        self.regex_features = kwargs.get('regex_features', None)
        self.model_features = kwargs.get('model_features', None)
        self.patterns = kwargs.get('patterns', None)
        self.utterances = kwargs.get('utterances', None)