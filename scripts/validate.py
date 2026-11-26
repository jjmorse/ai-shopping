#!/usr/bin/env python3
"""Validate lists/*.yaml against the schema in templates/list.yaml.

Usage: python3 scripts/validate.py [files...]   (default: lists/*.yaml)
Exit 1 on any error.
"""
import datetime as dt
import glob
import sys

import yaml

STATUSES = {"todo", "researching", "decided", "bought", "skip"}
LIST_KEYS = {"list", "title", "updated", "items"}
ITEM_KEYS = {"id", "name", "status"}
OPTION_KEYS = {"product", "store", "price", "url", "checked"}


def is_date(v):
    if isinstance(v, dt.date):
        return True
    try:
        dt.date.fromisoformat(str(v))
        return True
    except ValueError:
        return False


def check(path):
    errs = []
    with open(path) as f:
        data = yaml.safe_load(f) or {}
    for k in LIST_KEYS - data.keys():
        errs.append(f"missing list key '{k}'")
    seen = set()
    for i, item in enumerate(data.get("items") or []):
        where = f"items[{i}] ({item.get('id', '?')})"
        for k in ITEM_KEYS - item.keys():
            errs.append(f"{where}: missing '{k}'")
        if item.get("id") in seen:
            errs.append(f"{where}: duplicate id")
        seen.add(item.get("id"))
        if item.get("status") not in STATUSES:
            errs.append(f"{where}: bad status {item.get('status')!r}")
        for j, opt in enumerate(item.get("options") or []):
            ow = f"{where}.options[{j}]"
            for k in OPTION_KEYS - opt.keys():
                errs.append(f"{ow}: missing '{k}'")
            if "price" in opt and not isinstance(opt["price"], (int, float)):
                errs.append(f"{ow}: price must be a number")
            if opt.get("checked") is not None and not is_date(opt["checked"]):
                errs.append(f"{ow}: checked not YYYY-MM-DD")
            if opt.get("sale_ends") and not is_date(opt["sale_ends"]):
                errs.append(f"{ow}: sale_ends not YYYY-MM-DD")
    return errs


def main():
    files = sys.argv[1:] or sorted(glob.glob("lists/*.yaml"))
    bad = 0
    for path in files:
        errs = check(path)
        status = "ok" if not errs else f"{len(errs)} error(s)"
        print(f"{path}: {status}")
        for e in errs:
            print(f"  - {e}")
        bad += len(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
