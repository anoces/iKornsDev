


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
FILE         : GitExecutionService.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Execution Service
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    GitExecutionService is the main orchestration service for iKornsDevGit.
    It executes safe Git commands through subprocess and returns structured
    results for console, report, and registry layers.

TH:
    GitExecutionService คือ service หลักสำหรับควบคุม Git flow ของ iKornsDevGit
    ใช้เรียกคำสั่ง Git แบบปลอดภัยผ่าน subprocess และคืนผลลัพธ์แบบมีโครงสร้าง
    เพื่อให้ Console, Report และ Registry ใช้ต่อได้

POSITION:
    Console -> Module -> GitExecutionService -> Git CLI

THIS FILE MUST:
    - Run git status
    - Stage selected files
    - Stage all files
    - Commit staged files
    - Push current branch
    - Pull latest changes
    - Run publish flow: status -> stage -> commit -> push
    - Use dynamic paths only
    - Return structured result

THIS FILE MUST NOT:
    - Store credentials
    - Hardcode repository path
    - Push without caller confirmation
    - Modify non-git folders directly
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


SERVICE_NAME = "GitExecutionService"
SERVICE_VERSION = "0.0.1"
SERVICE_STATUS = "DEVELOPMENT"

ENV_IPROJECTS_ROOT = "IKORNS_IPROJECTS_ROOT"


@dataclass
class GitCommandResult:
    command: List[str]
    return_code: int
    stdout: str = ""
    stderr: str = ""

    def ok(self) -> bool:
        return self.return_code == 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "command": list(self.command),
            "return_code": self.return_code,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "success": self.ok(),
        }


