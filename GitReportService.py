


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
FILE         : GitReportService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Report Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Exports iKornsDevGit operation results to MD, JSON, and LOG files.

TH:
    ส่งออกผลลัพธ์ iKornsDevGit เป็นไฟล์ MD, JSON และ LOG

POSITION:
    GitExecutionService / GitModule -> GitReportService -> sources/reports/git/

THIS FILE MUST:
    - write .md
    - write .json
    - write .log
    - use dynamic paths
    - return structured report result

THIS FILE MUST NOT:
    - run git commands
    - commit
    - push
    - pull
    - store credentials
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import json
import os
import secrets
import traceback


SERVICE_NAME = "GitReportService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENCODING = "utf-8"
ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"
ENV_GIT_REPORT_ROOT = "IKORNS_GIT_REPORT_ROOT"

DEFAULT_TIMESTAMP_FORMAT = "%y%m%d%H%M%S"
DEFAULT_RANDOM_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


@dataclass
class GitReportResult:
    success: bool
    status: str
    code: str
    message: str
    report_id: str = ""
    paths: Dict[str, str] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "status": self.status,
            "code": self.code,
            "message": self.message,
            "report_id": self.report_id,
            "paths": dict(self.paths),
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "created_at": self.created_at,
        }

    @classmethod
    def ok(cls, message: str, report_id: str, paths: Dict[str, str]) -> "GitReportResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_REPORT_CREATED",
            message=message,
            report_id=report_id,
            paths=paths,
        )

    @classmethod
    def fail(cls, message: str, errors: Optional[List[str]] = None) -> "GitReportResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_REPORT_FAILED",
            message=message,
            errors=errors or [],
        )


def discover_project_root() -> Path:
    env_root = os.environ.get(ENV_IPROJECTS_ROOT)
    if env_root:
        return Path(env_root).expanduser().resolve()

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "iKorns" / "iKornsDev").exists():
            return parent.resolve()

    return current.parents[6].resolve()


def discover_git_report_root() -> Path:
    env_root = os.environ.get(ENV_GIT_REPORT_ROOT)
    if env_root:
        return Path(env_root).expanduser().resolve()

    return discover_project_root() / "iKorns" / "iKornsDev" / "sources" / "reports" / "git"


def build_report_id() -> str:
    now = datetime.now()
    timestamp = now.strftime(DEFAULT_TIMESTAMP_FORMAT)
    millisecond = f"{now.microsecond // 1000:03d}"
    random_part = "".join(secrets.choice(DEFAULT_RANDOM_POOL) for _ in range(6))
    return f"{timestamp}-{millisecond}-{random_part}"


def normalize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    safe = dict(payload or {})
    safe.setdefault("tool", "iKornsDevGit")
    safe.setdefault("report_type", "Git Operation Report")
    safe.setdefault("generated_at", datetime.now().isoformat(timespec="seconds"))
    safe.setdefault("service", SERVICE_NAME)
    safe.setdefault("service_version", SERVICE_VERSION)
    safe.setdefault("project_root", str(discover_project_root()))
    safe.setdefault("report_root", str(discover_git_report_root()))
    return safe


def render_markdown(payload: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# IKORNS DEV GIT REPORT",
        "",
        "## Cover",
        f"- Report ID: {payload.get('report_id', '-')}",
        f"- Tool: {payload.get('tool', '-')}",
        f"- Service: {payload.get('service', '-')}",
        f"- Generated: {payload.get('generated_at', '-')}",
        "",
        "## Operation",
        f"- Operation: {payload.get('operation', '-')}",
        f"- Status: {payload.get('status', '-')}",
        f"- Success: {payload.get('success', '-')}",
        f"- Message: {payload.get('message', '-')}",
        "",
        "## Data",
    ]

    data = payload.get("data", {}) or {}
    if isinstance(data, dict) and data:
        for key, value in data.items():
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- No data")

    warnings = payload.get("warnings", []) or []
    errors = payload.get("errors", []) or []
    commands = payload.get("commands", []) or []

    if warnings:
        lines.extend(["", "## Warnings"])
        for item in warnings:
            lines.append(f"- {item}")

    if errors:
        lines.extend(["", "## Errors"])
        for item in errors:
            lines.append(f"- {item}")

    if commands:
        lines.extend(["", "## Commands"])
        for command in commands:
            lines.append(f"- {command}")

    return "\n".join(lines)


def render_log(payload: Dict[str, Any]) -> str:
    lines: List[str] = [
        "[IKORNS DEV GIT REPORT]",
        f"REPORT_ID: {payload.get('report_id', '-')}",
        f"OPERATION: {payload.get('operation', '-')}",
        f"STATUS: {payload.get('status', '-')}",
        f"SUCCESS: {payload.get('success', '-')}",
        f"MESSAGE: {payload.get('message', '-')}",
        f"GENERATED: {payload.get('generated_at', '-')}",
        "",
        "DATA",
        json.dumps(payload.get("data", {}), ensure_ascii=False, indent=2),
        "",
        "WARNINGS",
    ]

    for item in payload.get("warnings", []) or []:
        lines.append(f"- {item}")

    lines.append("")
    lines.append("ERRORS")
    for item in payload.get("errors", []) or []:
        lines.append(f"- {item}")

    lines.append("")
    lines.append("COMMANDS")
    for item in payload.get("commands", []) or []:
        lines.append(str(item))

    return "\n".join(lines)


class GitReportService:
    """
    EN:
        Single report service that writes MD/JSON/LOG.

    TH:
        Service เดียวสำหรับเขียนรายงาน MD/JSON/LOG
    """

    def __init__(self, report_root: Optional[str | Path] = None) -> None:
        self.report_root = (
            Path(report_root).expanduser().resolve()
            if report_root
            else discover_git_report_root()
        )

    def build_paths(self, report_id: str) -> Dict[str, Path]:
        return {
            "md": self.report_root / "md" / f"{report_id}.md",
            "json": self.report_root / "json" / f"{report_id}.json",
            "log": self.report_root / "log" / f"{report_id}.log",
        }

    def ensure_folders(self) -> None:
        for folder in ("md", "json", "log"):
            (self.report_root / folder).mkdir(parents=True, exist_ok=True)

    def write_report(self, payload: Dict[str, Any]) -> GitReportResult:
        try:
            self.ensure_folders()

            report_id = str(payload.get("report_id") or build_report_id())
            normalized = normalize_payload(payload)
            normalized["report_id"] = report_id

            paths = self.build_paths(report_id)

            paths["md"].write_text(render_markdown(normalized), encoding=ENCODING)
            paths["json"].write_text(
                json.dumps(normalized, ensure_ascii=False, indent=2),
                encoding=ENCODING,
            )
            paths["log"].write_text(render_log(normalized), encoding=ENCODING)

            return GitReportResult.ok(
                message="Git report exported successfully.",
                report_id=report_id,
                paths={key: str(value) for key, value in paths.items()},
            )

        except Exception as exc:
            return GitReportResult.fail(
                message="Git report export failed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )


def write_git_report(payload: Dict[str, Any]) -> GitReportResult:
    return GitReportService().write_report(payload)


__all__ = [
    "GitReportResult",
    "GitReportService",
    "write_git_report",
]