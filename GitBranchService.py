


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
FILE         : GitBranchService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Branch Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Read and manage Git branch state for iKornsDevGit.

TH:
    อ่านและจัดการสถานะ branch ของ Git สำหรับ iKornsDevGit

POSITION:
    GitExecutionService -> GitBranchService -> Git CLI

THIS FILE MUST:
    - read current branch
    - list local branches
    - list remote branches
    - read upstream branch
    - checkout branch
    - create branch
    - delete local branch safely

THIS FILE MUST NOT:
    - push
    - pull
    - commit
    - stage
    - merge/rebase
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


SERVICE_NAME = "GitBranchService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitBranchResult:
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
    def ok(cls, message: str, data: Optional[Dict[str, Any]] = None, warnings: Optional[List[str]] = None) -> "GitBranchResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_BRANCH_PASS",
            message=message,
            data=data or {},
            warnings=warnings or [],
        )

    @classmethod
    def fail(cls, message: str, errors: Optional[List[str]] = None, data: Optional[Dict[str, Any]] = None) -> "GitBranchResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_BRANCH_FAIL",
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


class GitBranchService:
    """
    EN:
        Branch-focused Git service.

    TH:
        Service สำหรับจัดการ branch โดยเฉพาะ
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

    def current_branch(self) -> GitBranchResult:
        try:
            ok, stdout, stderr = self._read_git(["branch", "--show-current"])

            if not ok or not stdout:
                return GitBranchResult.fail(
                    message="Unable to read current branch.",
                    errors=[stderr or "empty branch"],
                    data={"service_info": self.get_service_info()},
                )

            return GitBranchResult.ok(
                message="Current branch detected.",
                data={
                    "service_info": self.get_service_info(),
                    "branch": stdout,
                },
            )

        except Exception as exc:
            return GitBranchResult.fail(
                message="Current branch read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def list_local_branches(self) -> GitBranchResult:
        try:
            ok, stdout, stderr = self._read_git(["branch", "--list"])

            if not ok:
                return GitBranchResult.fail(
                    message="Unable to list local branches.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            branches: List[Dict[str, Any]] = []
            for line in stdout.splitlines():
                raw = line.rstrip()
                is_current = raw.startswith("*")
                name = raw.replace("*", "", 1).strip()
                if name:
                    branches.append({"name": name, "current": is_current})

            return GitBranchResult.ok(
                message="Local branches listed.",
                data={
                    "service_info": self.get_service_info(),
                    "branches": branches,
                    "count": len(branches),
                },
            )

        except Exception as exc:
            return GitBranchResult.fail(
                message="Local branch list crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def list_remote_branches(self) -> GitBranchResult:
        try:
            ok, stdout, stderr = self._read_git(["branch", "-r"])

            if not ok:
                return GitBranchResult.fail(
                    message="Unable to list remote branches.",
                    errors=[stderr],
                    data={"service_info": self.get_service_info()},
                )

            branches = [
                line.strip()
                for line in stdout.splitlines()
                if line.strip() and "->" not in line
            ]

            return GitBranchResult.ok(
                message="Remote branches listed.",
                data={
                    "service_info": self.get_service_info(),
                    "remote_branches": branches,
                    "count": len(branches),
                },
            )

        except Exception as exc:
            return GitBranchResult.fail(
                message="Remote branch list crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def upstream_branch(self) -> GitBranchResult:
        try:
            ok, stdout, stderr = self._read_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"])

            if not ok:
                return GitBranchResult.ok(
                    message="No upstream branch configured.",
                    warnings=["No upstream branch configured for current branch."],
                    data={
                        "service_info": self.get_service_info(),
                        "upstream": "",
                        "stderr": stderr,
                    },
                )

            return GitBranchResult.ok(
                message="Upstream branch detected.",
                data={
                    "service_info": self.get_service_info(),
                    "upstream": stdout,
                },
            )

        except Exception as exc:
            return GitBranchResult.fail(
                message="Upstream branch read crashed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def checkout_branch(self, branch_name: str) -> GitBranchResult:
        clean_name = str(branch_name or "").strip()

        if not clean_name:
            return GitBranchResult.fail(
                message="Branch name is required.",
                errors=["branch_name is empty"],
                data={"service_info": self.get_service_info()},
            )

        result = self._run_git(["checkout", clean_name])

        if result.returncode != 0:
            return GitBranchResult.fail(
                message="Branch checkout failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={
                    "service_info": self.get_service_info(),
                    "branch": clean_name,
                },
            )

        return GitBranchResult.ok(
            message="Branch checkout completed.",
            data={
                "service_info": self.get_service_info(),
                "branch": clean_name,
                "stdout": result.stdout.strip(),
            },
        )

    def create_branch(self, branch_name: str, checkout: bool = False) -> GitBranchResult:
        clean_name = str(branch_name or "").strip()

        if not clean_name:
            return GitBranchResult.fail(
                message="Branch name is required.",
                errors=["branch_name is empty"],
                data={"service_info": self.get_service_info()},
            )

        args = ["checkout", "-b", clean_name] if checkout else ["branch", clean_name]
        result = self._run_git(args)

        if result.returncode != 0:
            return GitBranchResult.fail(
                message="Branch creation failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={
                    "service_info": self.get_service_info(),
                    "branch": clean_name,
                    "checkout": checkout,
                },
            )

        return GitBranchResult.ok(
            message="Branch created.",
            data={
                "service_info": self.get_service_info(),
                "branch": clean_name,
                "checkout": checkout,
                "stdout": result.stdout.strip(),
            },
        )

    def delete_local_branch(self, branch_name: str, force: bool = False) -> GitBranchResult:
        clean_name = str(branch_name or "").strip()

        if not clean_name:
            return GitBranchResult.fail(
                message="Branch name is required.",
                errors=["branch_name is empty"],
                data={"service_info": self.get_service_info()},
            )

        current = self.current_branch()
        if current.success and current.data.get("branch") == clean_name:
            return GitBranchResult.fail(
                message="Cannot delete the current active branch.",
                errors=["active branch deletion blocked"],
                data={
                    "service_info": self.get_service_info(),
                    "branch": clean_name,
                },
            )

        flag = "-D" if force else "-d"
        result = self._run_git(["branch", flag, clean_name])

        if result.returncode != 0:
            return GitBranchResult.fail(
                message="Branch deletion failed.",
                errors=[result.stderr.strip() or result.stdout.strip()],
                data={
                    "service_info": self.get_service_info(),
                    "branch": clean_name,
                    "force": force,
                },
            )

        return GitBranchResult.ok(
            message="Local branch deleted.",
            data={
                "service_info": self.get_service_info(),
                "branch": clean_name,
                "force": force,
                "stdout": result.stdout.strip(),
            },
        )


def get_current_git_branch(repo_root: Optional[str | Path] = None) -> GitBranchResult:
    return GitBranchService(repo_root=repo_root).current_branch()


__all__ = [
    "GitBranchResult",
    "GitBranchService",
    "get_current_git_branch",
]