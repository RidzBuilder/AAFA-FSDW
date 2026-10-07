from __future__ import annotations

from dataclasses import dataclass, field
from .domain import Evidence, EvidenceStatus


@dataclass
class EvidenceLedger:
    _items: dict[str, Evidence] = field(default_factory=dict)

    def add(self, evidence: Evidence) -> None:
        if evidence.evidence_id in self._items:
            raise ValueError(f"evidence already exists: {evidence.evidence_id}")
        self._items[evidence.evidence_id] = evidence

    def get(self, evidence_id: str) -> Evidence:
        return self._items[evidence_id]

    def valid(self) -> list[Evidence]:
        return [e for e in self._items.values() if e.status == EvidenceStatus.VALID]

    def all(self) -> tuple[Evidence, ...]:
        return tuple(self._items.values())
