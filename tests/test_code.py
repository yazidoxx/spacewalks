import pytest 
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_integer():
    """Test the text_to_duration function with an integer duration."""
    assert text_to_duration("10:00") == 10
    
def test_text_to_duration_float():
    """Test the text_to_duration function with a float duration."""
    assert text_to_duration("10:20") == pytest.approx(10.3333333) 

@pytest.mark.parametrize("input_value, expected_results",[
    ("person 1;",1),
    ("person 1 ;person 2;",2),
])

def test_calculate_crew_size(input_value, expected_results):
    """
    Test the calculate_crew_size function with various crew entries.
    """
    
    actual_result = calculate_crew_size(input_value)
    expected_result = expected_results
    assert actual_result == expected_result
    
    
