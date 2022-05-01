from abs import __version__
from abs.abc086_c import can_travel


def test_version():
    assert __version__ == '0.1.0'

def test_can_travel():
    assert can_travel(2, 0, 2)
