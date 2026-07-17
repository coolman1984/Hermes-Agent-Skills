def classify_invoice(amount, vendor):
    action = 'auto-approve' if amount <= 1000 and vendor in {'known-vendor'} else 'needs-human-review'
    return {'vendor': vendor, 'amount': amount, 'action': action}

if __name__ == '__main__':
    assert classify_invoice(500,'known-vendor')['action']=='auto-approve'
    assert classify_invoice(5000,'known-vendor')['action']=='needs-human-review'
    assert classify_invoice(100,'new-vendor')['action']=='needs-human-review'
    print('PASS ai automation human gate', classify_invoice(5000,'known-vendor'))
