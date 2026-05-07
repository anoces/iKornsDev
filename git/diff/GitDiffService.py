


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
FILE         : GitDiffService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Diff Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Read-only Git diff service for iKornsDevGit.

TH:
    Service อ่าน diff ของ Git แบบ read-only สำหรับ iKornsDevGit

POSITION:
    GitExecutionService -> GitDiffService -> Git CLI

THIS FILE MUST:
    - read changed files
    - read staged diff
    - read unstaged diff
    - read file-level diff
    - summarize diff stats

THIS FILE MUST NOT:
    - stage files
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
import os
import subprocess
import traceback


SERVICE_NAME = "GitDiffService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitDiffResult:
    success: bool
    status: str
    code: str
    message: str
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
            "data": dict(self.data),
            "warnings": list(self.warnings),
            "errors": list(self.errors),
            "created_at": self.created_at,
        }

    @classmethod
    def ok(
        cls,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        warnings: Optional[List[str]] = None,
    ) -> "GitDiffResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_DIFF_PASS",
            message=message,
            data=data or {},
            warnings=warnings or [],
        )

    @classmethod
    def fail(
        cls,
        message: str,
        errors: Optional[List[str]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> "GitDiffResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_DIFF_FAIL",
            message=message,
            errors=errors or [],
            data=data or {},
        )


def discover_project_root() -> Path:
    env_root = os.environ.get(ENV_IPROJECTS_ROOT)
    if env_root:
        return Path(env_root).expanduser().resolve()

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").exists():
            return parent.resolve()
        if (parent / "iKorns" / "iKornsDev").exists():
            return parent.resolve()

    return current.parents[6].resolve()


class GitDiffService:
    """
    EN:
        Read-only Git diff service.

    TH:
        Service อ่าน Git diff เท่านั้น
    """

    def __init__(self, repo_root: Optional[str | Path] = None) -> None:
        self.repo_root = (
            Path(repo_root).expanduser().resolve()
            if repo_root
            else discover_project_root()
        )

    def get_service_info(self) -> Dict[str, Any]:
        return {
            "service": SERVICE_NAME,
            "version": SERVICE_VERSION,
            "status": SERVICE_STATUS,
            "repo_root": str(self.repo_root),
        }

    def _run_git(self, args: List[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git"] + list(args),
            cwd=str(self.repo_root),
            text=True,
            capture_output=True,
            shell=False,
        )

    def _read_git(self, args: List[str]) -> tuple[bool, str, str]:
        result = self._run_git(args)
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()

    def changed_files(self) -> GitDiffResult:
        try:
            ok, stdout, stderr = self._read_git(["status", "--short"])

            if not ok:
                return GitDiffResult.fail(
                    message="Unable to read changed files.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            files: List[Dict[str, str]] = []

            for line in stdout.splitlines():
                if len(line) >= 3:
                    files.append(
                        {
                            "status_code": line[:2],
                            "path": line[3:].strip(),
                            "raw": line,
                        }
                    )

            return GitDiffResult.ok(
                message="Changed files read.",
                data={
                    "service_info": self.get_service_info(),
                    "changed_files": files,
                    "changed_count": len(files),
                    "has_changes": len(files) > 0,
                    "status_text": stdout,
                },
            )

        except Exception as exc:
            return GitDiffResult.fail(
                message="Changed files read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def staged_files(self) -> GitDiffResult:
        try:
            ok, stdout, stderr = self._read_git(["diff", "--cached", "--name-status"])

            if not ok:
                return GitDiffResult.fail(
                    message="Unable to read staged files.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            files: List[Dict[str, str]] = []

            for line in stdout.splitlines():
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    files.append(
                        {
                            "status": parts[0],
                            "path": parts[1],
                            "raw": line,
                        }
                    )

            return GitDiffResult.ok(
                message="Staged files read.",
                data={
                    "service_info": self.get_service_info(),
                    "staged_files": files,
                    "staged_count": len(files),
                    "has_staged_files": len(files) > 0,
                },
            )

        except Exception as exc:
            return GitDiffResult.fail(
                message="Staged files read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def unstaged_files(self) -> GitDiffResult:
        try:
            ok, stdout, stderr = self._read_git(["diff", "--name-status"])

            if not ok:
                return GitDiffResult.fail(
                    message="Unable to read unstaged files.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            files: List[Dict[str, str]] = []

            for line in stdout.splitlines():
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    files.append(
                        {
                            "status": parts[0],
                            "path": parts[1],
                            "raw": line,
                        }
                    )

            return GitDiffResult.ok(
                message="Unstaged files read.",
                data={
                    "service_info": self.get_service_info(),
                    "unstaged_files": files,
                    "unstaged_count": len(files),
                    "has_unstaged_files": len(files) > 0,
                },
            )

        except Exception as exc:
            return GitDiffResult.fail(
                message="Unstaged files read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def diff_stat(self, staged: bool = False) -> GitDiffResult:
        try:
            args = ["diff", "--stat"]
            if staged:
                args = ["diff", "--cached", "--stat"]

            ok, stdout, stderr = self._read_git(args)

            if not ok:
                return GitDiffResult.fail(
                    message="Unable to read diff stat.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info(), "staged": staged},
                )

            return GitDiffResult.ok(
                message="Diff stat read.",
                data={
                    "service_info": self.get_service_info(),
                    "staged": staged,
                    "stat_text": stdout,
                    "has_diff": bool(stdout),
                },
            )

        except Exception as exc:
            return GitDiffResult.fail(
                message="Diff stat read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def raw_diff(self, staged: bool = False, max_chars: int = 20000) -> GitDiffResult:
        try:
            args = ["diff"]
            if staged:
                args = ["diff", "--cached"]

            ok, stdout, stderr = self._read_git(args)

            if not ok:
                return GitDiffResult.fail(
                    message="Unable to read raw diff.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info(), "staged": staged},
                )

            text = stdout
            truncated = False

            if len(text) > max_chars:
                text = text[:max_chars]
                truncated = True

            return GitDiffResult.ok(
                message="Raw diff read.",
                data={
                    "service_info": self.get_service_info(),
                    "staged": staged,
                    "diff_text": text,
                    "truncated": truncated,
                    "original_length": len(stdout),
                    "max_chars": max_chars,
                },
            )

        except Exception as exc:
            return GitDiffResult.fail(
                message="Raw diff read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def file_diff(self, file_path: str, staged: bool = False, max_chars: int = 20000) -> GitDiffResult:
        clean_path = str(file_path or "").strip().strip('"').strip("'")

        if not clean_path:
            return GitDiffResult.fail(
                message="file_path is required.",
                errors=["file_path is empty"],
                data={"service_info": self.get_service_info()},
            )

        try:
            args = ["diff", "--", clean_path]
            if staged:
                args = ["diff", "--cached", "--", clean_path]

            ok, stdout, stderr = self._read_git(args)

            if not ok:
                return GitDiffResult.fail(
                    message="Unable to read file diff.",
                    errors=[stderr],
                    data={
                        "service_info": self.get_service_info(),
                        "file_path": clean_path,
                        "staged": staged,
                    },
                )

            text = stdout
            truncated = False

            if len(text) > max_chars:
                text = text[:max_chars]
                truncated = True

            return GitDiffResult.ok(
                message="File diff read.",
                data={
                    "service_info": self.get_service_info(),
                    "file_path": clean_path,
                    "staged": staged,
                    "diff_text": text,
                    "truncated": truncated,
                    "original_length": len(stdout),
                    "max_chars": max_chars,
                },
            )

        except Exception as exc:
            return GitDiffResult.fail(
                message="File diff read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def overview(self) -> GitDiffResult:
        changed = self.changed_files()
        staged = self.staged_files()
        unstaged = self.unstaged_files()
        stat = self.diff_stat(staged=False)
        cached_stat = self.diff_stat(staged=True)

        errors: List[str] = []
        warnings: List[str] = []

        for result in (changed, staged, unstaged, stat, cached_stat):
            warnings.extend(result.warnings)
            if not result.success:
                errors.extend(result.errors)

        if errors:
            return GitDiffResult.fail(
                message="Git diff overview completed with errors.",
                errors=errors,
                data={
                    "service_info": self.get_service_info(),
                    "changed": changed.to_dict(),
                    "staged": staged.to_dict(),
                    "unstaged": unstaged.to_dict(),
                    "stat": stat.to_dict(),
                    "cached_stat": cached_stat.to_dict(),
                },
            )

        return GitDiffResult.ok(
            message="Git diff overview read.",
            warnings=warnings,
            data={
                "service_info": self.get_service_info(),
                "changed": changed.data,
                "staged": staged.data,
                "unstaged": unstaged.data,
                "stat": stat.data,
                "cached_stat": cached_stat.data,
            },
        )


def get_git_diff_overview(repo_root: Optional[str | Path] = None) -> GitDiffResult:
    return GitDiffService(repo_root=repo_root).overview()


__all__ = [
    "GitDiffResult",
    "GitDiffService",
    "get_git_diff_overview",
]