import pytest
from q_3083_existenceOfASubstringInAStringAndItsReverse import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_isSubstringPresent(self, s: str, output: bool):
        sc = Solution()
        assert sc.isSubstringPresent() == output
