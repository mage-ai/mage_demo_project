@extension('great_expectations')
def validate(validator, *args, **kwargs):
    validator.expect_table_row_count_to_be_between(
        min_value=1000,
        max_value=10000,
    )