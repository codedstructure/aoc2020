from collections import deque
from utils import get_blank_sep_lines


def score(deck):
    return sum((len(deck) - idx) * val for (idx, val) in enumerate(deck))


def puzzle1():
    deck1, deck2 = get_blank_sep_lines('day22')
    # ignore first line; int-ify
    deck1 = deque(int(card) for card in deck1[1:])
    deck2 = deque(int(card) for card in deck2[1:])

    while deck1 and deck2:
        top1 = deck1.popleft()
        top2 = deck2.popleft()
        if top1 > top2:
            winner = deck1
        else:
            winner = deck2
        winner.append(max(top1, top2))
        winner.append(min(top1, top2))

    print(score(winner))


def recursive_combat(deck1, deck2, depth=0):
    seen_scores = set()

    while deck1 and deck2:
        # Prevent infinite recursion
        s1 = tuple(list(deck1))
        s2 = tuple(list(deck2))
        if (s1, s2) in seen_scores:
            return deck1, 1
        seen_scores.add((s1, s2))

        top1 = deck1.popleft()
        top2 = deck2.popleft()
        # print(top1, top2, deck1, deck2)
        if len(deck1) >= top1 and len(deck2) >= top2:
            r_deck1 = deque(list(deck1)[:top1])
            r_deck2 = deque(list(deck2)[:top2])
            _, player = recursive_combat(r_deck1, r_deck2, depth + 1)
            if player == 1:
                winner = deck1
                win_card, lose_card = top1, top2
            else:
                winner = deck2
                win_card, lose_card = top2, top1
        elif top1 > top2:
            winner = deck1
            win_card, lose_card = top1, top2
        else:
            winner = deck2
            win_card, lose_card = top2, top1
        winner.extend((win_card, lose_card))

    return winner, 1 if win_card == top1 else 2


def puzzle2():
    deck1, deck2 = get_blank_sep_lines('day22')
    # ignore first line; int-ify
    deck1 = deque(int(card) for card in deck1[1:])
    deck2 = deque(int(card) for card in deck2[1:])

    # Sample data
    # deck1 = deque([9, 2, 6, 3, 1])
    # deck2 = deque([5, 8, 4, 7, 10])

    winner, *_ = recursive_combat(deck1, deck2)

    print(score(winner))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
