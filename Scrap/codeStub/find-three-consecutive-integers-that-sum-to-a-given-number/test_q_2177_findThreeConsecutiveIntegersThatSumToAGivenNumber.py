import pytest
from q_2177_findThreeConsecutiveIntegersThatSumToAGivenNumber import Solution


@pytest.mark.parametrize("num, output", [(33, [10, 11, 12]), (4, [])])
class TestSolution:
    def test_sumOfThree(self, num: int, output: List[int]):
        sc = Solution()
        assert (
            sc.sumOfThree(
                num,
            )
            == output
        )
