from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProjectManifest:
    project_id: str
    name: str
    version: str
    standard_refs: tuple[str, ...]
    stage_ids: tuple[str, ...]
    required_claims: tuple[str, ...] = ()
    metadata: dict[str, str] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.project_id or not self.name or not self.version:
            raise ValueError("project_id, name, and version are required")
        if not self.standard_refs:
            raise ValueError("at least one standard reference is required")
        if not self.stage_ids:
            raise ValueError("at least one stage is required")
