import pytest
from q_2694_eventEmitter import Solution


@pytest.mark.parametrize(
    "output",
    [
        ([[], ["emitted", []], ["subscribed"], ["subscribed"], ["emitted", [5, 6]]]),
        ([[], ["subscribed"], ["emitted", ["1,2,3"]], ["emitted", ["3,4,6"]]]),
        (
            [
                [],
                ["subscribed"],
                ["emitted", ["1,2,3"]],
                ["unsubscribed", 0],
                ["emitted", []],
            ]
        ),
        (
            [
                [],
                ["subscribed"],
                ["emitted", ["1,2,3"]],
                ["unsubscribed", 0],
                ["emitted", [7]],
            ]
        ),
    ],
)
class TestSolution:
    def test_eventEmitter(self, output: Any):
        sc = Solution()
        assert sc.eventEmitter() == output
