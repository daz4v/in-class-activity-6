from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class AgentConfig:
    repo: str
    model: str
    host: str
    temperature: float
    github_token: str = ""
    github_owner: str = ""
    github_repo: str = ""
    verbose: bool = False


@dataclass(frozen=True)
class RunResult:
    ok: bool
    details: str


@dataclass
class CodeReview:
    """Result of code review analysis."""
    changes_summary: str
    change_type: str  # feature, bugfix, refactor, docs, other
    risk_level: str  # low, medium, high
    issues_found: list[str]
    improvements: list[str]
    recommendation: str  # issue, pr, nothing
    evidence: str


@dataclass
class DraftContent:
    """Draft Issue or PR content."""
    title: str
    body: str
    draft_type: str  # issue or pr
    is_approved: bool = False


@dataclass
class ReflectionVeredict:
    """Critic's reflection on draft quality."""
    passed: bool
    issues: list[str]
    suggestions: list[str]
    evidence: str


@dataclass
class ApprovalState:
    """Tracks draft approval workflow."""
    draft_id: str
    draft_content: DraftContent = field(default_factory=lambda: DraftContent("", "", "issue"))
    reflection: Optional[ReflectionVeredict] = None
    user_approved: bool = False
    created_url: Optional[str] = None