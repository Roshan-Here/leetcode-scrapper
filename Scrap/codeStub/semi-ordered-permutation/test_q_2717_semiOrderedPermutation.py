import pytest
from q_2717_semiOrderedPermutation import Solution


@pytest.mark.parametrize(
    "nums, output", [([2, 1, 4, 3], 2), ([2, 4, 1, 3], 3), ([1, 3, 4, 2, 5], 0)]
)
class TestSolution:
    def test_semiOrderedPermutation(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.semiOrderedPermutation(
                nums,
            )
            == output
        )
