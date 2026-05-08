


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
FILE         : GitValidationService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Validation Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Validates Git environment, repository state, branch, remote, paths,
    commit message, and publish-flow readiness.

TH:
    ตรวจสอบ Git environment, repository, branch, remote, paths,
    commit message และความพร้อมก่อน publish flow

POSITION:
    Console -> Module -> GitExecutionService -> GitValidationService -> Git CLI

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
import shutil
import subprocess
import traceback


SERVICE_NAME = "GitValidationService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitValidationIssue:
    level: str
    code: str
    message: str
    detail: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "level": self.level,
            "code": self.code,
            "message": self.message,
            "detail": dict(self.detail),
        }


@dataclass
class GitValidationResult:
    success: bool
    status: str
    code: str
    message: str
    issues: List[GitValidationIssue] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    data: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "status": self.status,
            "code": self.code,
            "message": self.message,
            "issues": [issue.to_dict() for issue in self.issues],
            "warnings": list(self.warnings),
            "errors": list(self.errors),
            "data": dict(self.data),
            "created_at": self.created_at,
        }

    @classmethod
    def ok(
        cls,
        message: str,
        issues: Optional[List[GitValidationIssue]] = None,
        warnings: Optional[List[str]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> "GitValidationResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_VALIDATION_PASS",
            message=message,
            issues=issues or [],
            warnings=warnings or [],
            data=data or {},
        )

    @classmethod
    def fail(
        cls,
        message: str,
        issues: Optional[List[GitValidationIssue]] = None,
        errors: Optional[List[str]] = None,
        warnings: Optional[List[str]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> "GitValidationResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_VALIDATION_FAIL",
            message=message,
            issues=issues or [],
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


class GitValidationService:
    """
    EN:
        Central Git validation service.

    TH:
        Service กลางสำหรับตรวจความพร้อมของ Git
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

    def _issue(
        self,
        level: str,
        code: str,
        message: str,
        detail: Optional[Dict[str, Any]] = None,
    ) -> GitValidationIssue:
        return GitValidationIssue(
            level=level,
            code=code,
            message=message,
            detail=detail or {},
        )

    def validate_git_installed(self) -> GitValidationResult:
        issues: List[GitValidationIssue] = []

        if shutil.which("git") is None:
            issues.append(
                self._issue(
                    "ERROR",
                    "GIT_NOT_INSTALLED",
                    "Git executable was not found in PATH.",
                )
            )
            return GitValidationResult.fail(
                message="Git is not installed or not available in PATH.",
                issues=issues,
                errors=["git executable not found"],
                data={"service_info": self.get_service_info()},
            )

        return GitValidationResult.ok(
            message="Git executable is available.",
            data={"service_info": self.get_service_info()},
        )

    def validate_repository(self) -> GitValidationResult:
        issues: List[GitValidationIssue] = []

        git_check = self.validate_git_installed()
        if not git_check.success:
            return git_check

        try:
            result = self._run_git(["rev-parse", "--is-inside-work-tree"])
            is_repo = result.returncode == 0 and result.stdout.strip().lower() == "true"

            if not is_repo:
                issues.append(
                    self._issue(
                        "ERROR",
                        "NOT_GIT_REPOSITORY",
                        "Current root is not inside a Git work tree.",
                        {"repo_root": str(self.repo_root), "stderr": result.stderr.strip()},
                    )
                )
                return GitValidationResult.fail(
                    message="Repository validation failed.",
                    issues=issues,
                    errors=["not a git repository"],
                    data={"service_info": self.get_service_info()},
                )

            return GitValidationResult.ok(
                message="Repository validation passed.",
                data={"service_info": self.get_service_info()},
            )

        except Exception as exc:
            return GitValidationResult.fail(
                message="Repository validation crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
                data={"service_info": self.get_service_info()},
            )

    def get_current_branch(self) -> GitValidationResult:
        repo_check = self.validate_repository()
        if not repo_check.success:
            return repo_check

        result = self._run_git(["branch", "--show-current"])
        branch = result.stdout.strip()

        if result.returncode != 0 or not branch:
            return GitValidationResult.fail(
                message="Unable to determine current branch.",
                errors=[result.stderr.strip() or "empty branch name"],
                data={"service_info": self.get_service_info()},
            )

        return GitValidationResult.ok(
            message="Current branch detected.",
            data={
                "service_info": self.get_service_info(),
                "branch": branch,
            },
        )

    def validate_remote(self) -> GitValidationResult:
        repo_check = self.validate_repository()
        if not repo_check.success:
            return repo_check

        result = self._run_git(["remote", "-v"])
        remote_text = result.stdout.strip()

        if result.returncode != 0 or not remote_text:
            return GitValidationResult.fail(
                message="Git remote is not configured.",
                errors=[result.stderr.strip() or "remote is empty"],
                data={"service_info": self.get_service_info()},
            )

        return GitValidationResult.ok(
            message="Git remote validation passed.",
            data={
                "service_info": self.get_service_info(),
                "remote": remote_text,
            },
        )

    def validate_commit_message(self, message: str) -> GitValidationResult:
        clean_message = str(message or "").strip()

        if not clean_message:
            return GitValidationResult.fail(
                message="Commit message is required.",
                errors=["commit message is empty"],
                data={"service_info": self.get_service_info()},
            )

        warnings: List[str] = []
        if len(clean_message) < 8:
            warnings.append("Commit message is short. Consider writing a clearer message.")

        return GitValidationResult.ok(
            message="Commit message validation passed.",
            warnings=warnings,
            data={
                "service_info": self.get_service_info(),
                "commit_message": clean_message,
                "length": len(clean_message),
            },
        )

    def validate_stage_paths(self, paths: List[str]) -> GitValidationResult:
        repo_check = self.validate_repository()
        if not repo_check.success:
            return repo_check

        clean_paths = [str(path).strip().strip('"').strip("'") for path in paths if str(path).strip()]
        issues: List[GitValidationIssue] = []
        warnings: List[str] = []

        if not clean_paths:
            return GitValidationResult.fail(
                message="No paths provided for stage selected.",
                errors=["stage paths are empty"],
                data={"service_info": self.get_service_info()},
            )

        for raw_path in clean_paths:
            candidate = Path(raw_path)
            resolved = candidate if candidate.is_absolute() else self.repo_root / candidate
            resolved = resolved.resolve()

            try:
                resolved.relative_to(self.repo_root)
            except Exception:
                issues.append(
                    self._issue(
                        "ERROR",
                        "STAGE_PATH_OUTSIDE_REPO",
                        "Stage path is outside repository root.",
                        {"path": str(resolved)},
                    )
                )
                continue

            if not resolved.exists():
                warnings.append(f"Stage path does not exist yet, Git may treat it as deleted or invalid: {resolved}")

        errors = [issue.message for issue in issues if issue.level == "ERROR"]
        if errors:
            return GitValidationResult.fail(
                message="Stage path validation failed.",
                issues=issues,
                errors=errors,
                warnings=warnings,
                data={"service_info": self.get_service_info(), "paths": clean_paths},
            )

        return GitValidationResult.ok(
            message="Stage path validation passed.",
            issues=issues,
            warnings=warnings,
            data={"service_info": self.get_service_info(), "paths": clean_paths},
        )

    def validate_publish_readiness(
        self,
        commit_message: str,
        require_remote: bool = True,
    ) -> GitValidationResult:
        issues: List[GitValidationIssue] = []
        warnings: List[str] = []
        errors: List[str] = []

        repo_check = self.validate_repository()
        if not repo_check.success:
            return repo_check

        branch_check = self.get_current_branch()
        if not branch_check.success:
            return branch_check

        message_check = self.validate_commit_message(commit_message)
        if not message_check.success:
            return message_check
        warnings.extend(message_check.warnings)

        remote_data: Dict[str, Any] = {}
        if require_remote:
            remote_check = self.validate_remote()
            if not remote_check.success:
                return remote_check
            remote_data = remote_check.data

        status_result = self._run_git(["status", "--short"])
        status_text = status_result.stdout.strip()

        if status_result.returncode != 0:
            return GitValidationResult.fail(
                message="Unable to read Git status for publish readiness.",
                errors=[status_result.stderr.strip()],
                data={"service_info": self.get_service_info()},
            )

        if not status_text:
            warnings.append("Working tree has no changes. Commit step may have nothing to commit.")

        return GitValidationResult.ok(
            message="Publish readiness validation passed.",
            issues=issues,
            warnings=warnings,
            data={
                "service_info": self.get_service_info(),
                "branch": branch_check.data.get("branch", ""),
                "remote": remote_data.get("remote", ""),
                "has_changes": bool(status_text),
                "status_text": status_text,
            },
        )


def validate_git_repository(repo_root: Optional[str | Path] = None) -> GitValidationResult:
    return GitValidationService(repo_root=repo_root).validate_repository()


__all__ = [
    "GitValidationIssue",
    "GitValidationResult",
    "GitValidationService",
    "validate_git_repository",
]