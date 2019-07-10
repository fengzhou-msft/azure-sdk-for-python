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


class Authorization(Model):
    """Authorization info used to access a resource (like code repository).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar authorization_type: Required. Type of authorization. Default value:
     "personalAccessToken" .
    :vartype authorization_type: str
    :param parameters: Authorization parameters corresponding to the
     authorization type.
    :type parameters: dict[str, str]
    """

    _validation = {
        'authorization_type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'authorization_type': {'key': 'authorizationType', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
    }

    authorization_type = "personalAccessToken"

    def __init__(self, **kwargs):
        super(Authorization, self).__init__(**kwargs)
        self.parameters = kwargs.get('parameters', None)


class BootstrapConfiguration(Model):
    """Configuration used to bootstrap a Pipeline.

    All required parameters must be populated in order to send to Azure.

    :param repository: Repository containing the source code for the pipeline.
    :type repository: ~microsoft.devops.models.CodeRepository
    :param template: Required. Template used to bootstrap the pipeline.
    :type template: ~microsoft.devops.models.PipelineTemplate
    """

    _validation = {
        'template': {'required': True},
    }

    _attribute_map = {
        'repository': {'key': 'repository', 'type': 'CodeRepository'},
        'template': {'key': 'template', 'type': 'PipelineTemplate'},
    }

    def __init__(self, **kwargs):
        super(BootstrapConfiguration, self).__init__(**kwargs)
        self.repository = kwargs.get('repository', None)
        self.template = kwargs.get('template', None)


class CloudError(Model):
    """An error response from the Pipelines Resource Provider.

    :param error:
    :type error: ~microsoft.devops.models.CloudErrorBody
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
    """An error response from the Pipelines Resource Provider.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for display in a user interface.
    :type message: str
    :param target: The target of the particular error. For example, the name
     of the property in error or the method where the error occurred.
    :type target: str
    :param details: A list of additional details about the error.
    :type details: list[~microsoft.devops.models.CloudErrorBody]
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


