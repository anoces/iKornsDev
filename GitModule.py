


# /*
# |==========================================================================|
# | IKORNS ENTERPRISE SYSTEM ::: SOURCE CODE MASTER CONTROL HEADER           |
# |==========================================================================|
# | SYSTEM            ::: IKORNS LOG ENGINE SYSTEM                           |
# | PROJECT CODE      ::: IPJ001 - AleMesAPI                                 |
# | SYSTEM TYPE       ::: ENTERPRISE DISTRIBUTED INTELLIGENT LOG SYSTEM      |
# | ARCHITECTURE      ::: DISTRIBUTED / MICROSERVICE / AI-READY / SOC-READY  |
# | MODULE            ::: <MODULE_NAME>                                      |
# | SUB MODULE        ::: <SUB_MODULE_NAME>                                  |
# | FILE              ::: <FILE_NAME>                                        |
# | FILE PATH         ::: <FILE_PATH>                                        |
# | LANGUAGE          ::: JavaScript / TypeScript / Node.js                  |
# | ENVIRONMENT       ::: DEV / TEST / UAT / STAGING / PROD                  |
# | BUILD VERSION     ::: V0.0.1                                             |
# | GIT BRANCH        ::: <GIT_BRANCH>                                       |
# | GIT COMMIT ID     ::: <GIT_COMMIT_ID>                                    |
# | RELEASE TAG       ::: <RELEASE_TAG>                                      |
# |==========================================================================|
# | DOCUMENT CONTROL  :::                                                    |
# | DOCUMENT ID       ::: IPJ001-<MODULE>-SRC-001                            |
# | TEMPLATE VERSION  ::: HEADER-v1.0.0                                      |
# | HEADER STANDARD   ::: IKORNS-ENTERPRISE-SOURCE-HEADER                    |
# | SOURCE TEMPLATE   ::: ALEMESAPI/structure/StructureLogSystemRev001.log   |
# | DOCUMENT STATUS   ::: DRAFT / REVIEW / APPROVED / LOCKED                 |
# | CREATED DATE      ::: YYYY-MM-DD HH:mm:ss UTC                            |
# | LAST MODIFIED     ::: YYYY-MM-DD HH:mm:ss UTC                            |
# |==========================================================================|
# | OWNERSHIP         :::                                                    |
# | AUTHOR            ::: IKORNS                                             |
# | CODE OWNER        ::: IKORNS                                             |
# | SYSTEM OWNER      ::: IKORNS                                             |
# | REVIEWED BY       ::: <REVIEWER_NAME>                                    |
# | APPROVED BY       ::: <APPROVER_NAME>                                    |
# | MAINTAINER        ::: <MAINTAINER_NAME>                                  |
# | PERMISSION        ::: OWNER / ADMIN / DEVELOPER / AUDITOR                |
# |==========================================================================|
# | CLASSIFICATION    :::                                                    |
# | SECURITY LEVEL    ::: INTERNAL / RESTRICTED / CONFIDENTIAL / SECRET      |
# | DATA SENSITIVITY  ::: LOW / MEDIUM / HIGH / CRITICAL                     |
# | BUSINESS IMPACT   ::: LOW / MEDIUM / HIGH / CRITICAL                     |
# | ACCESS CONTROL    ::: RBAC REQUIRED                                      |
# | AUTHORIZATION     ::: REQUIRED BEFORE MODIFICATION                       |
# | ENCRYPTION        ::: ENABLED / REQUIRED                                 |
# | SECRET HANDLING   ::: DO NOT HARDCODE SECRET / USE ENV ONLY              |
# |==========================================================================|
# | COMPLIANCE        :::                                                    |
# | ISO STANDARD      ::: ISO/IEC 27001 / ISO/IEC 27002                      |
# | AUDIT STANDARD    ::: INTERNAL AUDIT / EXTERNAL AUDIT READY              |
# | SECURITY STANDARD ::: SOC 2 TYPE II READY                                |
# | PRIVACY STANDARD  ::: PDPA / GDPR READY IF APPLICABLE                    |
# | LOG STANDARD      ::: STRUCTURED LOG / JSON LOG / UTC TIME               |
# | RETENTION POLICY  ::: FOLLOW ORGANIZATION DATA RETENTION POLICY          |
# |==========================================================================|
# | PURPOSE           :::                                                    |
# | This source file is part of the IKORNS Enterprise Core Engine.           |
# | It is designed for production-grade system development, auditability,    |
# | traceability, security control, observability, and future AI integration.|
# |==========================================================================|
# | DESCRIPTION       :::                                                    |
# | <WRITE_FILE_DESCRIPTION_HERE>                                            |
# |                                                                          |
# | RESPONSIBILITIES  :::                                                    |
# | - <RESPONSIBILITY_01>                                                    |
# | - <RESPONSIBILITY_02>                                                    |
# | - <RESPONSIBILITY_03>                                                    |
# | - <RESPONSIBILITY_04>                                                    |
# |==========================================================================|
# | CORE FUNCTION     :::                                                    |
# | PRIMARY ROLE      ::: <PRIMARY_FUNCTION_OF_THIS_FILE>                    |
# | INPUT SOURCE      ::: <INPUT_SOURCE>                                     |
# | OUTPUT TARGET     ::: <OUTPUT_TARGET>                                    |
# | PROCESS TYPE      ::: SYNC / ASYNC / EVENT-DRIVEN / SCHEDULED            |
# | EXECUTION MODE    ::: SINGLE / BATCH / STREAM / REALTIME                 |
# | DEPENDENCY LEVEL  ::: LOW / MEDIUM / HIGH / CRITICAL                     |
# |==========================================================================|
# | TRACEABILITY      :::                                                    |
# | TRACE ID          ::: AUTO-GENERATED PER REQUEST                         |
# | CORRELATION ID    ::: REQUIRED                                           |
# | REQUEST ID        ::: REQUIRED                                           |
# | SESSION ID        ::: OPTIONAL / REQUIRED                                |
# | USER ID TRACKING  ::: MASKED / HASHED / INTERNAL ONLY                    |
# | EVENT ID          ::: REQUIRED FOR SYSTEM EVENTS                         |
# | TIMEZONE POLICY   ::: UTC ONLY                                           |
# | TIMESTAMP FORMAT  ::: ISO 8601                                           |
# |==========================================================================|
# | AUDIT CONTROL     :::                                                    |
# | AUDIT LOG         ::: REQUIRED                                           |
# | CHANGE LOG        ::: REQUIRED                                           |
# | ACCESS LOG        ::: REQUIRED FOR SENSITIVE ACTIONS                     |
# | ERROR LOG         ::: REQUIRED                                           |
# | SECURITY LOG      ::: REQUIRED FOR SECURITY EVENTS                       |
# | IMMUTABLE LOG     ::: RECOMMENDED                                        |
# | LOG VERIFICATION  ::: REQUIRED FOR WRITE OPERATIONS                      |
# |==========================================================================|
# | DATA GOVERNANCE   :::                                                    |
# | DATA TYPE         ::: SYSTEM / USER / SECURITY / OPERATIONAL / ANALYTICS |
# | PII HANDLING      ::: MASK / HASH / ENCRYPT                              |
# | DATA MASKING      ::: REQUIRED FOR SENSITIVE DATA                        |
# | DATA VALIDATION   ::: REQUIRED BEFORE PROCESSING                         |
# | DATA SANITIZATION ::: REQUIRED BEFORE STORAGE / OUTPUT                   |
# | DATA RETENTION    ::: 90 DAYS / 1 YEAR / CUSTOM POLICY                   |
# | BACKUP POLICY     ::: REQUIRED                                           |
# | DELETE POLICY     ::: SOFT DELETE / HARD DELETE / ARCHIVE                |
# |==========================================================================|
# | RISK CONTROL      :::                                                    |
# | RISK LEVEL        ::: LOW / MEDIUM / HIGH / CRITICAL                     |
# | IMPACT SCOPE      ::: MODULE / SERVICE / SYSTEM-WIDE / SECURITY / AUDIT  |
# | FAILURE POLICY    ::: FAIL-SAFE / FAIL-CLOSED / FAIL-OPEN                |
# | RECOVERY POLICY   ::: AUTO-RETRY / MANUAL REVIEW / INCIDENT REPORT       |
# | ERROR HANDLING    ::: REQUIRED                                           |
# | EXCEPTION POLICY  ::: NO SILENT FAILURE                                  |
# | INCIDENT LEVEL    ::: LOW / MEDIUM / HIGH / SEV-1                        |
# |==========================================================================|
# | SECURITY CONTROL  :::                                                    |
# | INPUT VALIDATION  ::: REQUIRED                                           |
# | OUTPUT ENCODING   ::: REQUIRED IF USER-FACING                            |
# | RATE LIMITING     ::: REQUIRED IF API / PUBLIC ENTRY                     |
# | AUTHENTICATION    ::: REQUIRED IF PROTECTED RESOURCE                     |
# | AUTHORIZATION     ::: REQUIRED IF ROLE-BASED ACTION                      |
# | TOKEN POLICY      ::: ENV ONLY / ROTATION REQUIRED                       |
# | CREDENTIAL POLICY ::: NEVER COMMIT CREDENTIALS                           |
# |==========================================================================|
# | QUALITY CONTROL   :::                                                    |
# | CODE REVIEW       ::: REQUIRED BEFORE MERGE                              |
# | TEST REQUIRED     ::: UNIT / INTEGRATION / SECURITY / REGRESSION         |
# | LINT STANDARD     ::: ESLINT / PROJECT STANDARD                          |
# | FORMAT STANDARD   ::: PRETTIER / PROJECT STANDARD                        |
# | TYPE CHECK        ::: REQUIRED IF TYPESCRIPT                             |
# | STATIC ANALYSIS   ::: RECOMMENDED                                        |
# | DEPLOYMENT GATE   ::: CI/CD APPROVAL REQUIRED                            |
# |==========================================================================|
# | PERFORMANCE       :::                                                    |
# | PERFORMANCE LEVEL ::: STANDARD / HIGH / CRITICAL                         |
# | LATENCY TARGET    ::: <LATENCY_TARGET>                                   |
# | THROUGHPUT TARGET ::: <THROUGHPUT_TARGET>                                |
# | MEMORY POLICY     ::: NO MEMORY LEAK / MONITOR REQUIRED                  |
# | CPU POLICY        ::: OPTIMIZED FOR PRODUCTION                           |
# | SCALE POLICY      ::: HORIZONTAL SCALE READY                             |
# |==========================================================================|
# | OBSERVABILITY     :::                                                    |
# | METRICS           ::: REQUIRED                                           |
# | LOGGING           ::: REQUIRED                                           |
# | TRACING           ::: REQUIRED FOR CORE FLOW                             |
# | HEALTH CHECK      ::: REQUIRED IF SERVICE MODULE                         |
# | ALERTING          ::: REQUIRED FOR CRITICAL FAILURE                      |
# | DASHBOARD         ::: RECOMMENDED                                        |
# |==========================================================================|
# | DEPENDENCIES      :::                                                    |
# | INTERNAL MODULES  ::: <INTERNAL_MODULE_LIST>                             |
# | EXTERNAL MODULES  ::: <EXTERNAL_MODULE_LIST>                             |
# | DATABASE          ::: <DATABASE_NAME_OR_NONE>                            |
# | MESSAGE QUEUE     ::: <QUEUE_NAME_OR_NONE>                               |
# | CACHE             ::: <CACHE_NAME_OR_NONE>                               |
# | THIRD PARTY API   ::: <API_NAME_OR_NONE>                                 |
# |==========================================================================|
# | CONFIGURATION     :::                                                    |
# | ENV REQUIRED      ::: YES / NO                                           |
# | CONFIG FILE       ::: <CONFIG_FILE_PATH>                                 |
# | ENV VARIABLES     ::: <ENV_VARIABLE_LIST>                                |
# | DEFAULT CONFIG    ::: <DEFAULT_CONFIG_POLICY>                            |
# | CONFIG VALIDATION ::: REQUIRED                                           |
# |==========================================================================|
# | CHANGE CONTROL    :::                                                    |
# | CHANGE REQUEST ID ::: CR-YYYYMMDD-001                                    |
# | CHANGE TYPE       ::: FEATURE / FIX / SECURITY / REFACTOR / HOTFIX       |
# | CHANGE SUMMARY    ::: <CHANGE_SUMMARY>                                   |
# | BREAKING CHANGE   ::: YES / NO                                           |
# | MIGRATION NEEDED  ::: YES / NO                                           |
# | ROLLBACK PLAN     ::: REQUIRED                                           |
# |==========================================================================|
# | VERSION HISTORY   :::                                                    |
# | v0.0.1            ::: Initial enterprise source header                   |
# |==========================================================================|
# | CODING RULES      :::                                                    |
# | - DO NOT modify this file without authorization.                         |
# | - DO NOT hardcode secrets, tokens, passwords, or credentials.            |
# | - DO NOT remove audit, security, traceability, or error controls.        |
# | - DO NOT bypass validation, logging, or permission checks.               |
# | - DO NOT change public behavior without change request approval.         |
# | - EVERY change must be traceable by commit, author, date, and reason.    |
# | - EVERY critical function must include error handling.                   |
# | - EVERY production path must be observable, testable, and reviewable.    |
# |==========================================================================|
# | WARNING           :::                                                    |
# | THIS FILE IS PART OF THE IKORNS ENTERPRISE CORE SYSTEM.                  |
# | UNAUTHORIZED MODIFICATION MAY BREAK SECURITY, AUDIT, OR SYSTEM FLOW.     |
# |==========================================================================|
# */

