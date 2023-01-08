from behave import when, then
from config.Configuration import Configuration

config: Configuration = None

@when('asadas')
def step_impl(context):
    config = Configuration('LOCAL')
    assert config.url is not None

@then('dssas')
def step_impl(context):
    config = Configuration('LOCAL')
    assert config.environment == 'LOCAL'
    assert True
