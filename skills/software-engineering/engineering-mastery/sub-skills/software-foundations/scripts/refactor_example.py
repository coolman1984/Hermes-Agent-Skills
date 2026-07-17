from collections import Counter

def messy_count(items):
    result = {}
    for item in items:
        key = str(item).strip().lower()
        if not key:
            continue
        if key not in result:
            result[key] = 0
        result[key] += 1
    return result

def clean_count(items):
    """Normalize non-empty items and count occurrences."""
    return dict(Counter(str(item).strip().lower() for item in items if str(item).strip()))

if __name__ == '__main__':
    sample = [' Apple ', 'apple', '', 'Banana', 'BANANA', 7, '7']
    assert clean_count(sample) == messy_count(sample)
    print('PASS foundations refactor example', clean_count(sample))
