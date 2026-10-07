from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class GateOutcome(str, Enum):
    PASS = "PASS"
    BLOCK = "BLOCK"
    REJECT = "REJECT"
    EXCEPTION = "EXCEPTION"


@dataclass(frozen=True)
class GateInput:
    context_valid: bool = True
    blocker: bool = False
    unresolved_critical: bool = False
    mandatory_failure: bool = False
    evidence_missing: bool = False
    test_failure: bool = False
    remediation_open: bool = False
    claim_exceeds_evidence: bool = False
    dependency_unsatisfied: bool = False
    controlled_exception: bool = False


@dataclass(frozen=True)
class GateDecision:
    outcome: GateOutcome
    reason: str
    precedence: int


def evaluate_gate(i: GateInput) -> GateDecision:
    checks = [
        (not i.context_valid, GateOutcome.REJECT, "invalid/unsupported context", 1),
        (i.blocker, GateOutcome.BLOCK, "blocker", 2),
        (i.unresolved_critical, GateOutcome.BLOCK, "unresolved critical", 3),
        (i.mandatory_failure, GateOutcome.BLOCK, "mandatory criterion failure", 4),
        (i.evidence_missing, GateOutcome.BLOCK, "required evidence missing/invalid", 5),
        (i.test_failure, GateOutcome.BLOCK, "required test failure", 6),
        (i.remediation_open, GateOutcome.BLOCK, "unresolved required remediation", 7),
        (i.claim_exceeds_evidence, GateOutcome.BLOCK, "claim exceeds evidence", 8),
        (i.dependency_unsatisfied, GateOutcome.BLOCK, "unsatisfied dependency", 9),
        (i.controlled_exception, GateOutcome.EXCEPTION, "valid controlled exception", 10),
    ]
    for condition, outcome, reason, precedence in checks:
        if condition:
            return GateDecision(outcome, reason, precedence)
    return GateDecision(GateOutcome.PASS, "all mandatory criteria satisfied", 11)
