from aafa_fsdw.claims import evaluate_claim
from aafa_fsdw.domain import Claim, ClaimStatus, Evidence, EvidenceLevel, EvidenceStatus, OperationalStatus
from aafa_fsdw.gates import GateInput, GateOutcome, evaluate_gate
from aafa_fsdw.state import transition


def ev(eid, level):
    return Evidence(eid, level, EvidenceStatus.VALID, "test", f"artifact://{eid}")


def test_claim_cannot_exceed_evidence():
    claim = Claim("c1", "runtime proven", EvidenceLevel.E4, ("e1",))
    assert evaluate_claim(claim, [ev("e1", EvidenceLevel.E3)]) == ClaimStatus.PARTIAL


def test_claim_is_proven_at_required_level():
    claim = Claim("c1", "runtime proven", EvidenceLevel.E4, ("e1",))
    assert evaluate_claim(claim, [ev("e1", EvidenceLevel.E4)]) == ClaimStatus.PROVEN


def test_gate_precedence_prefers_blocker():
    result = evaluate_gate(GateInput(blocker=True, controlled_exception=True))
    assert result.outcome == GateOutcome.BLOCK
    assert result.precedence == 2


def test_missing_evidence_blocks_pass():
    result = evaluate_gate(GateInput(evidence_missing=True))
    assert result.outcome == GateOutcome.BLOCK


def test_state_transition_is_controlled():
    assert transition(OperationalStatus.ACTIVE, OperationalStatus.COMPLETED) == OperationalStatus.COMPLETED
    try:
        transition(OperationalStatus.COMPLETED, OperationalStatus.ACTIVE)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid transition was accepted")
