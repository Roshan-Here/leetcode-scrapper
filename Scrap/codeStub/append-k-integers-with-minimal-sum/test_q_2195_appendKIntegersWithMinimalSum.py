import pytest
from q_2195_appendKIntegersWithMinimalSum import Solution


@pytest.mark.parametrize(
    "nums, k, output", [([1, 4, 25, 10, 25], 2, 5), ([5, 6], 6, 25)]
)
class TestSolution:
    def test_minimalKSum(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.minimalKSum(
                nums,
                k,
            )
            == output
        )