@dataclass
class GitExecutionResult:
    success: bool
    status: str
    code: str
    message: str
    operation: str = ""
    commands: List[GitCommandResult] = field(default_factory=list)
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
            "commands": [item.to_dict() for item in self.commands],
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
        commands: Optional[List[GitCommandResult]] = None,
        data: Optional[Dict[str, Any]] = None,
        warnings: Optional[List[str]] = None,
    ) -> "GitExecutionResult":
        return cls(
            success=True,
            status="PASS",
            code="GIT_EXECUTION_PASS",
            message=message,
            operation=operation,
            commands=commands or [],
            data=data or {},
            warnings=warnings or [],
        )

    @classmethod
    def fail(
        cls,
        operation: str,
        message: str,
        commands: Optional[List[GitCommandResult]] = None,
        errors: Optional[List[str]] = None,
        warnings: Optional[List[str]] = None,
    ) -> "GitExecutionResult":
        return cls(
            success=False,
            status="FAIL",
            code="GIT_EXECUTION_FAIL",
            message=message,
            operation=operation,
            commands=commands or [],
            errors=errors or [],
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

    return current.parents[5].resolve()


class GitExecutionService:
    """
    EN:
        Main Git execution orchestration service.

    TH:
        Service หลักสำหรับควบคุมคำสั่ง Git
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

    def _run_git(self, args: List[str]) -> GitCommandResult:
        command = ["git"] + list(args)

        completed = subprocess.run(
            command,
            cwd=str(self.repo_root),
            text=True,
            capture_output=True,
            shell=False,
        )

        return GitCommandResult(
            command=command,
            return_code=completed.returncode,
            stdout=completed.stdout.strip(),
            stderr=completed.stderr.strip(),
        )

    def _ensure_git_repo(self) -> Optional[GitExecutionResult]:
        try:
            result = self._run_git(["rev-parse", "--is-inside-work-tree"])
            if not result.ok() or result.stdout.lower() != "true":
                return GitExecutionResult.fail(
                    operation="VALIDATE_REPOSITORY",
                    message="Current root is not a Git repository.",
                    commands=[result],
                    errors=[result.stderr or result.stdout],
                )
            return None
        except Exception as exc:
            return GitExecutionResult.fail(
                operation="VALIDATE_REPOSITORY",
                message="Git repository validation failed.",
                errors=[f"{type(exc).__name__}: {exc}", traceback.format_exc()],
            )

    def status(self) -> GitExecutionResult:
        validation_error = self._ensure_git_repo()
        if validation_error:
            return validation_error

        result = self._run_git(["status", "--short", "--branch"])

        if not result.ok():
            return GitExecutionResult.fail(
                operation="GIT_STATUS",
                message="Git status failed.",
                commands=[result],
                errors=[result.stderr],
            )

        return GitExecutionResult.ok(
            operation="GIT_STATUS",
            message="Git status completed.",
            commands=[result],
            data={
                "service_info": self.get_service_info(),
                "status_text": result.stdout,
            },
        )

    def stage_selected(self, paths: List[str]) -> GitExecutionResult:
        validation_error = self._ensure_git_repo()
        if validation_error:
            return validation_error

        clean_paths = [str(item).strip() for item in paths if str(item).strip()]
        if not clean_paths:
            return GitExecutionResult.fail(
                operation="STAGE_SELECTED",
                message="No paths provided for staging.",
                errors=["paths is empty"],
            )

        command_result = self._run_git(["add"] + clean_paths)

        if not command_result.ok():
            return GitExecutionResult.fail(
                operation="STAGE_SELECTED",
                message="Stage selected files failed.",
                commands=[command_result],
                errors=[command_result.stderr],
            )

        return GitExecutionResult.ok(
            operation="STAGE_SELECTED",
            message="Selected files staged successfully.",
            commands=[command_result],
            data={"staged_paths": clean_paths},
        )

    def stage_all(self) -> GitExecutionResult:
        validation_error = self._ensure_git_repo()
        if validation_error:
            return validation_error

        command_result = self._run_git(["add", "-A"])

        if not command_result.ok():
            return GitExecutionResult.fail(
                operation="STAGE_ALL",
                message="Stage all failed.",
                commands=[command_result],
                errors=[command_result.stderr],
            )

        return GitExecutionResult.ok(
            operation="STAGE_ALL",
            message="All changed files staged successfully.",
            commands=[command_result],
        )

    def commit(self, message: str) -> GitExecutionResult:
        validation_error = self._ensure_git_repo()
        if validation_error:
            return validation_error

        commit_message = str(message or "").strip()
        if not commit_message:
            return GitExecutionResult.fail(
                operation="COMMIT",
                message="Commit message is required.",
                errors=["commit message is empty"],
            )

        command_result = self._run_git(["commit", "-m", commit_message])

        if not command_result.ok():
            return GitExecutionResult.fail(
                operation="COMMIT",
                message="Git commit failed.",
                commands=[command_result],
                errors=[command_result.stderr or command_result.stdout],
            )

        return GitExecutionResult.ok(
            operation="COMMIT",
            message="Git commit completed.",
            commands=[command_result],
            data={"commit_message": commit_message},
        )

    def push(self) -> GitExecutionResult:
        validation_error = self._ensure_git_repo()
        if validation_error:
            return validation_error

        command_result = self._run_git(["push"])

        if not command_result.ok():
            return GitExecutionResult.fail(
                operation="PUSH",
                message="Git push failed.",
                commands=[command_result],
                errors=[command_result.stderr],
            )

        return GitExecutionResult.ok(
            operation="PUSH",
            message="Git push completed.",
            commands=[command_result],
        )

    def pull(self) -> GitExecutionResult:
        validation_error = self._ensure_git_repo()
        if validation_error:
            return validation_error

        command_result = self._run_git(["pull"])

        if not command_result.ok():
            return GitExecutionResult.fail(
                operation="PULL",
                message="Git pull failed.",
                commands=[command_result],
                errors=[command_result.stderr],
            )

        return GitExecutionResult.ok(
            operation="PULL",
            message="Git pull completed.",
            commands=[command_result],
        )

    def publish_flow(
        self,
        commit_message: str,
        stage_all: bool = True,
        selected_paths: Optional[List[str]] = None,
    ) -> GitExecutionResult:
        """
        EN:
            Publish flow follows locked console contract:
            Status -> Stage -> Commit -> Push

        TH:
            Publish flow ยึดตาม contract:
            Status -> Stage -> Commit -> Push
        """

        commands: List[GitCommandResult] = []
        warnings: List[str] = []

        status_result = self.status()
        commands.extend(status_result.commands)

        if not status_result.success:
            return status_result

        if stage_all:
            stage_result = self.stage_all()
        else:
            stage_result = self.stage_selected(selected_paths or [])

        commands.extend(stage_result.commands)

        if not stage_result.success:
            return GitExecutionResult.fail(
                operation="PUBLISH_FLOW",
                message="Publish flow stopped at stage step.",
                commands=commands,
                errors=stage_result.errors,
                warnings=warnings + stage_result.warnings,
            )

        commit_result = self.commit(commit_message)
        commands.extend(commit_result.commands)

        if not commit_result.success:
            return GitExecutionResult.fail(
                operation="PUBLISH_FLOW",
                message="Publish flow stopped at commit step.",
                commands=commands,
                errors=commit_result.errors,
                warnings=warnings + commit_result.warnings,
            )

        push_result = self.push()
        commands.extend(push_result.commands)

        if not push_result.success:
            return GitExecutionResult.fail(
                operation="PUBLISH_FLOW",
                message="Publish flow stopped at push step.",
                commands=commands,
                errors=push_result.errors,
                warnings=warnings + push_result.warnings,
            )

        return GitExecutionResult.ok(
            operation="PUBLISH_FLOW",
            message="Publish flow completed: Status -> Stage -> Commit -> Push.",
            commands=commands,
            data={
                "service_info": self.get_service_info(),
                "commit_message": commit_message,
                "stage_all": stage_all,
                "selected_paths": selected_paths or [],
            },
            warnings=warnings,
        )


__all__ = [
    "GitCommandResult",
    "GitExecutionResult",
    "GitExecutionService",
]