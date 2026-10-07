from dataclasses import dataclass
from .domain import OperationClass


@dataclass(frozen=True)
class AuthorityDecision:
    requested: str
    granted: str
    permission: str
    approved: bool


class AuthorityError(PermissionError):
    pass


def authorize(
    *,
    intent: str,
    requested_authority: str,
    granted_authority: str,
    permission: str,
    operation: OperationClass,
    approved: bool = False,
) -> AuthorityDecision:
    if not intent:
        raise AuthorityError("intent is required")
    if not granted_authority:
        raise AuthorityError("granted authority is required")
    if not permission:
        raise AuthorityError("permission is required")
    if operation in {OperationClass.APPROVE, OperationClass.RELEASE} and not approved:
        raise AuthorityError(f"{operation.value} requires explicit approval")
    return AuthorityDecision(
        requested=requested_authority,
        granted=granted_authority,
        permission=permission,
        approved=approved,
    )
