import pytest
from q_3151_specialArrayI import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_isArraySpecial(self, nums: List[int], output: bool):
        sc = Solution()
        assert sc.isArraySpecial() == output
