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
from msrest.exceptions import HttpOperationError


class ActionGroupsInformation(Model):
    """The Action Groups information, used by the alert rule.

    All required parameters must be populated in order to send to Azure.

    :param custom_email_subject: An optional custom email subject to use in
     email notifications.
    :type custom_email_subject: str
    :param custom_webhook_payload: An optional custom web-hook payload to use
     in web-hook notifications.
    :type custom_webhook_payload: str
    :param group_ids: Required. The Action Group resource IDs.
    :type group_ids: list[str]
    """

    _validation = {
        'group_ids': {'required': True},
    }

    _attribute_map = {
        'custom_email_subject': {'key': 'customEmailSubject', 'type': 'str'},
        'custom_webhook_payload': {'key': 'customWebhookPayload', 'type': 'str'},
        'group_ids': {'key': 'groupIds', 'type': '[str]'},
    }

    def __init__(self, *, group_ids, custom_email_subject: str=None, custom_webhook_payload: str=None, **kwargs) -> None:
        super(ActionGroupsInformation, self).__init__(**kwargs)
        self.custom_email_subject = custom_email_subject
        self.custom_webhook_payload = custom_webhook_payload
        self.group_ids = group_ids


class ProxyResource(Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None


class Alert(ProxyResource):
    """An alert created in alert management service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param properties:
    :type properties: ~azure.mgmt.alertsmanagement.models.AlertProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'AlertProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(Alert, self).__init__(**kwargs)
        self.properties = properties


class AlertModification(ProxyResource):
    """Alert Modification details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param properties:
    :type properties:
     ~azure.mgmt.alertsmanagement.models.AlertModificationProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'AlertModificationProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(AlertModification, self).__init__(**kwargs)
        self.properties = properties


class AlertModificationItem(Model):
    """Alert modification item.

    :param modification_event: Reason for the modification. Possible values
     include: 'AlertCreated', 'StateChange', 'MonitorConditionChange'
    :type modification_event: str or
     ~azure.mgmt.alertsmanagement.models.AlertModificationEvent
    :param old_value: Old value
    :type old_value: str
    :param new_value: New value
    :type new_value: str
    :param modified_at: Modified date and time
    :type modified_at: str
    :param modified_by: Modified user details (Principal client name)
    :type modified_by: str
    :param comments: Modification comments
    :type comments: str
    :param description: Description of the modification
    :type description: str
    """

    _attribute_map = {
        'modification_event': {'key': 'modificationEvent', 'type': 'AlertModificationEvent'},
        'old_value': {'key': 'oldValue', 'type': 'str'},
        'new_value': {'key': 'newValue', 'type': 'str'},
        'modified_at': {'key': 'modifiedAt', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'str'},
        'comments': {'key': 'comments', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, modification_event=None, old_value: str=None, new_value: str=None, modified_at: str=None, modified_by: str=None, comments: str=None, description: str=None, **kwargs) -> None:
        super(AlertModificationItem, self).__init__(**kwargs)
        self.modification_event = modification_event
        self.old_value = old_value
        self.new_value = new_value
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.comments = comments
        self.description = description


class AlertModificationProperties(Model):
    """Properties of the alert modification item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar alert_id: Unique Id of the alert for which the history is being
     retrieved
    :vartype alert_id: str
    :param modifications: Modification details
    :type modifications:
     list[~azure.mgmt.alertsmanagement.models.AlertModificationItem]
    """

    _validation = {
        'alert_id': {'readonly': True},
    }

    _attribute_map = {
        'alert_id': {'key': 'alertId', 'type': 'str'},
        'modifications': {'key': 'modifications', 'type': '[AlertModificationItem]'},
    }

    def __init__(self, *, modifications=None, **kwargs) -> None:
        super(AlertModificationProperties, self).__init__(**kwargs)
        self.alert_id = None
        self.modifications = modifications


class AlertProperties(Model):
    """Alert property bag.

    :param essentials:
    :type essentials: ~azure.mgmt.alertsmanagement.models.Essentials
    :param context:
    :type context: object
    :param egress_config:
    :type egress_config: object
    """

    _attribute_map = {
        'essentials': {'key': 'essentials', 'type': 'Essentials'},
        'context': {'key': 'context', 'type': 'object'},
        'egress_config': {'key': 'egressConfig', 'type': 'object'},
    }

    def __init__(self, *, essentials=None, context=None, egress_config=None, **kwargs) -> None:
        super(AlertProperties, self).__init__(**kwargs)
        self.essentials = essentials
        self.context = context
        self.egress_config = egress_config


class AzureResource(Model):
    """An Azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar name: The resource name.
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureResource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None


class AlertRule(AzureResource):
    """The alert rule information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar name: The resource name.
    :vartype name: str
    :param description: The alert rule description.
    :type description: str
    :param state: Required. The alert rule state. Possible values include:
     'Enabled', 'Disabled'
    :type state: str or ~azure.mgmt.alertsmanagement.models.AlertRuleState
    :param severity: Required. The alert rule severity. Possible values
     include: 'Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4'
    :type severity: str or ~azure.mgmt.alertsmanagement.models.Severity
    :param frequency: Required. The alert rule frequency in ISO8601 format.
     The time granularity must be in minutes and minimum value is 5 minutes.
    :type frequency: timedelta
    :param detector: Required. The alert rule's detector.
    :type detector: ~azure.mgmt.alertsmanagement.models.Detector
    :param scope: Required. The alert rule resources scope.
    :type scope: list[str]
    :param action_groups: Required. The alert rule actions.
    :type action_groups:
     ~azure.mgmt.alertsmanagement.models.ActionGroupsInformation
    :param throttling: The alert rule throttling information.
    :type throttling:
     ~azure.mgmt.alertsmanagement.models.ThrottlingInformation
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'state': {'required': True},
        'severity': {'required': True},
        'frequency': {'required': True},
        'detector': {'required': True},
        'scope': {'required': True},
        'action_groups': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'frequency': {'key': 'properties.frequency', 'type': 'duration'},
        'detector': {'key': 'properties.detector', 'type': 'Detector'},
        'scope': {'key': 'properties.scope', 'type': '[str]'},
        'action_groups': {'key': 'properties.actionGroups', 'type': 'ActionGroupsInformation'},
        'throttling': {'key': 'properties.throttling', 'type': 'ThrottlingInformation'},
    }

    def __init__(self, *, state, severity, frequency, detector, scope, action_groups, description: str=None, throttling=None, **kwargs) -> None:
        super(AlertRule, self).__init__(**kwargs)
        self.description = description
        self.state = state
        self.severity = severity
        self.frequency = frequency
        self.detector = detector
        self.scope = scope
        self.action_groups = action_groups
        self.throttling = throttling


class AlertsSummary(ProxyResource):
    """Summary of alerts based on the input filters and 'groupby' parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param properties:
    :type properties: ~azure.mgmt.alertsmanagement.models.AlertsSummaryGroup
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'AlertsSummaryGroup'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(AlertsSummary, self).__init__(**kwargs)
        self.properties = properties


class AlertsSummaryGroup(Model):
    """Group the result set.

    :param total: Total count of the result set.
    :type total: int
    :param smart_groups_count: Total count of the smart groups.
    :type smart_groups_count: int
    :param groupedby: Name of the field aggregated
    :type groupedby: str
    :param values: List of the items
    :type values:
     list[~azure.mgmt.alertsmanagement.models.AlertsSummaryGroupItem]
    """

    _attribute_map = {
        'total': {'key': 'total', 'type': 'int'},
        'smart_groups_count': {'key': 'smartGroupsCount', 'type': 'int'},
        'groupedby': {'key': 'groupedby', 'type': 'str'},
        'values': {'key': 'values', 'type': '[AlertsSummaryGroupItem]'},
    }

    def __init__(self, *, total: int=None, smart_groups_count: int=None, groupedby: str=None, values=None, **kwargs) -> None:
        super(AlertsSummaryGroup, self).__init__(**kwargs)
        self.total = total
        self.smart_groups_count = smart_groups_count
        self.groupedby = groupedby
        self.values = values


class AlertsSummaryGroupItem(Model):
    """Alerts summary group item.

    :param name: Value of the aggregated field
    :type name: str
    :param count: Count of the aggregated field
    :type count: int
    :param groupedby: Name of the field aggregated
    :type groupedby: str
    :param values: List of the items
    :type values:
     list[~azure.mgmt.alertsmanagement.models.AlertsSummaryGroupItem]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'groupedby': {'key': 'groupedby', 'type': 'str'},
        'values': {'key': 'values', 'type': '[AlertsSummaryGroupItem]'},
    }

    def __init__(self, *, name: str=None, count: int=None, groupedby: str=None, values=None, **kwargs) -> None:
        super(AlertsSummaryGroupItem, self).__init__(**kwargs)
        self.name = name
        self.count = count
        self.groupedby = groupedby
        self.values = values


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Detector(Model):
    """The detector information. By default this is not populated, unless it's
    specified in expandDetector.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The detector id.
    :type id: str
    :param parameters: The detector's parameters.'
    :type parameters: dict[str, object]
    :param name: The Smart Detector name. By default this is not populated,
     unless it's specified in expandDetector
    :type name: str
    :param description: The Smart Detector description. By default this is not
     populated, unless it's specified in expandDetector
    :type description: str
    :param supported_resource_types: The Smart Detector supported resource
     types. By default this is not populated, unless it's specified in
     expandDetector
    :type supported_resource_types: list[str]
    :param image_paths: The Smart Detector image path. By default this is not
     populated, unless it's specified in expandDetector
    :type image_paths: list[str]
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'supported_resource_types': {'key': 'supportedResourceTypes', 'type': '[str]'},
        'image_paths': {'key': 'imagePaths', 'type': '[str]'},
    }

    def __init__(self, *, id: str, parameters=None, name: str=None, description: str=None, supported_resource_types=None, image_paths=None, **kwargs) -> None:
        super(Detector, self).__init__(**kwargs)
        self.id = id
        self.parameters = parameters
        self.name = name
        self.description = description
        self.supported_resource_types = supported_resource_types
        self.image_paths = image_paths


class ErrorResponse(Model):
    """An error response from the service.

    :param error:
    :type error: ~azure.mgmt.alertsmanagement.models.ErrorResponseBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ErrorResponse1(Model):
    """Describe the format of an Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse1, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponse1Exception(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse1'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponse1Exception, self).__init__(deserialize, response, 'ErrorResponse1', *args)


class ErrorResponseBody(Model):
    """Details of error response.

    :param code: Error code, intended to be consumed programmatically.
    :type code: str
    :param message: Description of the error, intended for display in user
     interface.
    :type message: str
    :param target: Target of the particular error, for example name of the
     property.
    :type target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.alertsmanagement.models.ErrorResponseBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponseBody]'},
    }

    def __init__(self, *, code: str=None, message: str=None, target: str=None, details=None, **kwargs) -> None:
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class Essentials(Model):
    """This object contains consistent fields across different monitor services.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar severity: Severity of alert Sev0 being highest and Sev4 being
     lowest. Possible values include: 'Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4'
    :vartype severity: str or ~azure.mgmt.alertsmanagement.models.Severity
    :ivar signal_type: The type of signal the alert is based on, which could
     be metrics, logs or activity logs. Possible values include: 'Metric',
     'Log', 'Unknown'
    :vartype signal_type: str or
     ~azure.mgmt.alertsmanagement.models.SignalType
    :ivar alert_state: Alert object state, which can be modified by the user.
     Possible values include: 'New', 'Acknowledged', 'Closed'
    :vartype alert_state: str or
     ~azure.mgmt.alertsmanagement.models.AlertState
    :ivar monitor_condition: Can be 'Fired' or 'Resolved', which represents
     whether the underlying conditions have crossed the defined alert rule
     thresholds. Possible values include: 'Fired', 'Resolved'
    :vartype monitor_condition: str or
     ~azure.mgmt.alertsmanagement.models.MonitorCondition
    :param target_resource: Target ARM resource, on which alert got created.
    :type target_resource: str
    :param target_resource_name: Name of the target ARM resource name, on
     which alert got created.
    :type target_resource_name: str
    :param target_resource_group: Resource group of target ARM resource, on
     which alert got created.
    :type target_resource_group: str
    :param target_resource_type: Resource type of target ARM resource, on
     which alert got created.
    :type target_resource_type: str
    :ivar monitor_service: Monitor service on which the rule(monitor) is set.
     Possible values include: 'Application Insights', 'ActivityLog
     Administrative', 'ActivityLog Security', 'ActivityLog Recommendation',
     'ActivityLog Policy', 'ActivityLog Autoscale', 'Log Analytics', 'Nagios',
     'Platform', 'SCOM', 'ServiceHealth', 'SmartDetector', 'VM Insights',
     'Zabbix', 'Resource Health'
    :vartype monitor_service: str or
     ~azure.mgmt.alertsmanagement.models.MonitorService
    :ivar alert_rule: Rule(monitor) which fired alert instance. Depending on
     the monitor service,  this would be ARM id or name of the rule.
    :vartype alert_rule: str
    :ivar source_created_id: Unique Id created by monitor service for each
     alert instance. This could be used to track the issue at the monitor
     service, in case of Nagios, Zabbix, SCOM etc.
    :vartype source_created_id: str
    :ivar smart_group_id: Unique Id of the smart group
    :vartype smart_group_id: str
    :ivar smart_grouping_reason: Verbose reason describing the reason why this
     alert instance is added to a smart group
    :vartype smart_grouping_reason: str
    :ivar start_date_time: Creation time(ISO-8601 format) of alert instance.
    :vartype start_date_time: datetime
    :ivar last_modified_date_time: Last modification time(ISO-8601 format) of
     alert instance.
    :vartype last_modified_date_time: datetime
    :ivar monitor_condition_resolved_date_time: Resolved time(ISO-8601 format)
     of alert instance. This will be updated when monitor service resolves the
     alert instance because the rule condition is no longer met.
    :vartype monitor_condition_resolved_date_time: datetime
    :ivar last_modified_user_name: User who last modified the alert, in case
     of monitor service updates user would be 'system', otherwise name of the
     user.
    :vartype last_modified_user_name: str
    """

    _validation = {
        'severity': {'readonly': True},
        'signal_type': {'readonly': True},
        'alert_state': {'readonly': True},
        'monitor_condition': {'readonly': True},
        'monitor_service': {'readonly': True},
        'alert_rule': {'readonly': True},
        'source_created_id': {'readonly': True},
        'smart_group_id': {'readonly': True},
        'smart_grouping_reason': {'readonly': True},
        'start_date_time': {'readonly': True},
        'last_modified_date_time': {'readonly': True},
        'monitor_condition_resolved_date_time': {'readonly': True},
        'last_modified_user_name': {'readonly': True},
    }

    _attribute_map = {
        'severity': {'key': 'severity', 'type': 'str'},
        'signal_type': {'key': 'signalType', 'type': 'str'},
        'alert_state': {'key': 'alertState', 'type': 'str'},
        'monitor_condition': {'key': 'monitorCondition', 'type': 'str'},
        'target_resource': {'key': 'targetResource', 'type': 'str'},
        'target_resource_name': {'key': 'targetResourceName', 'type': 'str'},
        'target_resource_group': {'key': 'targetResourceGroup', 'type': 'str'},
        'target_resource_type': {'key': 'targetResourceType', 'type': 'str'},
        'monitor_service': {'key': 'monitorService', 'type': 'str'},
        'alert_rule': {'key': 'alertRule', 'type': 'str'},
        'source_created_id': {'key': 'sourceCreatedId', 'type': 'str'},
        'smart_group_id': {'key': 'smartGroupId', 'type': 'str'},
        'smart_grouping_reason': {'key': 'smartGroupingReason', 'type': 'str'},
        'start_date_time': {'key': 'startDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'monitor_condition_resolved_date_time': {'key': 'monitorConditionResolvedDateTime', 'type': 'iso-8601'},
        'last_modified_user_name': {'key': 'lastModifiedUserName', 'type': 'str'},
    }

    def __init__(self, *, target_resource: str=None, target_resource_name: str=None, target_resource_group: str=None, target_resource_type: str=None, **kwargs) -> None:
        super(Essentials, self).__init__(**kwargs)
        self.severity = None
        self.signal_type = None
        self.alert_state = None
        self.monitor_condition = None
        self.target_resource = target_resource
        self.target_resource_name = target_resource_name
        self.target_resource_group = target_resource_group
        self.target_resource_type = target_resource_type
        self.monitor_service = None
        self.alert_rule = None
        self.source_created_id = None
        self.smart_group_id = None
        self.smart_grouping_reason = None
        self.start_date_time = None
        self.last_modified_date_time = None
        self.monitor_condition_resolved_date_time = None
        self.last_modified_user_name = None


class Operation(Model):
    """Operation provided by provider.

    :param name: Name of the operation
    :type name: str
    :param display: Properties of the operation
    :type display: ~azure.mgmt.alertsmanagement.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, *, name: str=None, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(Model):
    """Properties of the operation.

    :param provider: Provider name
    :type provider: str
    :param resource: Resource name
    :type resource: str
    :param operation: Operation name
    :type operation: str
    :param description: Description of the operation
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class SmartGroup(ProxyResource):
    """Set of related alerts grouped together smartly by AMS.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param alerts_count: Total number of alerts in smart group
    :type alerts_count: int
    :ivar smart_group_state: Smart group state. Possible values include:
     'New', 'Acknowledged', 'Closed'
    :vartype smart_group_state: str or
     ~azure.mgmt.alertsmanagement.models.State
    :ivar severity: Severity of smart group is the highest(Sev0 >... > Sev4)
     severity of all the alerts in the group. Possible values include: 'Sev0',
     'Sev1', 'Sev2', 'Sev3', 'Sev4'
    :vartype severity: str or ~azure.mgmt.alertsmanagement.models.Severity
    :ivar start_date_time: Creation time of smart group. Date-Time in ISO-8601
     format.
    :vartype start_date_time: datetime
    :ivar last_modified_date_time: Last updated time of smart group. Date-Time
     in ISO-8601 format.
    :vartype last_modified_date_time: datetime
    :ivar last_modified_user_name: Last modified by user name.
    :vartype last_modified_user_name: str
    :param resources: Summary of target resources in the smart group
    :type resources:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param resource_types: Summary of target resource types in the smart group
    :type resource_types:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param resource_groups: Summary of target resource groups in the smart
     group
    :type resource_groups:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param monitor_services: Summary of monitorServices in the smart group
    :type monitor_services:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param monitor_conditions: Summary of monitorConditions in the smart group
    :type monitor_conditions:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param alert_states: Summary of alertStates in the smart group
    :type alert_states:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param alert_severities: Summary of alertSeverities in the smart group
    :type alert_severities:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupAggregatedProperty]
    :param next_link: The URI to fetch the next page of alerts. Call
     ListNext() with this URI to fetch the next page alerts.
    :type next_link: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'smart_group_state': {'readonly': True},
        'severity': {'readonly': True},
        'start_date_time': {'readonly': True},
        'last_modified_date_time': {'readonly': True},
        'last_modified_user_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'alerts_count': {'key': 'properties.alertsCount', 'type': 'int'},
        'smart_group_state': {'key': 'properties.smartGroupState', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'start_date_time': {'key': 'properties.startDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'properties.lastModifiedDateTime', 'type': 'iso-8601'},
        'last_modified_user_name': {'key': 'properties.lastModifiedUserName', 'type': 'str'},
        'resources': {'key': 'properties.resources', 'type': '[SmartGroupAggregatedProperty]'},
        'resource_types': {'key': 'properties.resourceTypes', 'type': '[SmartGroupAggregatedProperty]'},
        'resource_groups': {'key': 'properties.resourceGroups', 'type': '[SmartGroupAggregatedProperty]'},
        'monitor_services': {'key': 'properties.monitorServices', 'type': '[SmartGroupAggregatedProperty]'},
        'monitor_conditions': {'key': 'properties.monitorConditions', 'type': '[SmartGroupAggregatedProperty]'},
        'alert_states': {'key': 'properties.alertStates', 'type': '[SmartGroupAggregatedProperty]'},
        'alert_severities': {'key': 'properties.alertSeverities', 'type': '[SmartGroupAggregatedProperty]'},
        'next_link': {'key': 'properties.nextLink', 'type': 'str'},
    }

    def __init__(self, *, alerts_count: int=None, resources=None, resource_types=None, resource_groups=None, monitor_services=None, monitor_conditions=None, alert_states=None, alert_severities=None, next_link: str=None, **kwargs) -> None:
        super(SmartGroup, self).__init__(**kwargs)
        self.alerts_count = alerts_count
        self.smart_group_state = None
        self.severity = None
        self.start_date_time = None
        self.last_modified_date_time = None
        self.last_modified_user_name = None
        self.resources = resources
        self.resource_types = resource_types
        self.resource_groups = resource_groups
        self.monitor_services = monitor_services
        self.monitor_conditions = monitor_conditions
        self.alert_states = alert_states
        self.alert_severities = alert_severities
        self.next_link = next_link


class SmartGroupAggregatedProperty(Model):
    """Aggregated property of each type.

    :param name: Name of the type.
    :type name: str
    :param count: Total number of items of type.
    :type count: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
    }

    def __init__(self, *, name: str=None, count: int=None, **kwargs) -> None:
        super(SmartGroupAggregatedProperty, self).__init__(**kwargs)
        self.name = name
        self.count = count


