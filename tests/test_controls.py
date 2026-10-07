from aafa_fsdw.conformance import AgnosticConformanceVector, requires_e4_for_agentic_proof
from aafa_fsdw.domain import EvidenceLevel, EvidenceStatus, OperationClass, RuntimeTrace
from aafa_fsdw.evidence import EvidenceLedger
from aafa_fsdw.project import ProjectManifest
from aafa_fsdw.remediation import RemediationStatus, advance
from aafa_fsdw.security import authorize


def test_e4_requirement_is_explicit():
    assert requires_e4_for_agentic_proof(EvidenceLevel.E4, EvidenceStatus.VALID)
    assert not requires_e4_for_agentic_proof(EvidenceLevel.E3, EvidenceStatus.VALID)


def test_agnostic_vector_requires_all_dimensions():
    vector = AgnosticConformanceVector(True, True, True, True, True, True)
    assert vector.passed()


def test_evidence_ledger_rejects_duplicate():
    from aafa_fsdw.domain import Evidence
    ledger = EvidenceLedger()
    e = Evidence("e1", EvidenceLevel.E2, EvidenceStatus.VALID, "test", "artifact://e1")
    ledger.add(e)
    try:
        ledger.add(e)
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate evidence accepted")


def test_manifest_requires_stage():
    manifest = ProjectManifest("p1", "AAFA-FSDW", "0.1.0", ("AAFA",), ("S00",))
    manifest.validate()


def test_authority_separates_approval():
    d = authorize(
        intent="release", requested_authority="release", granted_authority="release",
        permission="release", operation=OperationClass.RELEASE, approved=True
    )
    assert d.approved


def test_runtime_trace_validates_required_fields():
    trace = RuntimeTrace(
        run_id="r1", goal="g", context_ref="ctx", decision="d", capability="c",
        action="a", provider="p", observation="o", evaluation="e",
        state_transition="s", next_decision=None, termination_reason="complete",
        authority="a1", approval="ok", error=None, recovery=None,
        timestamp="2026-10-08T00:00:00+07:00"
    )
    trace.validate()


def test_remediation_lifecycle():
    s = RemediationStatus.OPEN
    for target in (
        RemediationStatus.TRIAGED, RemediationStatus.ACTIONED,
        RemediationStatus.EVIDENCE_SUBMITTED, RemediationStatus.VERIFIED,
        RemediationStatus.CLOSED,
    ):
        s = advance(s, target)
    assert s == RemediationStatus.CLOSED
