import pytest
from q_3144_minimumSubstringPartitionOfEqualCharacterFrequency import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_minimumSubstringsInPartition(self, s: str, output: int):
        sc = Solution()
        assert sc.minimumSubstringsInPartition() == output
