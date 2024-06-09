import pytest
from q_0948_bagOfTokens import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_bagOfTokensScore(self, tokens: List[int], power: int, output: int):
        sc = Solution()
        assert sc.bagOfTokensScore() == output
