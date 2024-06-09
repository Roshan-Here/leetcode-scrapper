import pytest
from q_0396_rotateFunction import Solution


@pytest.mark.parametrize("nums, output", [([4, 3, 2, 6], 26), ([100], 0)])
class TestSolution:
    def test_maxRotateFunction(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxRotateFunction(
                nums,
            )
            == output
        )
