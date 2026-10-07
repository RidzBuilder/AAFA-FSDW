from .domain import Claim, ClaimStatus, Evidence, EvidenceLevel, EvidenceStatus

_ORDER = {EvidenceLevel.E0:0, EvidenceLevel.E1:1, EvidenceLevel.E2:2,
          EvidenceLevel.E3:3, EvidenceLevel.E4:4, EvidenceLevel.E5:5}


def evaluate_claim(claim: Claim, evidence: list[Evidence]) -> ClaimStatus:
    usable = [
        e for e in evidence
        if e.evidence_id in claim.evidence_ids and e.status == EvidenceStatus.VALID
    ]
    if not usable:
        return ClaimStatus.UNVERIFIED
    strongest = max(usable, key=lambda e: _ORDER[e.level])
    if _ORDER[strongest.level] < _ORDER[claim.required_level]:
        return ClaimStatus.PARTIAL
    return ClaimStatus.PROVEN