class CodeRepository(Model):
    """Repository containing the source code for a pipeline.

    All required parameters must be populated in order to send to Azure.

    :param repository_type: Required. Type of code repository. Possible values
     include: 'gitHub', 'vstsGit'
    :type repository_type: str or ~microsoft.devops.models.CodeRepositoryType
    :param id: Required. Unique immutable identifier of the code repository.
    :type id: str
    :param default_branch: Required. Default branch used to configure
     Continuous Integration (CI) in the pipeline.
    :type default_branch: str
    :param authorization: Authorization info to access the code repository.
    :type authorization: ~microsoft.devops.models.Authorization
    :param properties: Repository-specific properties.
    :type properties: dict[str, str]
    """

    _validation = {
        'repository_type': {'required': True},
        'id': {'required': True},
        'default_branch': {'required': True},
    }

    _attribute_map = {
        'repository_type': {'key': 'repositoryType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'authorization': {'key': 'authorization', 'type': 'Authorization'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(CodeRepository, self).__init__(**kwargs)
        self.repository_type = kwargs.get('repository_type', None)
        self.id = kwargs.get('id', None)
        self.default_branch = kwargs.get('default_branch', None)
        self.authorization = kwargs.get('authorization', None)
        self.properties = kwargs.get('properties', None)


class InputDescriptor(Model):
    """Representation of a pipeline template input parameter.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Identifier of the input parameter.
    :type id: str
    :param description: Description of the input parameter.
    :type description: str
    :param type: Required. Data type of the value of the input parameter.
     Possible values include: 'String', 'SecureString', 'Int', 'Bool',
     'Authorization'
    :type type: str or ~microsoft.devops.models.InputDataType
    :param possible_values: List of possible values for the input parameter.
    :type possible_values: list[~microsoft.devops.models.InputValue]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'},
    }

    def __init__(self, **kwargs):
        super(InputDescriptor, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.description = kwargs.get('description', None)
        self.type = kwargs.get('type', None)
        self.possible_values = kwargs.get('possible_values', None)


class InputValue(Model):
    """Representation of a pipeline template input parameter value.

    :param value: Value of an input parameter.
    :type value: str
    :param display_value: Description of the input parameter value.
    :type display_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'display_value': {'key': 'displayValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(InputValue, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.display_value = kwargs.get('display_value', None)


class Operation(Model):
    """Properties of an Operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the operation.
    :vartype name: str
    :param is_data_action: Indicates whether the operation applies to
     data-plane.
    :type is_data_action: str
    :ivar operation: Friendly name of the operation.
    :vartype operation: str
    :ivar resource: Friendly name of the resource type the operation applies
     to.
    :vartype resource: str
    :ivar description: Friendly description of the operation.
    :vartype description: str
    :ivar provider: Friendly name of the resource provider.
    :vartype provider: str
    """

    _validation = {
        'name': {'readonly': True},
        'operation': {'readonly': True},
        'resource': {'readonly': True},
        'description': {'readonly': True},
        'provider': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'operation': {'key': 'display.operation', 'type': 'str'},
        'resource': {'key': 'display.resource', 'type': 'str'},
        'description': {'key': 'display.description', 'type': 'str'},
        'provider': {'key': 'display.provider', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.is_data_action = kwargs.get('is_data_action', None)
        self.operation = None
        self.resource = None
        self.description = None
        self.provider = None


class OrganizationReference(Model):
    """Reference to an Azure DevOps Organization.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Unique immutable identifier for the Azure DevOps Organization.
    :vartype id: str
    :param name: Required. Name of the Azure DevOps Organization.
    :type name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OrganizationReference, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)


class Resource(Model):
    """An Azure Resource Manager (ARM) resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar type: Resource Type
    :vartype type: str
    :param tags: Resource Tags
    :type tags: dict[str, str]
    :param location: Resource Location
    :type location: str
    :ivar name: Resource Name
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
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)
        self.name = None


class Pipeline(Resource):
    """Azure DevOps Pipeline used to configure Continuous Integration (CI) &
    Continuous Delivery (CD) for Azure resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar type: Resource Type
    :vartype type: str
    :param tags: Resource Tags
    :type tags: dict[str, str]
    :param location: Resource Location
    :type location: str
    :ivar name: Resource Name
    :vartype name: str
    :ivar pipeline_id: Unique identifier of the Azure Pipeline within the
     Azure DevOps Project.
    :vartype pipeline_id: int
    :param organization: Required. Reference to the Azure DevOps Organization
     containing the Pipeline.
    :type organization: ~microsoft.devops.models.OrganizationReference
    :param project: Required. Reference to the Azure DevOps Project containing
     the Pipeline.
    :type project: ~microsoft.devops.models.ProjectReference
    :param bootstrap_configuration: Required. Configuration used to bootstrap
     the Pipeline.
    :type bootstrap_configuration:
     ~microsoft.devops.models.BootstrapConfiguration
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'pipeline_id': {'readonly': True},
        'organization': {'required': True},
        'project': {'required': True},
        'bootstrap_configuration': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pipeline_id': {'key': 'properties.pipelineId', 'type': 'int'},
        'organization': {'key': 'properties.organization', 'type': 'OrganizationReference'},
        'project': {'key': 'properties.project', 'type': 'ProjectReference'},
        'bootstrap_configuration': {'key': 'properties.bootstrapConfiguration', 'type': 'BootstrapConfiguration'},
    }

    def __init__(self, **kwargs):
        super(Pipeline, self).__init__(**kwargs)
        self.pipeline_id = None
        self.organization = kwargs.get('organization', None)
        self.project = kwargs.get('project', None)
        self.bootstrap_configuration = kwargs.get('bootstrap_configuration', None)


class PipelineTemplate(Model):
    """Template used to bootstrap the pipeline.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique identifier of the pipeline template.
    :type id: str
    :param parameters: Dictionary of input parameters used in the pipeline
     template.
    :type parameters: dict[str, str]
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(PipelineTemplate, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.parameters = kwargs.get('parameters', None)


class PipelineTemplateDefinition(Model):
    """Definition of a pipeline template.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique identifier of the pipeline template.
    :type id: str
    :param description: Description of the pipeline enabled by the template.
    :type description: str
    :param inputs: List of input parameters required by the template to create
     a pipeline.
    :type inputs: list[~microsoft.devops.models.InputDescriptor]
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[InputDescriptor]'},
    }

    def __init__(self, **kwargs):
        super(PipelineTemplateDefinition, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.description = kwargs.get('description', None)
        self.inputs = kwargs.get('inputs', None)


class PipelineTemplateDefinitionListResult(Model):
    """Result of a request to list all pipeline template definitions.

    :param value: List of pipeline template definitions.
    :type value: list[~microsoft.devops.models.PipelineTemplateDefinition]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PipelineTemplateDefinition]'},
    }

    def __init__(self, **kwargs):
        super(PipelineTemplateDefinitionListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class PipelineUpdateParameters(Model):
    """Request payload used to update an existing Azure Pipeline.

    :param tags: Dictionary of key-value pairs to be set as tags on the Azure
     Pipeline. This will overwrite any existing tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(PipelineUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class ProjectReference(Model):
    """Reference to an Azure DevOps Project.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Unique immutable identifier of the Azure DevOps Project.
    :vartype id: str
    :param name: Required. Name of the Azure DevOps Project.
    :type name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProjectReference, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)
