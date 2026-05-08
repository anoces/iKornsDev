








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
FILE         : GitRepositoryService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Repository Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Read-only repository information service for iKornsDevGit.

TH:
    Service อ่านข้อมูล Git repository เท่านั้น ไม่ execute action ที่เปลี่ยน state

POSITION:
    GitExecutionService / GitValidationService -> GitRepositoryService -> Git CLI

THIS FILE MUST NOT:
    - git add
    - git commit
    - git push
    - git pull
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


SERVICE_NAME = "GitRepositoryService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitRepositoryResult:
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
    ) -> "GitRepositoryResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_REPOSITORY_READ_PASS",
            message=message,
            data=data or {},
            warnings=warnings or [],
        )

    @classmethod
    def fail(
        cls,
        message: str,
        errors: Optional[List[str]] = None,
        warnings: Optional[List[str]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> "GitRepositoryResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_REPOSITORY_READ_FAIL",
            message=message,
            errors=errors or [],
            warnings=warnings or [],
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


class GitRepositoryService:
    """
    EN:
        Read-only Git repository information service.

    TH:
        Service สำหรับอ่านข้อมูล Git repository แบบ read-only
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

    def _read_git_text(self, args: List[str]) -> tuple[bool, str, str]:
        result = self._run_git(args)
        return (
            result.returncode == 0,
            result.stdout.strip(),
            result.stderr.strip(),
        )

    def is_git_repository(self) -> bool:
        ok, stdout, _ = self._read_git_text(["rev-parse", "--is-inside-work-tree"])
        return ok and stdout.lower() == "true"

    def get_repository_root(self) -> GitRepositoryResult:
        try:
            ok, stdout, stderr = self._read_git_text(["rev-parse", "--show-toplevel"])

            if not ok:
                return GitRepositoryResult.fail(
                    message="Unable to read Git repository root.",
                    errors=[stderr or stdout],
                    data={"service_info": self.get_service_info()},
                )

            return GitRepositoryResult.ok(
                message="Git repository root detected.",
                data={
                    "service_info": self.get_service_info(),
                    "repository_root": stdout,
                },
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Git repository root read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_current_branch(self) -> GitRepositoryResult:
        try:
            ok, stdout, stderr = self._read_git_text(["branch", "--show-current"])

            if not ok or not stdout:
                return GitRepositoryResult.fail(
                    message="Unable to read current Git branch.",
                    errors=[stderr or "empty branch"],
                    data={"service_info": self.get_service_info()},
                )

            return GitRepositoryResult.ok(
                message="Current Git branch detected.",
                data={
                    "service_info": self.get_service_info(),
                    "branch": stdout,
                },
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Current branch read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_remote_info(self) -> GitRepositoryResult:
        try:
            ok, stdout, stderr = self._read_git_text(["remote", "-v"])

            if not ok:
                return GitRepositoryResult.fail(
                    message="Unable to read Git remote info.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            remotes: List[Dict[str, str]] = []

            for line in stdout.splitlines():
                parts = line.split()
                if len(parts) >= 3:
                    remotes.append(
                        {
                            "name": parts[0],
                            "url": parts[1],
                            "mode": parts[2].strip("()"),
                        }
                    )

            warnings: List[str] = []
            if not remotes:
                warnings.append("No Git remote configured.")

            return GitRepositoryResult.ok(
                message="Git remote info read.",
                data={
                    "service_info": self.get_service_info(),
                    "remote_text": stdout,
                    "remotes": remotes,
                },
                warnings=warnings,
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Git remote info read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_status_short(self) -> GitRepositoryResult:
        try:
            ok, stdout, stderr = self._read_git_text(["status", "--short", "--branch"])

            if not ok:
                return GitRepositoryResult.fail(
                    message="Unable to read Git status.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            changed_files: List[Dict[str, str]] = []
            branch_line = ""

            for line in stdout.splitlines():
                if line.startswith("##"):
                    branch_line = line
                    continue

                if len(line) >= 3:
                    changed_files.append(
                        {
                            "status_code": line[:2],
                            "path": line[3:].strip(),
                            "raw": line,
                        }
                    )

            return GitRepositoryResult.ok(
                message="Git short status read.",
                data={
                    "service_info": self.get_service_info(),
                    "status_text": stdout,
                    "branch_line": branch_line,
                    "changed_files": changed_files,
                    "changed_count": len(changed_files),
                    "has_changes": len(changed_files) > 0,
                },
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Git status read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_latest_commit(self) -> GitRepositoryResult:
        try:
            ok, stdout, stderr = self._read_git_text(
                ["log", "-1", "--pretty=format:%H%n%h%n%an%n%ae%n%ad%n%s"]
            )

            if not ok:
                return GitRepositoryResult.fail(
                    message="Unable to read latest commit.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            lines = stdout.splitlines()

            data = {
                "full_hash": lines[0] if len(lines) > 0 else "",
                "short_hash": lines[1] if len(lines) > 1 else "",
                "author_name": lines[2] if len(lines) > 2 else "",
                "author_email": lines[3] if len(lines) > 3 else "",
                "date": lines[4] if len(lines) > 4 else "",
                "subject": lines[5] if len(lines) > 5 else "",
            }

            return GitRepositoryResult.ok(
                message="Latest commit read.",
                data={
                    "service_info": self.get_service_info(),
                    "latest_commit": data,
                },
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Latest commit read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_git_user(self) -> GitRepositoryResult:
        try:
            name_ok, name_out, name_err = self._read_git_text(["config", "user.name"])
            email_ok, email_out, email_err = self._read_git_text(["config", "user.email"])

            warnings: List[str] = []

            if not name_ok or not name_out:
                warnings.append("Git user.name is not configured.")

            if not email_ok or not email_out:
                warnings.append("Git user.email is not configured.")

            return GitRepositoryResult.ok(
                message="Git user config read.",
                data={
                    "service_info": self.get_service_info(),
                    "user_name": name_out,
                    "user_email": email_out,
                    "name_error": name_err,
                    "email_error": email_err,
                },
                warnings=warnings,
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Git user config read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_repository_overview(self) -> GitRepositoryResult:
        """
        EN:
            Build one repository overview payload.

        TH:
            รวมข้อมูล repository หลักเป็น payload เดียว
        """

        try:
            warnings: List[str] = []
            errors: List[str] = []

            repo_root = self.get_repository_root()
            branch = self.get_current_branch()
            remote = self.get_remote_info()
            status = self.get_status_short()
            latest_commit = self.get_latest_commit()
            git_user = self.get_git_user()

            for result in (repo_root, branch, remote, status, latest_commit, git_user):
                warnings.extend(result.warnings)
                if not result.success:
                    errors.extend(result.errors)

            if errors:
                return GitRepositoryResult.fail(
                    message="Repository overview completed with errors.",
                    errors=errors,
                    warnings=warnings,
                    data={
                        "service_info": self.get_service_info(),
                        "repository_root": repo_root.to_dict(),
                        "branch": branch.to_dict(),
                        "remote": remote.to_dict(),
                        "status": status.to_dict(),
                        "latest_commit": latest_commit.to_dict(),
                        "git_user": git_user.to_dict(),
                    },
                )

            return GitRepositoryResult.ok(
                message="Repository overview read.",
                data={
                    "service_info": self.get_service_info(),
                    "repository_root": repo_root.data.get("repository_root", ""),
                    "branch": branch.data.get("branch", ""),
                    "remote": remote.data,
                    "status": status.data,
                    "latest_commit": latest_commit.data.get("latest_commit", {}),
                    "git_user": {
                        "user_name": git_user.data.get("user_name", ""),
                        "user_email": git_user.data.get("user_email", ""),
                    },
                },
                warnings=warnings,
            )

        except Exception as exc:
            return GitRepositoryResult.fail(
                message="Repository overview crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )


def get_git_repository_overview(repo_root: Optional[str | Path] = None) -> GitRepositoryResult:
    return GitRepositoryService(repo_root=repo_root).get_repository_overview()


__all__ = [
    "GitRepositoryResult",
    "GitRepositoryService",
    "get_git_repository_overview",
]