# -*- coding: utf-8 -*-
"""
===============================================================================
IKORNS DEV SYSTEM ::: SOURCE CODE MASTER CONTROL
===============================================================================
FILE         : GitModule.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Module
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Bridge module between console layer and git services.

TH:
    โมดูลกลางเชื่อม Console กับ Git Services

POSITION:
    scripts/iKornsDevGit.py
        -> modules/git/GitModule.py
            -> services/git/*

THIS FILE MUST:
    - normalize request
    - route operation
    - return structured result

THIS FILE MUST NOT:
    - run git subprocess directly
    - store credentials
    - change console flow
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


try:
    from services.git.GitExecutionService import GitExecutionService
except Exception:
    GitExecutionService = None


SUPPORTED_OPERATIONS = {
    "GIT_STATUS",
    "STAGE_SELECTED",
    "STAGE_ALL",
    "COMMIT",
    "PUSH",
    "PULL",
    "PUBLISH_FLOW",
}


@dataclass
class GitModuleRequest:
    operation: str
    paths: List[str] = field(default_factory=list)
    commit_message: str = ""
    stage_all: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)

    def normalized_operation(self) -> str:
        return str(self.operation or "").strip().upper()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "operation": self.operation,
            "paths": list(self.paths),
            "commit_message": self.commit_message,
            "stage_all": self.stage_all,
            "metadata": dict(self.metadata),
        }


@dataclass
class GitModuleResult:
    success: bool
    status: str
    code: str
    message: str
    operation: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "status": self.status,
            "code": self.code,
            "message": self.message,
            "operation": self.operation,
            "data": dict(self.data),
            "warnings": list(self.warnings),
            "errors": list(self.errors),
            "created_at": self.created_at,
        }

    @classmethod
    def ok(
        cls,
        operation: str,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        warnings: Optional[List[str]] = None,
    ) -> "GitModuleResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_MODULE_PASS",
            message=message,
            operation=operation,
            data=data or {},
            warnings=warnings or [],
        )

    @classmethod
    def fail(
        cls,
        operation: str,
        message: str,
        errors: Optional[List[str]] = None,
        warnings: Optional[List[str]] = None,
    ) -> "GitModuleResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_MODULE_FAIL",
            message=message,
            operation=operation,
            errors=errors or [],
            warnings=warnings or [],
        )


class GitModule:
    """
    EN:
        Main Git module router.

    TH:
        ตัวกลาง route operation ของ Git
    """

    def __init__(self) -> None:
        self.execution_service = (
            GitExecutionService()
            if GitExecutionService is not None
            else None
        )

    def validate_operation(self, operation: str) -> Optional[GitModuleResult]:
        clean = str(operation or "").strip().upper()

        if not clean:
            return GitModuleResult.fail(
                operation="UNKNOWN",
                message="Operation is required.",
                errors=["operation is empty"],
            )

        if clean not in SUPPORTED_OPERATIONS:
            return GitModuleResult.fail(
                operation=clean,
                message="Unsupported Git operation.",
                errors=[f"unsupported operation: {clean}"],
            )

        if self.execution_service is None:
            return GitModuleResult.fail(
                operation=clean,
                message="GitExecutionService is unavailable.",
                errors=["execution service import failed"],
            )

        return None

    def execute(self, request: GitModuleRequest) -> GitModuleResult:
        validation_error = self.validate_operation(
            request.normalized_operation()
        )

        if validation_error:
            return validation_error

        operation = request.normalized_operation()

        try:
            if operation == "GIT_STATUS":
                result = self.execution_service.status()

            elif operation == "STAGE_SELECTED":
                result = self.execution_service.stage_selected(
                    request.paths
                )

            elif operation == "STAGE_ALL":
                result = self.execution_service.stage_all()

            elif operation == "COMMIT":
                result = self.execution_service.commit(
                    request.commit_message
                )

            elif operation == "PUSH":
                result = self.execution_service.push()

            elif operation == "PULL":
                result = self.execution_service.pull()

            elif operation == "PUBLISH_FLOW":
                result = self.execution_service.publish_flow(
                    commit_message=request.commit_message,
                    stage_all=request.stage_all,
                    selected_paths=request.paths,
                )

            else:
                return GitModuleResult.fail(
                    operation=operation,
                    message="Unhandled Git operation.",
                    errors=[f"operation routing missing: {operation}"],
                )

            payload = (
                result.to_dict()
                if hasattr(result, "to_dict")
                else {"result": str(result)}
            )

            return GitModuleResult.ok(
                operation=operation,
                message=f"{operation} completed.",
                data=payload,
                warnings=payload.get("warnings", []),
            )

        except Exception as exc:
            return GitModuleResult.fail(
                operation=operation,
                message=f"{operation} crashed.",
                errors=[f"{type(exc).__name__}: {exc}"],
            )


def execute_git_operation(
    operation: str,
    paths: Optional[List[str]] = None,
    commit_message: str = "",
    stage_all: bool = True,
    metadata: Optional[Dict[str, Any]] = None,
) -> GitModuleResult:
    module = GitModule()

    request = GitModuleRequest(
        operation=operation,
        paths=paths or [],
        commit_message=commit_message,
        stage_all=stage_all,
        metadata=metadata or {},
    )

    return module.execute(request)


__all__ = [
    "GitModuleRequest",
    "GitModuleResult",
    "GitModule",
    "execute_git_operation",
]