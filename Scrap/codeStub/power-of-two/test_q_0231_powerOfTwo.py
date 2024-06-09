import pytest
from q_0231_powerOfTwo import Solution


@pytest.mark.parametrize("n, output", [(1, True), (16, True), (3, False)])
class TestSolution:
    def test_isPowerOfTwo(self, n: int, output: bool):
        sc = Solution()
        assert (
            sc.isPowerOfTwo(
                n,
            )
            == output
        )
