#!/usr/bin/env python3
import argparse, duckdb, time
ap=argparse.ArgumentParser()
ap.add_argument('db')
ap.add_argument('sql')
args=ap.parse_args()
con=duckdb.connect(args.db)
print('--- EXPLAIN ---')
for row in con.execute('explain ' + args.sql).fetchall(): print(row[1] if len(row)>1 else row[0])
start=time.perf_counter(); rows=con.execute(args.sql).fetchall(); elapsed=time.perf_counter()-start
print('--- RESULT ---')
print({'rows': len(rows), 'elapsed_seconds': round(elapsed, 6), 'sample': rows[:3]})
