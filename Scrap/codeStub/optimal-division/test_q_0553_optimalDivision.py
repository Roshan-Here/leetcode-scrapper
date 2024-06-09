import pytest
from q_0553_optimalDivision import Solution


@pytest.mark.parametrize(
    "nums, output", [([1000, 100, 10, 2], "1000/(100/10/2)"), ([2, 3, 4], "2/(3/4)")]
)
class TestSolution:
    def test_optimalDivision(self, nums: List[int], output: str):
        sc = Solution()
        assert (
            sc.optimalDivision(
                nums,
            )
            == output
        )
