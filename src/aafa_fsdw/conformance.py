from __future__ import annotations

from dataclasses import dataclass
from .domain import EvidenceLevel, EvidenceStatus


@dataclass(frozen=True)
class AgnosticConformanceVector:
    semantic_independence: bool
    capability_contract_independence: bool
    provider_separation: bool
    adapter_boundary_integrity: bool
    replaceability: bool
    runtime_independence: bool

    def passed(self) -> bool:
        return all((
            self.semantic_independence,
            self.capability_contract_independence,
            self.provider_separation,
            self.adapter_boundary_integrity,
            self.replaceability,
            self.runtime_independence,
        ))


def requires_e4_for_agentic_proof(level: EvidenceLevel, status: EvidenceStatus) -> bool:
    return level == EvidenceLevel.E4 and status == EvidenceStatus.VALID
