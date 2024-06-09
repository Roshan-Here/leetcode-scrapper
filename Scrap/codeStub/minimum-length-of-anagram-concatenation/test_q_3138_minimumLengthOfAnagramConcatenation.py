import pytest
from q_3138_minimumLengthOfAnagramConcatenation import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minAnagramLength(self, s: str, output: int):
        sc = Solution()
        assert sc.minAnagramLength() == output
