import pytest
from q_1418_displayTableOfFoodOrdersInARestaurant import Solution


@pytest.mark.parametrize(
    "orders, output",
    [
        (
            [
                ["David", "3", "Ceviche"],
                ["Corina", "10", "Beef Burrito"],
                ["David", "3", "Fried Chicken"],
                ["Carla", "5", "Water"],
                ["Carla", "5", "Ceviche"],
                ["Rous", "3", "Ceviche"],
            ],
            [
                ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
                ["3", "0", "2", "1", "0"],
                ["5", "0", "1", "0", "1"],
                ["10", "1", "0", "0", "0"],
            ],
        ),
        (
            [
                ["James", "12", "Fried Chicken"],
                ["Ratesh", "12", "Fried Chicken"],
                ["Amadeus", "12", "Fried Chicken"],
                ["Adam", "1", "Canadian Waffles"],
                ["Brianna", "1", "Canadian Waffles"],
            ],
            [
                ["Table", "Canadian Waffles", "Fried Chicken"],
                ["1", "2", "0"],
                ["12", "0", "3"],
            ],
        ),
        (
            [
                ["Laura", "2", "Bean Burrito"],
                ["Jhon", "2", "Beef Burrito"],
                ["Melissa", "2", "Soda"],
            ],
            [["Table", "Bean Burrito", "Beef Burrito", "Soda"], ["2", "1", "1", "1"]],
        ),
    ],
)
class TestSolution:
    def test_displayTable(self, orders: List[List[str]], output: List[List[str]]):
        sc = Solution()
        assert (
            sc.displayTable(
                orders,
            )
            == output
        )
