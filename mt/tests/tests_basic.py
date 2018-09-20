import pytest

from mt.base.application import Application
from mt.base.application.implementations.web_ui import ViaWebUI


def test_login(application):
    view = ViaWebUI.navigate_to(application.web_ui, "LoggedIn")
    assert view.is_displayed


def test_edit_profile(application, request):
    profile = application.collections.profiles.instantiate(username=application.username)

    @request.addfinalizer
    def _revert():
        profile.update(username="misharov", about="")

    # import pudb; pudb.set_trace()
    profile.update(username="misharov2", about="My bio")
    view = ViaWebUI.navigate_to(profile, "Details")
    assert view.title.text == "User: misharov2"