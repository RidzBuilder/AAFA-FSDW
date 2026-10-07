from .domain import OperationalStatus

_ALLOWED = {
    OperationalStatus.ACTIVE: {
        OperationalStatus.BLOCKED, OperationalStatus.SUSPENDED,
        OperationalStatus.COMPLETED, OperationalStatus.FAILED,
    },
    OperationalStatus.BLOCKED: {OperationalStatus.ACTIVE, OperationalStatus.FAILED},
    OperationalStatus.SUSPENDED: {OperationalStatus.ACTIVE, OperationalStatus.FAILED},
    OperationalStatus.COMPLETED: set(),
    OperationalStatus.FAILED: {OperationalStatus.ACTIVE},
}


def transition(current: OperationalStatus, target: OperationalStatus) -> OperationalStatus:
    if target not in _ALLOWED[current]:
        raise ValueError(f"invalid transition: {current.value} -> {target.value}")
    return target
