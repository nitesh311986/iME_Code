import pytest


@pytest.mark.usefixtures("init_driver", "failed_on_failure", "environment","wait_for_page_load")
class BaseTest:
    pass
