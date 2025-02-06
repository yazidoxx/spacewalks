import pytest 
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    """Test the text_to_duration function with an integer duration."""
    assert text_to_duration("10:00") == 10
    
def test_text_to_duration_float():
    """Test the text_to_duration function with a float duration."""
    assert text_to_duration("10:20") == pytest.approx(10.3333333) 
    
