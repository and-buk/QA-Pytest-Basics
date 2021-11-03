import pytest


def valid_email(email):
    import re

    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


@pytest.mark.parametrize(
    "email, result", [("test@test.ru", "1"), ("w@w.com", "1"), ("123QWE@mmm.mmm", "1")]
)
def test_valid_email(email, result, log):
    result = valid_email(email)
    assert result is True, "Email is valid!"


@pytest.mark.parametrize(
    "email, result", [("test@test.", "0"), ("w@", "0"), ("@tt", "0")]
)
def test_invalid_email(email, result, log):
    result = valid_email(email)
    assert result is False, "Email is not valid!"
