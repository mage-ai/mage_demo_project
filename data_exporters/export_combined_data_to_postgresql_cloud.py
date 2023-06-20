from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path


@data_exporter
def export_data_to_postgres(df_restaurant: DataFrame, df_users, **kwargs) -> None:
    schema_name = 'core_data'
    table_name = 'users_with_restaurants'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    df = df_restaurant.merge(df_users, how='left', left_on='user_id', right_on='id_user')

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            df,
            schema_name,
            table_name,
            index=False,
            if_exists='replace',
        )