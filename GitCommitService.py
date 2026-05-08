


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
FILE         : GitCommitService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Commit Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Handles local Git commit workflow only: stage, unstage, staged files,
    commit, and commit history.

TH:
    ดูแล workflow ฝั่ง local commit เท่านั้น เช่น stage, unstage,
    staged files, commit และ commit history

POSITION:
    GitExecutionService -> GitCommitService -> Git CLI

THIS FILE MUST NOT:
    - push
    - pull
    - merge
    - rebase
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


SERVICE_NAME = "GitCommitService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitCommitResult:
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
    ) -> "GitCommitResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_COMMIT_PASS",
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
        warnings: Optional[List[str]] = None,
    ) -> "GitCommitResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_COMMIT_FAIL",
            message=message,
            errors=errors or [],
            data=data or {},
            warnings=warnings or [],
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


class GitCommitService:
    """
    EN:
        Local Git commit workflow service.

    TH:
        Service สำหรับ local Git commit workflow
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

    def _clean_paths(self, paths: List[str]) -> List[str]:
        return [
            str(item).strip().strip('"').strip("'")
            for item in paths
            if str(item).strip()
        ]

    def stage_selected(self, paths: List[str]) -> GitCommitResult:
        clean_paths = self._clean_paths(paths)

        if not clean_paths:
            return GitCommitResult.fail(
                message="No selected paths provided for staging.",
                errors=["paths is empty"],
                data={"service_info": self.get_service_info()},
            )

        result = self._run_git(["add"] + clean_paths)

        if result.returncode != 0:
            return GitCommitResult.fail(
                message="Stage selected files failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={
                    "service_info": self.get_service_info(),
                    "paths": clean_paths,
                },
            )

        return GitCommitResult.ok(
            message="Selected files staged.",
            data={
                "service_info": self.get_service_info(),
                "paths": clean_paths,
                "stdout": result.stdout.strip(),
            },
        )

    def stage_all(self) -> GitCommitResult:
        result = self._run_git(["add", "-A"])

        if result.returncode != 0:
            return GitCommitResult.fail(
                message="Stage all files failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={"service_info": self.get_service_info()},
            )

        return GitCommitResult.ok(
            message="All changed files staged.",
            data={
                "service_info": self.get_service_info(),
                "stdout": result.stdout.strip(),
            },
        )

    def unstage_selected(self, paths: List[str]) -> GitCommitResult:
        clean_paths = self._clean_paths(paths)

        if not clean_paths:
            return GitCommitResult.fail(
                message="No selected paths provided for unstaging.",
                errors=["paths is empty"],
                data={"service_info": self.get_service_info()},
            )

        result = self._run_git(["restore", "--staged"] + clean_paths)

        if result.returncode != 0:
            return GitCommitResult.fail(
                message="Unstage selected files failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={
                    "service_info": self.get_service_info(),
                    "paths": clean_paths,
                },
            )

        return GitCommitResult.ok(
            message="Selected files unstaged.",
            data={
                "service_info": self.get_service_info(),
                "paths": clean_paths,
                "stdout": result.stdout.strip(),
            },
        )

    def unstage_all(self) -> GitCommitResult:
        result = self._run_git(["restore", "--staged", "."])

        if result.returncode != 0:
            return GitCommitResult.fail(
                message="Unstage all files failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={"service_info": self.get_service_info()},
            )

        return GitCommitResult.ok(
            message="All staged files unstaged.",
            data={
                "service_info": self.get_service_info(),
                "stdout": result.stdout.strip(),
            },
        )

    def get_staged_files(self) -> GitCommitResult:
        try:
            result = self._run_git(["diff", "--cached", "--name-status"])

            if result.returncode != 0:
                return GitCommitResult.fail(
                    message="Unable to read staged files.",
                    errors=[result.stderr.strip()],
                    data={"service_info": self.get_service_info()},
                )

            staged_files: List[Dict[str, str]] = []

            for line in result.stdout.splitlines():
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    staged_files.append(
                        {
                            "status": parts[0],
                            "path": parts[1],
                            "raw": line,
                        }
                    )

            return GitCommitResult.ok(
                message="Staged files read.",
                data={
                    "service_info": self.get_service_info(),
                    "staged_files": staged_files,
                    "staged_count": len(staged_files),
                    "has_staged_files": len(staged_files) > 0,
                },
            )

        except Exception as exc:
            return GitCommitResult.fail(
                message="Reading staged files crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def commit(self, message: str) -> GitCommitResult:
        clean_message = str(message or "").strip()

        if not clean_message:
            return GitCommitResult.fail(
                message="Commit message is required.",
                errors=["commit message is empty"],
                data={"service_info": self.get_service_info()},
            )

        staged = self.get_staged_files()
        if staged.success and not staged.data.get("has_staged_files", False):
            return GitCommitResult.fail(
                message="No staged files available for commit.",
                errors=["staged file list is empty"],
                data={
                    "service_info": self.get_service_info(),
                    "staged": staged.to_dict(),
                },
            )

        result = self._run_git(["commit", "-m", clean_message])

        if result.returncode != 0:
            return GitCommitResult.fail(
                message="Git commit failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={
                    "service_info": self.get_service_info(),
                    "commit_message": clean_message,
                    "staged": staged.to_dict(),
                },
            )

        latest = self.get_latest_commit()

        return GitCommitResult.ok(
            message="Git commit completed.",
            data={
                "service_info": self.get_service_info(),
                "commit_message": clean_message,
                "stdout": result.stdout.strip(),
                "latest_commit": latest.data.get("latest_commit", {}),
            },
        )

    def get_latest_commit(self) -> GitCommitResult:
        try:
            result = self._run_git(
                ["log", "-1", "--pretty=format:%H%n%h%n%an%n%ae%n%ad%n%s"]
            )

            if result.returncode != 0:
                return GitCommitResult.fail(
                    message="Unable to read latest commit.",
                    errors=[result.stderr.strip()],
                    data={"service_info": self.get_service_info()},
                )

            lines = result.stdout.splitlines()

            latest_commit = {
                "full_hash": lines[0] if len(lines) > 0 else "",
                "short_hash": lines[1] if len(lines) > 1 else "",
                "author_name": lines[2] if len(lines) > 2 else "",
                "author_email": lines[3] if len(lines) > 3 else "",
                "date": lines[4] if len(lines) > 4 else "",
                "subject": lines[5] if len(lines) > 5 else "",
            }

            return GitCommitResult.ok(
                message="Latest commit read.",
                data={
                    "service_info": self.get_service_info(),
                    "latest_commit": latest_commit,
                },
            )

        except Exception as exc:
            return GitCommitResult.fail(
                message="Latest commit read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def get_commit_history(self, limit: int = 10) -> GitCommitResult:
        safe_limit = max(1, min(int(limit or 10), 100))

        try:
            result = self._run_git(
                [
                    "log",
                    f"-{safe_limit}",
                    "--pretty=format:%H%x1f%h%x1f%an%x1f%ae%x1f%ad%x1f%s",
                ]
            )

            if result.returncode != 0:
                return GitCommitResult.fail(
                    message="Unable to read commit history.",
                    errors=[result.stderr.strip()],
                    data={"service_info": self.get_service_info()},
                )

            commits: List[Dict[str, str]] = []

            for line in result.stdout.splitlines():
                parts = line.split("\x1f")
                if len(parts) >= 6:
                    commits.append(
                        {
                            "full_hash": parts[0],
                            "short_hash": parts[1],
                            "author_name": parts[2],
                            "author_email": parts[3],
                            "date": parts[4],
                            "subject": parts[5],
                        }
                    )

            return GitCommitResult.ok(
                message="Commit history read.",
                data={
                    "service_info": self.get_service_info(),
                    "limit": safe_limit,
                    "commits": commits,
                    "count": len(commits),
                },
            )

        except Exception as exc:
            return GitCommitResult.fail(
                message="Commit history read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )


def commit_staged_files(
    message: str,
    repo_root: Optional[str | Path] = None,
) -> GitCommitResult:
    return GitCommitService(repo_root=repo_root).commit(message)


__all__ = [
    "GitCommitResult",
    "GitCommitService",
    "commit_staged_files",
]