import pytest
from q_3079_findTheSumOfEncryptedIntegers import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_sumOfEncryptedInt(self, nums: List[int], output: int):
        sc = Solution()
        assert sc.sumOfEncryptedInt() == output
