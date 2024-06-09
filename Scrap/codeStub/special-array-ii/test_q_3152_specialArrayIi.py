import pytest
from q_3152_specialArrayIi import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_isArraySpecial(
        self, nums: List[int], queries: List[List[int]], output: List[bool]
    ):
        sc = Solution()
        assert sc.isArraySpecial() == output
