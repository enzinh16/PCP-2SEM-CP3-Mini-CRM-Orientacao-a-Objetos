import json
import csv
from pathlib import Path
from typing import List, Dict


class ModelRepository:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "leads.json"

    def _load(self) -> List[Dict]:
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads: List[Dict]):
        self.db_path.write_text(
            json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def add_lead(self, lead_dict: Dict):
        leads = self._load()
        leads.append(lead_dict)
        self._save(leads)

    def read_leads(self) -> List[Dict]:
        return self._load()

    def search_leads(self, query: str) -> List[Dict]:
        query = query.lower()
        leads = self._load()
        return [
            l for l in leads
            if query in l["name"].lower()
            or query in l["company"].lower()
            or query in l["email"].lower()
        ]

    def export_csv(self, path=None) -> Path:
        path = Path(path) if path else (self.data_dir / "leads.csv")
        leads = self._load()
        if not leads:
            return None
        try:
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "name",
                        "company",
                        "email",
                        "stage",
                        "lead_type",
                        "interesse",
                        "created",
                    ],
                )
                writer.writeheader()
                for row in leads:
                    writer.writerow(row)
            return path
        except PermissionError:
            return None
