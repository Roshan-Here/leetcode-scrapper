import pytest
from q_0193_validPhoneNumbers import Solution


@pytest.mark.parametrize("", [])
class TestSolution:
    def test_validPhoneNumbers(self, output: Any):
        sc = Solution()
        assert sc.validPhoneNumbers() == output
