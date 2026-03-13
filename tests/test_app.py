import sys
import os

# add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app2 import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region = dash_duo.find_element("#region-filter")
    assert region is not None