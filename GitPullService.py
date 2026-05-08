


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
FILE         : GitPullService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Pull Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Git pull workflow service for iKornsDevGit.

TH:
    Service สำหรับ workflow การ pull ของ Git ใน iKornsDevGit

POSITION:
    GitExecutionService -> GitPullService -> Git CLI

THIS FILE MUST:
    - validate current branch
    - check upstream branch
    - check working tree warning
    - pull latest changes
    - summarize pull result

THIS FILE MUST NOT:
    - push
    - commit
    - merge manually
    - rebase manually
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


SERVICE_NAME = "GitPullService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitPullResult:
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
    ) -> "GitPullResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_PULL_PASS",
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
    ) -> "GitPullResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_PULL_FAIL",
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


class GitPullService:
    """
    EN:
        Git pull workflow service.

    TH:
        Service สำหรับ Git pull workflow
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
        return (
            result.returncode == 0,
            result.stdout.strip(),
            result.stderr.strip(),
        )

    def current_branch(self) -> GitPullResult:
        ok, stdout, stderr = self._read_git(["branch", "--show-current"])

        if not ok or not stdout:
            return GitPullResult.fail(
                message="Unable to read current branch.",
                errors=[stderr or "empty branch"],
                data={"service_info": self.get_service_info()},
            )

        return GitPullResult.ok(
            message="Current branch detected.",
            data={
                "service_info": self.get_service_info(),
                "branch": stdout,
            },
        )

    def upstream_branch(self) -> GitPullResult:
        ok, stdout, stderr = self._read_git(
            ["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"]
        )

        if not ok:
            return GitPullResult.ok(
                message="No upstream branch configured.",
                warnings=["No upstream branch configured. Pull may fail without remote tracking."],
                data={
                    "service_info": self.get_service_info(),
                    "upstream": "",
                    "stderr": stderr,
                },
            )

        return GitPullResult.ok(
            message="Upstream branch detected.",
            data={
                "service_info": self.get_service_info(),
                "upstream": stdout,
            },
        )

    def working_tree_status(self) -> GitPullResult:
        ok, stdout, stderr = self._read_git(["status", "--short"])

        if not ok:
            return GitPullResult.fail(
                message="Unable to read working tree status.",
                errors=[stderr],
                data={"service_info": self.get_service_info()},
            )

        changed_files: List[str] = [
            line.strip()
            for line in stdout.splitlines()
            if line.strip()
        ]

        warnings: List[str] = []

        if changed_files:
            warnings.append(
                "Working tree has local changes. Pull may create conflicts or require merge resolution."
            )

        return GitPullResult.ok(
            message="Working tree status read.",
            warnings=warnings,
            data={
                "service_info": self.get_service_info(),
                "has_changes": len(changed_files) > 0,
                "changed_count": len(changed_files),
                "changed_files": changed_files,
                "status_text": stdout,
            },
        )

    def fetch(self) -> GitPullResult:
        try:
            result = self._run_git(["fetch"])

            if result.returncode != 0:
                return GitPullResult.fail(
                    message="Git fetch failed.",
                    errors=[result.stderr.strip() or result.stdout.strip()],
                    data={
                        "service_info": self.get_service_info(),
                        "stdout": result.stdout.strip(),
                    },
                )

            return GitPullResult.ok(
                message="Git fetch completed.",
                data={
                    "service_info": self.get_service_info(),
                    "stdout": result.stdout.strip(),
                    "stderr": result.stderr.strip(),
                },
            )

        except Exception as exc:
            return GitPullResult.fail(
                message="Git fetch crashed.",
                errors=[
                    f"{type(exc).__name__}: {exc}",
                    traceback.format_exc(),
                ],
            )

    def pull_current_branch(
        self,
        rebase: bool = False,
    ) -> GitPullResult:
        try:
            branch = self.current_branch()
            upstream = self.upstream_branch()
            tree = self.working_tree_status()

            warnings: List[str] = []
            errors: List[str] = []

            for result in (branch, upstream, tree):
                warnings.extend(result.warnings)
                if not result.success:
                    errors.extend(result.errors)

            if errors:
                return GitPullResult.fail(
                    message="Pull readiness failed.",
                    errors=errors,
                    warnings=warnings,
                    data={
                        "service_info": self.get_service_info(),
                        "branch": branch.to_dict(),
                        "upstream": upstream.to_dict(),
                        "working_tree": tree.to_dict(),
                    },
                )

            args = ["pull"]

            if rebase:
                args.append("--rebase")
                warnings.append("Pull rebase mode enabled.")

            result = self._run_git(args)

            output_text = "\n".join(
                item for item in [result.stdout.strip(), result.stderr.strip()] if item
            )

            conflict_detected = any(
                token in output_text.lower()
                for token in [
                    "conflict",
                    "merge conflict",
                    "automatic merge failed",
                    "fix conflicts",
                ]
            )

            if conflict_detected:
                warnings.append("Possible merge conflict detected in pull output.")

            if result.returncode != 0:
                return GitPullResult.fail(
                    message="Git pull failed.",
                    errors=[result.stderr.strip() or result.stdout.strip()],
                    warnings=warnings,
                    data={
                        "service_info": self.get_service_info(),
                        "branch": branch.data,
                        "upstream": upstream.data,
                        "working_tree": tree.data,
                        "rebase": rebase,
                        "conflict_detected": conflict_detected,
                        "stdout": result.stdout.strip(),
                        "stderr": result.stderr.strip(),
                    },
                )

            return GitPullResult.ok(
                message="Git pull completed.",
                warnings=warnings,
                data={
                    "service_info": self.get_service_info(),
                    "branch": branch.data,
                    "upstream": upstream.data,
                    "working_tree": tree.data,
                    "rebase": rebase,
                    "conflict_detected": conflict_detected,
                    "stdout": result.stdout.strip(),
                    "stderr": result.stderr.strip(),
                },
            )

        except Exception as exc:
            return GitPullResult.fail(
                message="Git pull crashed.",
                errors=[
                    f"{type(exc).__name__}: {exc}",
                    traceback.format_exc(),
                ],
            )

    def overview(self) -> GitPullResult:
        branch = self.current_branch()
        upstream = self.upstream_branch()
        tree = self.working_tree_status()

        warnings: List[str] = []
        errors: List[str] = []

        for result in (branch, upstream, tree):
            warnings.extend(result.warnings)
            if not result.success:
                errors.extend(result.errors)

        if errors:
            return GitPullResult.fail(
                message="Pull overview completed with errors.",
                errors=errors,
                warnings=warnings,
                data={
                    "service_info": self.get_service_info(),
                    "branch": branch.to_dict(),
                    "upstream": upstream.to_dict(),
                    "working_tree": tree.to_dict(),
                },
            )

        return GitPullResult.ok(
            message="Pull overview read.",
            warnings=warnings,
            data={
                "service_info": self.get_service_info(),
                "branch": branch.data,
                "upstream": upstream.data,
                "working_tree": tree.data,
            },
        )


def pull_current_branch(
    repo_root: Optional[str | Path] = None,
    rebase: bool = False,
) -> GitPullResult:
    return GitPullService(
        repo_root=repo_root
    ).pull_current_branch(rebase=rebase)


__all__ = [
    "GitPullResult",
    "GitPullService",
    "pull_current_branch",
]