from collections import namedtuple


Card = namedtuple("Card", "id, num_won")


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
    cards = parse_cards(i)
    to_visit = list(cards.values())
    visited = []
    map = {}
    for c in to_visit:
        map.update(
            {c.id: [cards[num] for num in range(c.id + 1, c.id + c.num_won + 1)]}
        )

    while len(to_visit) > 0:
        card = to_visit[-1]
        new_to_visit = map[card.id]
        visited.append(card)
        to_visit.pop()
        to_visit.extend(new_to_visit)

    return len(visited)
