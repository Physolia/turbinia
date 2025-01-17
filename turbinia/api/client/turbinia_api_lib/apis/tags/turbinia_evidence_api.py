# coding: utf-8

"""
    Turbinia API Server

    Turbinia is an open-source framework for deploying,managing, and running distributed forensic workloads  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from turbinia_api_lib.paths.api_evidence_types_evidence_type.get import GetEvidenceAttributes
from turbinia_api_lib.paths.api_evidence_evidence_id.get import GetEvidenceById
from turbinia_api_lib.paths.api_evidence_summary.get import GetEvidenceSummary
from turbinia_api_lib.paths.api_evidence_types.get import GetEvidenceTypes
from turbinia_api_lib.paths.api_evidence_query.get import QueryEvidence
from turbinia_api_lib.paths.api_evidence_upload.post import UploadEvidence


class TurbiniaEvidenceApi(
    GetEvidenceAttributes,
    GetEvidenceById,
    GetEvidenceSummary,
    GetEvidenceTypes,
    QueryEvidence,
    UploadEvidence,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
