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

from enum import Enum


class ErrorCodeType(str, Enum):

    bad_argument = "BadArgument"
    forbidden = "Forbidden"
    not_found = "NotFound"
    kb_not_found = "KbNotFound"
    unauthorized = "Unauthorized"
    unspecified = "Unspecified"
    endpoint_keys_error = "EndpointKeysError"
    quota_exceeded = "QuotaExceeded"
    qna_runtime_error = "QnaRuntimeError"
    sku_limit_exceeded = "SKULimitExceeded"
    operation_not_found = "OperationNotFound"
    service_error = "ServiceError"
    validation_failure = "ValidationFailure"
    extraction_failure = "ExtractionFailure"
