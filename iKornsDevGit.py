





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
FILE         : iKornsDevGit.py
LANGUAGE     : PYTHON
SYSTEM       : iKornsDev
MODULE       : Git Console
VERSION      : 0.0.1
STATUS       : DEVELOPMENT
===============================================================================

EN:
    Console entry point for iKornsDevGit.

TH:
    หน้า Console หลักของ iKornsDevGit

LOCKED MENU:
    [1] GIT STATUS
    [2] STAGE SELECTED
    [3] STAGE ALL
    [4] COMMIT
    [5] PUSH
    [6] PULL
    [7] PUBLISH FLOW
    [0] EXIT
===============================================================================
"""

from __future__ import annotations

import json
import os
import secrets
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"

for candidate in (PROJECT_ROOT, SRC_ROOT):
    candidate_text = str(candidate)
    if candidate_text not in sys.path:
        sys.path.insert(0, candidate_text)

from services.ConsoleBuilderService import ConsoleBuilderService  # noqa: E402


try:
    from services.git.GitExecutionService import GitExecutionService
    from services.git.reports.GitReportService import GitReportService
except Exception:
    GitExecutionService = None
    GitReportService = None


LINE = "=" * 53
REPORT_ROOT = PROJECT_ROOT / "sources" / "reports" / "git"
HISTORY_PATH = REPORT_ROOT / "history" / "history.json"
CONSOLE_BUILDER = ConsoleBuilderService()


def _normalize_runtime_path(path_value: Any) -> Path:
    raw_text = str(path_value or "").strip()
    if not raw_text:
        return Path()
    return Path(os.path.normpath(os.path.normcase(str(Path(raw_text).resolve()))))


def _is_within_normalized_root(candidate: Any, root: Any) -> bool:
    candidate_path = _normalize_runtime_path(candidate)
    root_path = _normalize_runtime_path(root)
    if not str(candidate_path) or not str(root_path):
        return False
    try:
        candidate_path.relative_to(root_path)
        return True
    except ValueError:
        return candidate_path == root_path


def _runtime_data() -> Dict[str, str]:
    return CONSOLE_BUILDER.build_runtime_data(
        dev_name="iKornsDevGit",
        module_path="src/modules/git/iKornsDevGitModule.py",
        service_path="src/services/git/GitExecutionService.py",
        script_path="scripts/iKornsDevGit.py",
        version="0.0.1",
        notice="Developer Git Control Tool Only.",
        report_path="sources/reports/git/",
        library_path="src/library/console/LibraryConsole.json",
        runtime_mode="GIT",
        scan_engine="GIT_EXECUTION",
        report_export="MD/JSON/LOG",
        json_support="YES",
        log_support="YES",
        project_root=str(PROJECT_ROOT),
    )


def _ensure_report_folders() -> None:
    for folder in ("md", "json", "log", "history"):
        (REPORT_ROOT / folder).mkdir(parents=True, exist_ok=True)


def _operation_id() -> str:
    now = datetime.now()
    random_part = "".join(
        secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(6)
    )
    return f"{now.strftime('%y%m%d%H%M%S')}-{now.microsecond // 1000:03d}-{random_part}"


def _result_dict(result: Any) -> Dict[str, Any]:
    if result is None:
        return {}
    if hasattr(result, "to_dict"):
        try:
            return result.to_dict()
        except Exception:
            pass
    if isinstance(result, dict):
        return result
    return {
        "success": bool(getattr(result, "success", False)),
        "status": str(getattr(result, "status", "UNKNOWN")),
        "code": str(getattr(result, "code", "UNKNOWN")),
        "message": str(getattr(result, "message", "")),
        "operation": str(getattr(result, "operation", "")),
        "commands": getattr(result, "commands", []),
        "data": getattr(result, "data", {}),
        "warnings": getattr(result, "warnings", []),
        "errors": getattr(result, "errors", []),
        "created_at": getattr(result, "created_at", datetime.now().isoformat(timespec="seconds")),
    }


def _command_trace(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    trace: List[Dict[str, Any]] = []
    for item in payload.get("commands", []) or []:
        if hasattr(item, "to_dict"):
            try:
                trace.append(item.to_dict())
                continue
            except Exception:
                pass
        if isinstance(item, dict):
            trace.append(item)
            continue
        trace.append(
            {
                "command": list(getattr(item, "command", [])),
                "return_code": getattr(item, "return_code", -1),
                "stdout": getattr(item, "stdout", ""),
                "stderr": getattr(item, "stderr", ""),
            }
        )
    return trace


def _build_report_payload(operation_title: str, result: Dict[str, Any]) -> Dict[str, Any]:
    data = result.get("data", {}) or {}
    report_payload = {
        "operation_id": str(result.get("operation_id") or _operation_id()),
        "system_name": "iKornsDevGit",
        "operation_type": operation_title,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "source_path": str(data.get("repo_root") or data.get("source_path") or ""),
        "target_path": str(data.get("target_path") or ""),
        "validation_result": data.get("validation_result") or {"status": result.get("status", "UNKNOWN")},
        "preview_result": data.get("preview_result") or {},
        "backup_id": data.get("backup_id") or "",
        "backup_path": data.get("backup_path") or "",
        "execution_result": {
            "status": result.get("status", "UNKNOWN"),
            "success": bool(result.get("success", False)),
            "message": result.get("message", ""),
        },
        "success": bool(result.get("success", False)),
        "affected_items": data.get("affected_items") or data.get("selected_paths") or [],
        "command_trace": _command_trace(result),
        "report_paths": {},
        "history_status": "PENDING",
        "warnings": result.get("warnings", []) or [],
        "errors": result.get("errors", []) or [],
    }
    return report_payload


def _append_history(report_payload: Dict[str, Any], report_paths: Dict[str, str]) -> Dict[str, Any]:
    _ensure_report_folders()
    entry = dict(report_payload)
    entry["report_paths"] = dict(report_paths)
    existing: List[Dict[str, Any]] = []
    if HISTORY_PATH.exists():
        try:
            loaded = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
            if isinstance(loaded, list):
                existing = loaded
        except Exception:
            existing = []
    existing.append(entry)
    HISTORY_PATH.write_text(
        json.dumps(existing, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return {"success": True, "path": str(HISTORY_PATH), "count": len(existing)}


def export_operation(result: Any, operation_title: str) -> Dict[str, Any]:
    payload = _result_dict(result)
    if not payload:
        return {"success": False, "status": "FAIL", "message": "No result to export."}

    if GitReportService is None:
        return {"success": False, "status": "FAIL", "message": "GitReportService unavailable."}

    _ensure_report_folders()
    report_payload = _build_report_payload(operation_title, payload)
    report_result = GitReportService().write_report(report_payload)
    report_dict = report_result.to_dict() if hasattr(report_result, "to_dict") else dict(report_result)
    history_result = _append_history(report_payload, report_dict.get("paths", {}) or {})
    report_payload["report_paths"] = report_dict.get("paths", {}) or {}
    report_payload["history_status"] = "PASS" if history_result.get("success") else "FAIL"
    return {
        "report_result": report_dict,
        "history_result": history_result,
        "payload": report_payload,
    }


def print_header() -> None:
    print(CONSOLE_BUILDER.build_header(_runtime_data()))


def print_git_options() -> None:
    print("Select Git Mode:")
    print("[1] GIT STATUS        : Show repository status")
    print("[2] STAGE SELECTED    : Stage selected files after path input")
    print("[3] STAGE ALL         : Stage all changed files with YES confirm")
    print("[4] COMMIT            : Commit staged files with message")
    print("[5] PUSH              : Push current branch with YES confirm")
    print("[6] PULL              : Pull latest changes with YES confirm")
    print("[7] PUBLISH FLOW      : Status -> Stage -> Commit -> Push")
    print("[0] EXIT              : Exit git console")
    print(LINE)


def normalize_yes_no(raw_value: str) -> str:
    return str(raw_value or "").strip().strip('"').strip("'").rstrip(".").upper()


def is_yes(raw_value: str) -> bool:
    return normalize_yes_no(raw_value) in {"Y", "YES"}


def is_no(raw_value: str) -> bool:
    return normalize_yes_no(raw_value) in {"N", "NO"}


def split_paths(raw_value: str) -> List[str]:
    paths: List[str] = []
    for item in str(raw_value or "").split(","):
        clean = item.strip().strip('"').strip("'")
        if clean and clean.lower() not in {"0", "-", "none", "null"}:
            paths.append(clean)
    return paths


def print_progress(stage: str, percent: int, message: str) -> None:
    print(f"[{stage.upper()}][GIT] {percent:3d}% - {message}")


def result_to_dict(result: Any) -> Dict[str, Any]:
    if result is None:
        return {
            "success": False,
            "status": "FAIL",
            "message": "No result returned.",
        }

    if hasattr(result, "to_dict"):
        try:
            return result.to_dict()
        except Exception:
            pass

    if isinstance(result, dict):
        return result

    return {
        "success": bool(getattr(result, "success", False)),
        "status": str(getattr(result, "status", "UNKNOWN")),
        "message": str(getattr(result, "message", "")),
        "data": getattr(result, "data", {}),
        "warnings": getattr(result, "warnings", []),
        "errors": getattr(result, "errors", []),
    }


def print_result_summary(title: str, result: Any) -> None:
    payload = result_to_dict(result)

    print("=" * 61)
    print("GIT SUMMARY")
    print("=" * 61)
    print(f"Operation : {title}")
    print(f"Status    : {payload.get('status', '-')}")
    print(f"Success   : {payload.get('success', False)}")
    print(f"Message   : {payload.get('message', '-')}")

    data = payload.get("data", {}) or {}
    if data:
        print("-" * 61)
        print("Data:")
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"- {key}: {value}")
            else:
                print(f"- {key}: {value}")

    warnings = payload.get("warnings", []) or []
    if warnings:
        print("-" * 61)
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")

    errors = payload.get("errors", []) or []
    if errors:
        print("-" * 61)
        print("Errors:")
        for item in errors:
            print(f"- {item}")

    commands = payload.get("commands", []) or []
    if commands:
        print("-" * 61)
        print("Commands:")
        for command in commands:
            print(f"- {command.get('command', [])} -> {command.get('return_code', '-')}")
            stdout = str(command.get("stdout", "")).strip()
            stderr = str(command.get("stderr", "")).strip()
            if stdout:
                print(f"  stdout: {stdout}")
            if stderr:
                print(f"  stderr: {stderr}")

    print("=" * 61)


def build_service() -> Optional[Any]:
    if GitExecutionService is None:
        print("[ERROR] GitExecutionService import failed or not available.")
        return None

    service = GitExecutionService()
    project_root = _normalize_runtime_path(PROJECT_ROOT)
    script_path = _normalize_runtime_path(Path(__file__).resolve().parent)
    current_working_directory = _normalize_runtime_path(Path.cwd())
    repo_root = _normalize_runtime_path(getattr(service, "repo_root", "") or "")

    for candidate in (script_path, current_working_directory):
        if not _is_within_normalized_root(candidate, project_root):
            print("[ERROR] Git runtime blocked outside iKornsDev project root.")
            return None

    if str(repo_root) and not _is_within_normalized_root(repo_root, project_root):
        print("[ERROR] Git runtime blocked outside iKornsDev project root.")
        return None
    return service


def prompt_status(service: Any) -> Any:
    print_progress("STATUS", 10, "Reading repository status")
    return service.status()


def prompt_stage_selected(service: Any) -> Any:
    paths_input = input("Enter file paths (comma-separated): ")
    paths = split_paths(paths_input)

    if not paths:
        print("No valid paths provided.")
        return None

    confirm = input("Confirm stage selected files? (Y/N): ")
    if not is_yes(confirm):
        print("Stage selected cancelled.")
        return None

    print_progress("STAGE", 30, "Staging selected files")
    return service.stage_selected(paths)


def prompt_stage_all(service: Any) -> Any:
    confirm = input("Confirm stage all changed files? (Y/N): ")
    if not is_yes(confirm):
        print("Stage all cancelled.")
        return None

    print_progress("STAGE", 30, "Staging all changed files")
    return service.stage_all()


def prompt_commit(service: Any) -> Any:
    message = input("Enter commit message: ").strip()

    if not message:
        print("Commit cancelled. Message is required.")
        return None

    confirm = input("Confirm commit? (Y/N): ")
    if not is_yes(confirm):
        print("Commit cancelled.")
        return None

    print_progress("COMMIT", 60, "Creating commit")
    return service.commit(message)


def prompt_push(service: Any) -> Any:
    confirm = input("Confirm push current branch? (Y/N): ")
    if not is_yes(confirm):
        print("Push cancelled.")
        return None

    print_progress("PUSH", 80, "Pushing current branch")
    return service.push()


def prompt_pull(service: Any) -> Any:
    confirm = input("Confirm pull latest changes? (Y/N): ")
    if not is_yes(confirm):
        print("Pull cancelled.")
        return None

    print_progress("PULL", 80, "Pulling latest changes")
    return service.pull()


def prompt_publish_flow(service: Any) -> Any:
    print("Publish Flow: Status -> Stage -> Commit -> Push")
    confirm = input("Confirm publish flow? (Y/N): ")
    if not is_yes(confirm):
        print("Publish flow cancelled.")
        return None

    stage_choice = input("Stage all changed files? (Y/N): ")
    stage_all = is_yes(stage_choice)

    selected_paths: List[str] = []
    if not stage_all:
        selected_paths = split_paths(input("Enter selected paths (comma-separated): "))
        if not selected_paths:
            print("Publish flow cancelled. No selected paths provided.")
            return None

    commit_message = input("Enter commit message: ").strip()
    if not commit_message:
        print("Publish flow cancelled. Commit message is required.")
        return None

    print_progress("PUBLISH", 10, "Running Status -> Stage -> Commit -> Push")
    return service.publish_flow(
        commit_message=commit_message,
        stage_all=stage_all,
        selected_paths=selected_paths,
    )


def main() -> None:
    service = build_service()

    if service is None:
        return

    while True:
        print_header()
        print_git_options()

        choice = input("Enter Choice (0-7): ").strip()

        if choice == "0":
            print("Exiting git console.")
            return

        result = None
        operation_title = ""

        if choice == "1":
            operation_title = "GIT STATUS"
            result = prompt_status(service)
        elif choice == "2":
            operation_title = "STAGE SELECTED"
            result = prompt_stage_selected(service)
        elif choice == "3":
            operation_title = "STAGE ALL"
            result = prompt_stage_all(service)
        elif choice == "4":
            operation_title = "COMMIT"
            result = prompt_commit(service)
        elif choice == "5":
            operation_title = "PUSH"
            result = prompt_push(service)
        elif choice == "6":
            operation_title = "PULL"
            result = prompt_pull(service)
        elif choice == "7":
            operation_title = "PUBLISH FLOW"
            result = prompt_publish_flow(service)
        else:
            print("Invalid choice. Returning to main menu.")
            input("Press Enter to continue...")
            continue

        if result is not None:
            print_result_summary(operation_title, result)
            export_result = export_operation(result, operation_title)
            export_payload = export_result.get("payload", {}) if isinstance(export_result, dict) else {}
            report_result = export_result.get("report_result", {}) if isinstance(export_result, dict) else {}
            history_result = export_result.get("history_result", {}) if isinstance(export_result, dict) else {}

            if export_result and export_result.get("report_result"):
                print("-" * 61)
                print("EXPORT")
                print(f"Status      : {report_result.get('status', '-')}")
                print(f"Report ID   : {report_result.get('report_id', '-')}")
                paths = report_result.get("paths", {}) or {}
                for key, value in paths.items():
                    print(f"{key.upper():<11}: {value}")
                print(f"History     : {history_result.get('path', '-')}")
                print(f"HistoryRows : {history_result.get('count', '-')}")
                print(f"HistoryStat : {export_payload.get('history_status', '-')}")
                print("-" * 61)
        else:
            print("No operation executed.")

        input("Press Enter to return to main menu...")


if __name__ == "__main__":
    main()
