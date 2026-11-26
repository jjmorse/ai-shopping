#!/usr/bin/env python3
"""Print a markdown summary of lists/*.yaml: best offer per item, unit price, stale prices.

Usage: python3 scripts/report.py [--stale-days N] [files...]
"""
import argparse
import datetime as dt
import glob

import yaml


def unit_price(opt):
    q = opt.get("unit_qty")
    return opt["price"] / q if q else None


def fmt(v):
    return f"${v:,.2f}" if isinstance(v, (int, float)) else "–"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stale-days", type=int, default=3)
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    today = dt.date.today()

    for path in args.files or sorted(glob.glob("lists/*.yaml")):
        with open(path) as f:
            data = yaml.safe_load(f) or {}
        print(f"## {data.get('title', path)}\n")
        items = data.get("items") or []
        if not items:
            print("_No items yet._\n")
            continue
        print("| Item | Status | Best offer | Price | Unit price | Checked |")
        print("|------|--------|------------|-------|------------|---------|")
        for it in items:
            opts = [o for o in it.get("options") or [] if isinstance(o.get("price"), (int, float))]
            if not opts:
                print(f"| {it['name']} | {it['status']} | – | – | – | – |")
                continue
            best = min(opts, key=lambda o: (unit_price(o) or o["price"]))
            checked = best.get("checked")
            stale = ""
            if checked:
                age = (today - dt.date.fromisoformat(str(checked))).days
                stale = " ⚠ stale" if age > args.stale_days else ""
            up = unit_price(best)
            up_s = f"{fmt(up)}/{best.get('unit')}" if up else "–"
            print(
                f"| {it['name']} | {it['status']} | {best.get('product')} @ {best.get('store')} "
                f"| {fmt(best['price'])} | {up_s} | {checked}{stale} |"
            )
        print()


if __name__ == "__main__":
    main()
