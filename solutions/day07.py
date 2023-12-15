from collections import Counter

PART1_LABELS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
PART2_LABELS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def deal_with_jokers(hand: str, translator: dict[str, int]) -> str:
    """
    Checks for jokers ("J") in the hand, replaces them with the
    most common (count[x]) AND highest value (translator[x]) other character in the hand
    (defaulting to the most valuable character "A" in the edge case of "JJJJJ")
    """
    if "J" in hand:
        count = Counter(hand)
        del count["J"]  # to avoid replacing J with J
        best_val_char = max(
            count, key=lambda x: (count[x], translator[x]), default=min(translator)
        )
        return hand.replace("J", best_val_char)
    return hand


def first_order(hand: str) -> int:
    """
    Uses a count of each character to determine order
    e.g. "32T3K" results in {"3": 2, "2": 1, "T": 1, "K": 1}
    therefore the distinct set of values in the count result is {1, 2}
    This could be true for one or two pair, so the length of count results is checked
    Length is 4 (there are 4 distinct chars), so must be one pair; the order is 2
    """
    count = Counter(hand)
    count_values_set = frozenset(count.values())
    order_map = {
        frozenset([5]): 7,  # Five of a kind (e.g. AAAAA)
        frozenset([1, 4]): 6,  # Four of a kind (e.g. AA8AA)
        frozenset([2, 3]): 5,  # Full house (e.g. 23332)
        frozenset([1, 3]): 4,  # Three of a kind (e.g. TTT98)
        frozenset([1]): 1,  # High card (e.g. 23456)
    }
    return order_map.get(
        count_values_set, 3 if len(count) == 3 else 2
    )  # Two pair (e.g. 23432) or One pair (e.g. A23A4)


def second_order(hand: str, translator: dict[str, int]) -> list[int]:
    """
    Converts hand into a list of ints for ordering
    e.g. "A" maps to 13; "2" maps to 1
    Therefore "32T3K" maps to [2, 1, 9, 2, 12]
    """
    return [translator[char] for char in hand]


def add_ordering(
    hands: list[str], labels: list[str], jokers: bool = False
) -> list[tuple[str, int, list[int]]]:
    """
    Takes the list of hand-bet lines, creates a tuple,
    adding a list of orders (first, then second)
    e.g. "32T3K 765" turns into ("32T3K", 765, [2, 2, 1, 9, 2, 12])
    where the first int is the first order, and the subsequent 5 are the second order
    """
    translator = {label: num for label, num in zip(labels, range(len(labels), 0, -1))}
    if jokers:
        return [
            (
                hand,
                int(bet),
                [first_order(deal_with_jokers(hand, translator))]
                + second_order(hand, translator),
            )
            for hand, bet in (ln.split() for ln in hands)
        ]
    return [
        (hand, int(bet), [first_order(hand)] + second_order(hand, translator))
        for hand, bet in (ln.split() for ln in hands)
    ]


def part1(i: list[str]) -> int:
    """
    Adds ordering to the hand-bet lines, resulting in a list of tuples,
    then sorts the list of tuples according to the ordering
    then uses enumerate to find the rank (must start at 1!),
    and calculates the rank * bet
    """
    return sum(
        rank * bet
        for rank, (_, bet, _) in enumerate(
            sorted(add_ordering(i, PART1_LABELS), key=lambda x: x[2]), start=1
        )
    )


def part2(i: list[str]) -> int:
    """
    Adds ordering to the hand-bet lines, dealing with jokers as an added complication,
    resulting in a list of tuples,
    then sorts the list of tuples according to the ordering
    then uses enumerate to find the rank (must start at 1!),
    and calculates the rank * bet
    """
    return sum(
        rank * bet
        for rank, (_, bet, _) in enumerate(
            sorted(add_ordering(i, PART2_LABELS, True), key=lambda x: x[2]), start=1
        )
    )
