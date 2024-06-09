import pytest
from q_3163_stringCompressionIii import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_compressedString(self, word: str, output: str):
        sc = Solution()
        assert sc.compressedString() == output
