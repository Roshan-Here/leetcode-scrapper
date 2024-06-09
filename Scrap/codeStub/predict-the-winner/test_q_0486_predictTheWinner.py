import pytest
from q_0486_predictTheWinner import Solution


@pytest.mark.parametrize("nums, output", [([1, 5, 2], False), ([1, 5, 233, 7], True)])
class TestSolution:
    def test_predictTheWinner(self, nums: List[int], output: bool):
        sc = Solution()
        assert (
            sc.predictTheWinner(
                nums,
            )
            == output
        )
