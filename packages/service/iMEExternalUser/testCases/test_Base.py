import pytest


@pytest.mark.usefixtures("init_driver", "wait_for_page_load","failed_on_failure", "environment")
class BaseTest:
    pass
