from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class ProjectDocument:
    """Represent a document linked to a project."""

    project_id: str
    file_name: str
    register_date: float
    alg: str = "SHA-256"
    typ: str = "DOCUMENT"

    @classmethod
    def create(cls, project_id: str, file_name: str):
        """Create a document with the current UTC timestamp."""
        return cls(
            project_id=project_id,
            file_name=file_name,
            register_date=datetime.now(timezone.utc).timestamp(),
        )

    def _signature_payload(self) -> str:
        """Build the canonical payload used to compute the signature."""
        return (
            f"{{alg:{self.alg}, typ:{self.typ}, project_id:{self.project_id}, "
            f"file_name:{self.file_name}, register_date:{self.register_date}}}"
        )

    @property
    def file_signature(self) -> str:
        """Return the SHA-256 signature of the document payload."""
        return hashlib.sha256(
            self._signature_payload().encode("utf-8")
        ).hexdigest()

    def to_json(self):
        """Serialize the document as a JSON-compatible dictionary."""
        return {
            "alg": self.alg,
            "typ": self.typ,
            "project_id": self.project_id,
            "file_name": self.file_name,
            "register_date": self.register_date,
            "file_signature": self.file_signature,
        }
