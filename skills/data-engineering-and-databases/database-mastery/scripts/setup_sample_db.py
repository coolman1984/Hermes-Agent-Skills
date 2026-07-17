#!/usr/bin/env python3
import argparse, os, random
from pathlib import Path
import duckdb
import pandas as pd

PRODUCTS = ['Widget', 'Gadget', 'Service']
REGIONS = ['Cairo', 'Alex', 'Delta']
CUSTOMERS = [f'C{i:03d}' for i in range(1, 61)]

def build(out: Path, rows: int = 600):
    out.parent.mkdir(parents=True, exist_ok=True)
    random.seed(7)
    sales=[]
    for i in range(rows):
        month = pd.Timestamp('2026-01-01') + pd.DateOffset(months=random.randint(0,5))
        product=random.choice(PRODUCTS); region=random.choice(REGIONS); cust=random.choice(CUSTOMERS)
        qty=random.randint(1,20); price={'Widget':100,'Gadget':180,'Service':300}[product] * random.uniform(.85,1.2)
        sales.append(dict(order_id=i+1, order_date=month+pd.Timedelta(days=random.randint(0,27)), customer_id=cust, product=product, region=region, qty=qty, unit_price=round(price,2), revenue=round(qty*price,2)))
    sales_df=pd.DataFrame(sales)
    budget=[]
    for month in pd.date_range('2026-01-01', periods=6, freq='MS'):
        for product in PRODUCTS:
            for region in REGIONS:
                budget.append(dict(month=month, product=product, region=region, budget_qty=180, budget_price={'Widget':100,'Gadget':180,'Service':300}[product], budget_revenue=180*{'Widget':100,'Gadget':180,'Service':300}[product]))
    budget_df=pd.DataFrame(budget)
    con=duckdb.connect(str(out))
    con.execute('create or replace table sales as select * from sales_df')
    con.execute('create or replace table budget as select * from budget_df')
    con.execute('create or replace table monthly_sales as select date_trunc(\'month\', order_date) as month, product, region, sum(qty) qty, sum(revenue) revenue from sales group by 1,2,3')
    con.close()
    xlsx=out.with_suffix('.xlsx')
    with pd.ExcelWriter(xlsx, engine='openpyxl') as writer:
        sales_df.to_excel(writer, sheet_name='Sales Export', index=False)
        budget_df.to_excel(writer, sheet_name='Budget', index=False)
    print({'duckdb': str(out), 'excel': str(xlsx), 'sales_rows': len(sales_df), 'budget_rows': len(budget_df), 'sales_total': round(float(sales_df.revenue.sum()),2)})

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out', default='/tmp/dbmastery/demo.duckdb')
    ap.add_argument('--rows', type=int, default=600)
    args=ap.parse_args()
    build(Path(args.out), args.rows)
