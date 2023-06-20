@transformer
def transform(row, *args, **kwargs):
    row['ssn'] = '* * *'
    row['computed_column'] = 2 * 3
    return row