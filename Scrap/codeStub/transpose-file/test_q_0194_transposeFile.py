import pytest
from q_0194_transposeFile import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_transposeFile(self, output: Any):
        sc = Solution()
        assert sc.transposeFile() == output
