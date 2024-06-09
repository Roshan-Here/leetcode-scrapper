import pytest
from q_3136_validWord import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_isValid(self, word: str, output: bool):
        sc = Solution()
        assert sc.isValid() == output
