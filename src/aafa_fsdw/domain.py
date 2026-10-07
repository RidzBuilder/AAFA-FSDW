from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class EvidenceLevel(str, Enum):
    E0 = "E0"
    E1 = "E1"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E5 = "E5"


class EvidenceStatus(str, Enum):
    MISSING = "MISSING"
    UNVERIFIED = "UNVERIFIED"
    VALID = "VALID"
    REJECTED = "REJECTED"


class ClaimStatus(str, Enum):
    PROVEN = "PROVEN"
    PARTIAL = "PARTIAL"
    UNVERIFIED = "UNVERIFIED"
    REJECTED = "REJECTED"


class OperationalStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    SUSPENDED = "SUSPENDED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class OperationClass(str, Enum):
    READ = "READ"
    DECLARE = "DECLARE"
    MUTATE = "MUTATE"
    EXECUTE = "EXECUTE"
    EVALUATE = "EVALUATE"
    VERIFY = "VERIFY"
    APPROVE = "APPROVE"
    TRANSITION = "TRANSITION"
    RELEASE = "RELEASE"


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    level: EvidenceLevel
    status: EvidenceStatus
    source: str
    content_ref: str
    claim_ids: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Claim:
    claim_id: str
    text: str
    required_level: EvidenceLevel
    evidence_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class RuntimeTrace:
    run_id: str
    goal: str
    context_ref: str
    decision: str
    capability: str
    action: str
    provider: str
    observation: str
    evaluation: str
    state_transition: str
    next_decision: str | None
    termination_reason: str | None
    authority: str
    approval: str | None
    error: str | None
    recovery: str | None
    timestamp: str

    def validate(self) -> None:
        required = {
            "run_id": self.run_id, "goal": self.goal, "context_ref": self.context_ref,
            "decision": self.decision, "capability": self.capability, "action": self.action,
            "provider": self.provider, "observation": self.observation,
            "evaluation": self.evaluation, "state_transition": self.state_transition,
            "authority": self.authority, "timestamp": self.timestamp,
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise ValueError(f"runtime trace missing required fields: {missing}")


@dataclass(frozen=True)
class DecisionContextSnapshot:
    snapshot_id: str
    project_ref: str
    standards: tuple[str, ...]
    criteria: tuple[str, ...]
    claims: tuple[str, ...]
    evidence: tuple[str, ...]
    tests: tuple[str, ...]
    findings: tuple[str, ...]
    remediations: tuple[str, ...]
    exceptions: tuple[str, ...]
    dependencies: tuple[str, ...]
    authority: str
    version: str
