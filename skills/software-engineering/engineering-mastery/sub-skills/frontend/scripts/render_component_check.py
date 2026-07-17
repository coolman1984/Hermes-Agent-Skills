from html.parser import HTMLParser

COMPONENT_HTML = '''<section aria-labelledby="orders-title" class="card">
<h2 id="orders-title">Recent orders</h2>
<div role="status" aria-live="polite">Loaded 2 orders</div>
<table><caption>Orders by customer</caption><thead><tr><th scope="col">Customer</th><th scope="col">Amount</th></tr></thead><tbody><tr><td>ABC</td><td>120</td></tr><tr><td>XYZ</td><td>90</td></tr></tbody></table>
<button type="button">Refresh</button>
</section>'''

class Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags=[]
        self.attrs=[]
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.attrs.extend(attrs)

if __name__ == '__main__':
    p=Checker(); p.feed(COMPONENT_HTML)
    attrs=dict(p.attrs)
    assert 'section' in p.tags and 'table' in p.tags and 'caption' in p.tags
    assert ('aria-labelledby' in attrs) or ('aria-label' in attrs)
    assert ('role','status') in p.attrs
    print('PASS frontend accessible component check')
