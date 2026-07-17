#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import duckdb
ap=argparse.ArgumentParser()
ap.add_argument('db')
ap.add_argument('out')
args=ap.parse_args()
con=duckdb.connect(args.db, read_only=True)
kpis=con.execute('select count(*) orders, round(sum(revenue),2) revenue, round(avg(revenue),2) avg_order from sales').fetchone()
by_region=con.execute('select region, round(sum(revenue),2) revenue from sales group by 1 order by 2 desc').fetchall()
by_month=con.execute("select strftime(date_trunc('month', order_date), '%Y-%m') as month_label, round(sum(revenue),2) as revenue from sales group by 1 order by 1").fetchall()
top=con.execute('select product, region, round(sum(revenue),2) revenue from sales group by 1,2 order by 3 desc limit 20').fetchall()
data={'kpis': {'orders': kpis[0], 'revenue': kpis[1], 'avg_order': kpis[2]}, 'by_region': by_region, 'by_month': by_month, 'top': top}
html=f"""<!doctype html><meta charset='utf-8'><title>Database Mastery Dashboard</title>
<style>body{{font-family:Arial;margin:24px;background:#f7f7fb}}.cards{{display:flex;gap:12px}}.card{{background:white;padding:16px;border-radius:12px;box-shadow:0 1px 4px #ccc}}table{{border-collapse:collapse;background:white;margin-top:16px}}td,th{{border:1px solid #ddd;padding:8px}}</style>
<h1>Database Mastery Dashboard</h1><div class='cards'><div class='card'><b>Orders</b><br>{kpis[0]}</div><div class='card'><b>Revenue</b><br>{kpis[1]}</div><div class='card'><b>Average Order</b><br>{kpis[2]}</div></div>
<h2>Revenue by Region</h2><pre id='region'></pre><h2>Revenue by Month</h2><pre id='month'></pre><h2>Top Product/Region Rows</h2><table><tr><th>Product</th><th>Region</th><th>Revenue</th></tr>{''.join(f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in top)}</table>
<script>const data={json.dumps(data)};region.textContent=data.by_region.map(r=>r[0]+': '+r[1]).join('\n');month.textContent=data.by_month.map(r=>r[0]+': '+r[1]).join('\n');</script>"""
Path(args.out).write_text(html, encoding='utf-8')
print({'out': args.out, 'bytes': Path(args.out).stat().st_size, 'kpis': data['kpis']})
