from enum import Enum


class RemediationStatus(str, Enum):
    OPEN = "OPEN"
    TRIAGED = "TRIAGED"
    ACTIONED = "ACTIONED"
    EVIDENCE_SUBMITTED = "EVIDENCE SUBMITTED"
    VERIFIED = "VERIFIED"
    CLOSED = "CLOSED"


_ALLOWED = {
    RemediationStatus.OPEN: {RemediationStatus.TRIAGED},
    RemediationStatus.TRIAGED: {RemediationStatus.ACTIONED},
    RemediationStatus.ACTIONED: {RemediationStatus.EVIDENCE_SUBMITTED},
    RemediationStatus.EVIDENCE_SUBMITTED: {RemediationStatus.VERIFIED},
    RemediationStatus.VERIFIED: {RemediationStatus.CLOSED},
    RemediationStatus.CLOSED: set(),
}


def advance(current: RemediationStatus, target: RemediationStatus) -> RemediationStatus:
    if target not in _ALLOWED[current]:
        raise ValueError(f"invalid remediation transition: {current.value} -> {target.value}")
    return target
