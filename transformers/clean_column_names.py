@transformer
def transform(data, *args, **kwargs):
    data.columns = ['_'.join(col.lower().split(' ')) for col in data.columns]
    return data