class SmartGroupModification(ProxyResource):
    """Alert Modification details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param properties:
    :type properties:
     ~azure.mgmt.alertsmanagement.models.SmartGroupModificationProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'SmartGroupModificationProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(SmartGroupModification, self).__init__(**kwargs)
        self.properties = properties


class SmartGroupModificationItem(Model):
    """smartGroup modification item.

    :param modification_event: Reason for the modification. Possible values
     include: 'SmartGroupCreated', 'StateChange', 'AlertAdded', 'AlertRemoved'
    :type modification_event: str or
     ~azure.mgmt.alertsmanagement.models.SmartGroupModificationEvent
    :param old_value: Old value
    :type old_value: str
    :param new_value: New value
    :type new_value: str
    :param modified_at: Modified date and time
    :type modified_at: str
    :param modified_by: Modified user details (Principal client name)
    :type modified_by: str
    :param comments: Modification comments
    :type comments: str
    :param description: Description of the modification
    :type description: str
    """

    _attribute_map = {
        'modification_event': {'key': 'modificationEvent', 'type': 'SmartGroupModificationEvent'},
        'old_value': {'key': 'oldValue', 'type': 'str'},
        'new_value': {'key': 'newValue', 'type': 'str'},
        'modified_at': {'key': 'modifiedAt', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'str'},
        'comments': {'key': 'comments', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, modification_event=None, old_value: str=None, new_value: str=None, modified_at: str=None, modified_by: str=None, comments: str=None, description: str=None, **kwargs) -> None:
        super(SmartGroupModificationItem, self).__init__(**kwargs)
        self.modification_event = modification_event
        self.old_value = old_value
        self.new_value = new_value
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.comments = comments
        self.description = description


class SmartGroupModificationProperties(Model):
    """Properties of the smartGroup modification item.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar smart_group_id: Unique Id of the smartGroup for which the history is
     being retrieved
    :vartype smart_group_id: str
    :param modifications: Modification details
    :type modifications:
     list[~azure.mgmt.alertsmanagement.models.SmartGroupModificationItem]
    :param next_link: URL to fetch the next set of results.
    :type next_link: str
    """

    _validation = {
        'smart_group_id': {'readonly': True},
    }

    _attribute_map = {
        'smart_group_id': {'key': 'smartGroupId', 'type': 'str'},
        'modifications': {'key': 'modifications', 'type': '[SmartGroupModificationItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, modifications=None, next_link: str=None, **kwargs) -> None:
        super(SmartGroupModificationProperties, self).__init__(**kwargs)
        self.smart_group_id = None
        self.modifications = modifications
        self.next_link = next_link


class SmartGroupsList(Model):
    """List the alerts.

    :param next_link: URL to fetch the next set of alerts.
    :type next_link: str
    :param value: List of alerts
    :type value: list[~azure.mgmt.alertsmanagement.models.SmartGroup]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[SmartGroup]'},
    }

    def __init__(self, *, next_link: str=None, value=None, **kwargs) -> None:
        super(SmartGroupsList, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class ThrottlingInformation(Model):
    """Optional throttling information for the alert rule.

    :param duration: The required duration (in ISO8601 format) to wait before
     notifying on the alert rule again. The time granularity must be in minutes
     and minimum value is 0 minutes
    :type duration: timedelta
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'duration'},
    }

    def __init__(self, *, duration=None, **kwargs) -> None:
        super(ThrottlingInformation, self).__init__(**kwargs)
        self.duration = duration
