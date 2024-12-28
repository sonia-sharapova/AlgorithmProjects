from pytest import fixture

from reconstruct import naive_reconstruct, likely_reconstruct


@fixture(params=[naive_reconstruct, likely_reconstruct])
# @fixture(params=[likely_reconstruct])
def reconstruct(request):
    return request.param

def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        "markers", "slow: mark test to skip on automated tests"
    )
