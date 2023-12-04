import time

from collections import deque
from dataclasses import dataclass
from loguru import logger


@dataclass
class Card:
    id: int
    num_won: int

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id


def parse_cards(raw_input):
    card_dict = {}
    for raw_card in raw_input:
        id = int(raw_card.split(":")[0].split()[1])
        num_won = len(
            {
                int(n.strip())
                for n in raw_card.split(":")[1].split("|")[0].strip().split()
            }.intersection(
                {
                    int(n.strip())
                    for n in raw_card.split(":")[1].split("|")[1].strip().split()
                }
            )
        )
        card_dict.update(
            {
                id: Card(
                    id=id,
                    num_won=num_won,
                )
            }
        )
    return card_dict


def part1(i):
    points = 0
    for card in parse_cards(i).values():
        points += 1 * 2 ** (card.num_won - 1) if card.num_won > 0 else 0
    return int(points)


def part2(i):
    start = time.time()
    cards = parse_cards(i)
    to_visit = deque(cards.values())
    visited = 0
    map = {
        c.id: {cards[num] for num in range(c.id + 1, c.id + c.num_won + 1)}
        for c in to_visit
    }

    mid = time.time()

    while to_visit:
        card = to_visit.pop()
        visited += 1
        for new_card in map[card.id]:
            to_visit.append(new_card)

    end = time.time()

    logger.info((mid - start, end - mid, end - start))

    return visited
