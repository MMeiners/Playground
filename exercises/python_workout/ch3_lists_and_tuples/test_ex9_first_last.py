import pytest
from ex9_first_last import get_first_last


@pytest.mark.parametrize('input_sequence, output_sequence', [('apple', 'ae'), ([1, 2, 3, 4], [1, 4])])
def test_get_first_last(input_sequence, output_sequence):
    assert get_first_last(input_sequence) == output_sequence
