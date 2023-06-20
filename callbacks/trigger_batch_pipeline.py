from mage_ai.orchestration.triggers.api import trigger_pipeline


@callback('success')
def trigger(parent_block_data, **kwargs):
    trigger_pipeline('combine_and_transform_user_restaurant')
