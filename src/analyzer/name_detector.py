import os
from pathlib import Path

try:
    # RapidFuzz gives us fast, fuzzy substring matches (e.g., "al3x" ~ "alex")
    from rapidfuzz import fuzz
    HAS_RAPIDFUZZ = True
except Exception:  # pragma: no cover - optional dependency
    HAS_RAPIDFUZZ = False


class NameDetector:
    def __init__(
        self,
        name_file_path=None,
        fuzzy_threshold: int = 90,
        min_length: int = 3,
    ):
        """
        Detect personal names inside passwords.

        name_file_path: path to newline-delimited names. If None, defaults to repo data.
        fuzzy_threshold: RapidFuzz partial_ratio score required to count as a match.
        min_length: ignore names shorter than this to reduce junk matches.
        """
        self.fuzzy_threshold = fuzzy_threshold
        self.min_length = min_length

        if name_file_path is None:
            # Resolve to the bundled data file relative to this module.
            name_file_path = Path(__file__).resolve().parents[2] / "data" / "common-names.txt"

        self.names = self._load_names(name_file_path)

    def _load_names(self, path: Path) -> set[str]:
        path = Path(path)
        if not path.exists():
            # fallback: small built-in list so code never crashes
            return {"alex", "maria", "john", "david", "sofia"}

        names = set()
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                name = line.strip().lower()
                if name:
                    names.add(name)
        return names

    def _match_names(self, password: str) -> list[str]:
        # Normalize to catch leetspeak (e.g., p@ul -> paul)
        from src.utils import normalization

        pw = normalization.normalize(password)
        matched: set[str] = set()

        if HAS_RAPIDFUZZ:
            for name in self.names:
                if len(name) < self.min_length:
                    continue
                # partial_ratio catches substrings and minor substitutions
                if fuzz.partial_ratio(name, pw) >= self.fuzzy_threshold:
                    matched.add(name)
        else:
            for name in self.names:
                if len(name) >= self.min_length and name in pw:
                    matched.add(name)

        # Drop shorter names that are substrings of longer matches to avoid double counting
        filtered = []
        for name in sorted(matched, key=len, reverse=True):
            if not any(name != other and name in other for other in filtered):
                filtered.append(name)

        return sorted(filtered)

    def analyze(self, password: str):
        found = self._match_names(password)

        return {
            "contains_name": len(found) > 0,
            "matched_names": found,
            "name_score": len(found),   # 1 per unique hit
        }

    def evaluate(self, passwords):
        # Must return list of results, one per password
        return [self.analyze(pw) for pw in passwords]
