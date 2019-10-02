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


class AaaaRecord(Model):
    """An AAAA record.

    :param ipv6_address: The IPv6 address of this AAAA record.
    :type ipv6_address: str
    """

    _attribute_map = {
        'ipv6_address': {'key': 'ipv6Address', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AaaaRecord, self).__init__(**kwargs)
        self.ipv6_address = kwargs.get('ipv6_address', None)


class ARecord(Model):
    """An A record.

    :param ipv4_address: The IPv4 address of this A record.
    :type ipv4_address: str
    """

    _attribute_map = {
        'ipv4_address': {'key': 'ipv4Address', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ARecord, self).__init__(**kwargs)
        self.ipv4_address = kwargs.get('ipv4_address', None)


class Resource(Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AzureEntityResource(Resource):
    """The resource model definition for a Azure Resource Manager resource with an
    etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CloudError(Model):
    """CloudError.

    :param error:
    :type error: ~azure.mgmt.dns.v2016_04_01.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, **kwargs):
        super(CloudError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """CloudErrorBody.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~azure.mgmt.dns.v2016_04_01.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(self, **kwargs):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)


class CnameRecord(Model):
    """A CNAME record.

    :param cname: The canonical name for this CNAME record.
    :type cname: str
    """

    _attribute_map = {
        'cname': {'key': 'cname', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CnameRecord, self).__init__(**kwargs)
        self.cname = kwargs.get('cname', None)


class MxRecord(Model):
    """An MX record.

    :param preference: The preference value for this MX record.
    :type preference: int
    :param exchange: The domain name of the mail host for this MX record.
    :type exchange: str
    """

    _attribute_map = {
        'preference': {'key': 'preference', 'type': 'int'},
        'exchange': {'key': 'exchange', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MxRecord, self).__init__(**kwargs)
        self.preference = kwargs.get('preference', None)
        self.exchange = kwargs.get('exchange', None)


class NsRecord(Model):
    """An NS record.

    :param nsdname: The name server name for this NS record.
    :type nsdname: str
    """

    _attribute_map = {
        'nsdname': {'key': 'nsdname', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NsRecord, self).__init__(**kwargs)
        self.nsdname = kwargs.get('nsdname', None)


class ProxyResource(Resource):
    """The resource model definition for a ARM proxy resource. It will have
    everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProxyResource, self).__init__(**kwargs)


class PtrRecord(Model):
    """A PTR record.

    :param ptrdname: The PTR target domain name for this PTR record.
    :type ptrdname: str
    """

    _attribute_map = {
        'ptrdname': {'key': 'ptrdname', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PtrRecord, self).__init__(**kwargs)
        self.ptrdname = kwargs.get('ptrdname', None)


class RecordSet(Model):
    """Describes a DNS record set (a collection of DNS records with the same name
    and type).

    :param id: The ID of the record set.
    :type id: str
    :param name: The name of the record set.
    :type name: str
    :param type: The type of the record set.
    :type type: str
    :param etag: The etag of the record set.
    :type etag: str
    :param metadata: The metadata attached to the record set.
    :type metadata: dict[str, str]
    :param ttl: The TTL (time-to-live) of the records in the record set.
    :type ttl: long
    :param arecords: The list of A records in the record set.
    :type arecords: list[~azure.mgmt.dns.v2016_04_01.models.ARecord]
    :param aaaa_records: The list of AAAA records in the record set.
    :type aaaa_records: list[~azure.mgmt.dns.v2016_04_01.models.AaaaRecord]
    :param mx_records: The list of MX records in the record set.
    :type mx_records: list[~azure.mgmt.dns.v2016_04_01.models.MxRecord]
    :param ns_records: The list of NS records in the record set.
    :type ns_records: list[~azure.mgmt.dns.v2016_04_01.models.NsRecord]
    :param ptr_records: The list of PTR records in the record set.
    :type ptr_records: list[~azure.mgmt.dns.v2016_04_01.models.PtrRecord]
    :param srv_records: The list of SRV records in the record set.
    :type srv_records: list[~azure.mgmt.dns.v2016_04_01.models.SrvRecord]
    :param txt_records: The list of TXT records in the record set.
    :type txt_records: list[~azure.mgmt.dns.v2016_04_01.models.TxtRecord]
    :param cname_record: The CNAME record in the  record set.
    :type cname_record: ~azure.mgmt.dns.v2016_04_01.models.CnameRecord
    :param soa_record: The SOA record in the record set.
    :type soa_record: ~azure.mgmt.dns.v2016_04_01.models.SoaRecord
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': '{str}'},
        'ttl': {'key': 'properties.TTL', 'type': 'long'},
        'arecords': {'key': 'properties.ARecords', 'type': '[ARecord]'},
        'aaaa_records': {'key': 'properties.AAAARecords', 'type': '[AaaaRecord]'},
        'mx_records': {'key': 'properties.MXRecords', 'type': '[MxRecord]'},
        'ns_records': {'key': 'properties.NSRecords', 'type': '[NsRecord]'},
        'ptr_records': {'key': 'properties.PTRRecords', 'type': '[PtrRecord]'},
        'srv_records': {'key': 'properties.SRVRecords', 'type': '[SrvRecord]'},
        'txt_records': {'key': 'properties.TXTRecords', 'type': '[TxtRecord]'},
        'cname_record': {'key': 'properties.CNAMERecord', 'type': 'CnameRecord'},
        'soa_record': {'key': 'properties.SOARecord', 'type': 'SoaRecord'},
    }

    def __init__(self, **kwargs):
        super(RecordSet, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.etag = kwargs.get('etag', None)
        self.metadata = kwargs.get('metadata', None)
        self.ttl = kwargs.get('ttl', None)
        self.arecords = kwargs.get('arecords', None)
        self.aaaa_records = kwargs.get('aaaa_records', None)
        self.mx_records = kwargs.get('mx_records', None)
        self.ns_records = kwargs.get('ns_records', None)
        self.ptr_records = kwargs.get('ptr_records', None)
        self.srv_records = kwargs.get('srv_records', None)
        self.txt_records = kwargs.get('txt_records', None)
        self.cname_record = kwargs.get('cname_record', None)
        self.soa_record = kwargs.get('soa_record', None)


class RecordSetUpdateParameters(Model):
    """Parameters supplied to update a record set.

    :param record_set: Specifies information about the record set being
     updated.
    :type record_set: ~azure.mgmt.dns.v2016_04_01.models.RecordSet
    """

    _attribute_map = {
        'record_set': {'key': 'RecordSet', 'type': 'RecordSet'},
    }

    def __init__(self, **kwargs):
        super(RecordSetUpdateParameters, self).__init__(**kwargs)
        self.record_set = kwargs.get('record_set', None)


class SoaRecord(Model):
    """An SOA record.

    :param host: The domain name of the authoritative name server for this SOA
     record.
    :type host: str
    :param email: The email contact for this SOA record.
    :type email: str
    :param serial_number: The serial number for this SOA record.
    :type serial_number: long
    :param refresh_time: The refresh value for this SOA record.
    :type refresh_time: long
    :param retry_time: The retry time for this SOA record.
    :type retry_time: long
    :param expire_time: The expire time for this SOA record.
    :type expire_time: long
    :param minimum_ttl: The minimum value for this SOA record. By convention
     this is used to determine the negative caching duration.
    :type minimum_ttl: long
    """

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'serial_number': {'key': 'serialNumber', 'type': 'long'},
        'refresh_time': {'key': 'refreshTime', 'type': 'long'},
        'retry_time': {'key': 'retryTime', 'type': 'long'},
        'expire_time': {'key': 'expireTime', 'type': 'long'},
        'minimum_ttl': {'key': 'minimumTTL', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(SoaRecord, self).__init__(**kwargs)
        self.host = kwargs.get('host', None)
        self.email = kwargs.get('email', None)
        self.serial_number = kwargs.get('serial_number', None)
        self.refresh_time = kwargs.get('refresh_time', None)
        self.retry_time = kwargs.get('retry_time', None)
        self.expire_time = kwargs.get('expire_time', None)
        self.minimum_ttl = kwargs.get('minimum_ttl', None)


class SrvRecord(Model):
    """An SRV record.

    :param priority: The priority value for this SRV record.
    :type priority: int
    :param weight: The weight value for this SRV record.
    :type weight: int
    :param port: The port value for this SRV record.
    :type port: int
    :param target: The target domain name for this SRV record.
    :type target: str
    """

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'weight': {'key': 'weight', 'type': 'int'},
        'port': {'key': 'port', 'type': 'int'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SrvRecord, self).__init__(**kwargs)
        self.priority = kwargs.get('priority', None)
        self.weight = kwargs.get('weight', None)
        self.port = kwargs.get('port', None)
        self.target = kwargs.get('target', None)


class SubResource(Model):
    """SubResource.

    :param id: Resource Id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubResource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)


class TxtRecord(Model):
    """A TXT record.

    :param value: The text value of this TXT record.
    :type value: list[str]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(TxtRecord, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class Zone(TrackedResource):
    """Describes a DNS zone.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param etag: The etag of the zone.
    :type etag: str
    :param max_number_of_record_sets: The maximum number of record sets that
     can be created in this DNS zone.  This is a read-only property and any
     attempt to set this value will be ignored.
    :type max_number_of_record_sets: long
    :param number_of_record_sets: The current number of record sets in this
     DNS zone.  This is a read-only property and any attempt to set this value
     will be ignored.
    :type number_of_record_sets: long
    :ivar name_servers: The name servers for this DNS zone. This is a
     read-only property and any attempt to set this value will be ignored.
    :vartype name_servers: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'name_servers': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'max_number_of_record_sets': {'key': 'properties.maxNumberOfRecordSets', 'type': 'long'},
        'number_of_record_sets': {'key': 'properties.numberOfRecordSets', 'type': 'long'},
        'name_servers': {'key': 'properties.nameServers', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(Zone, self).__init__(**kwargs)
        self.etag = kwargs.get('etag', None)
        self.max_number_of_record_sets = kwargs.get('max_number_of_record_sets', None)
        self.number_of_record_sets = kwargs.get('number_of_record_sets', None)
        self.name_servers = None


class ZoneDeleteResult(Model):
    """The response to a Zone Delete operation.

    :param azure_async_operation: Users can perform a Get on
     Azure-AsyncOperation to get the status of their delete Zone operations.
    :type azure_async_operation: str
    :param status: Possible values include: 'InProgress', 'Succeeded',
     'Failed'
    :type status: str or ~azure.mgmt.dns.v2016_04_01.models.OperationStatus
    :param status_code: Possible values include: 'Continue',
     'SwitchingProtocols', 'OK', 'Created', 'Accepted',
     'NonAuthoritativeInformation', 'NoContent', 'ResetContent',
     'PartialContent', 'MultipleChoices', 'Ambiguous', 'MovedPermanently',
     'Moved', 'Found', 'Redirect', 'SeeOther', 'RedirectMethod', 'NotModified',
     'UseProxy', 'Unused', 'TemporaryRedirect', 'RedirectKeepVerb',
     'BadRequest', 'Unauthorized', 'PaymentRequired', 'Forbidden', 'NotFound',
     'MethodNotAllowed', 'NotAcceptable', 'ProxyAuthenticationRequired',
     'RequestTimeout', 'Conflict', 'Gone', 'LengthRequired',
     'PreconditionFailed', 'RequestEntityTooLarge', 'RequestUriTooLong',
     'UnsupportedMediaType', 'RequestedRangeNotSatisfiable',
     'ExpectationFailed', 'UpgradeRequired', 'InternalServerError',
     'NotImplemented', 'BadGateway', 'ServiceUnavailable', 'GatewayTimeout',
     'HttpVersionNotSupported'
    :type status_code: str or
     ~azure.mgmt.dns.v2016_04_01.models.HttpStatusCode
    :param request_id:
    :type request_id: str
    """

    _attribute_map = {
        'azure_async_operation': {'key': 'azureAsyncOperation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'status_code': {'key': 'statusCode', 'type': 'HttpStatusCode'},
        'request_id': {'key': 'requestId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ZoneDeleteResult, self).__init__(**kwargs)
        self.azure_async_operation = kwargs.get('azure_async_operation', None)
        self.status = kwargs.get('status', None)
        self.status_code = kwargs.get('status_code', None)
        self.request_id = kwargs.get('request_id', None)