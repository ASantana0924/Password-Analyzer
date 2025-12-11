import os
import re

class NameDetector:
    def __init__(self, name_file_path="../../data/common-names.txt"):
        self.names = set()
        self._load_names(name_file_path)

    def _load_names(self, path):
        if not os.path.exists(path):
            # fallback: small built-in list so code never crashes
            self.names = {"alex", "maria", "john", "david", "sofia"}
            return

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip().lower()
                if name:
                    self.names.add(name)

    def analyze(self, password: str):
        pw = password.lower()

        found = []
        # We match names as substrings, but ensure that
        # the substring has length >= 3 to avoid junk matches.
        for name in self.names:
            if len(name) >= 3 and name in pw:
                found.append(name)

        return {
            "contains_name": len(found) > 0,
            "matched_names": found,
            "name_score": len(found),   # 1 per unique hit
        }

    def evaluate(self, passwords):
        # Must return list of results, one per password
        return [self.analyze(pw) for pw in passwords]
