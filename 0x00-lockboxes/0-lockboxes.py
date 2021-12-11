#!/usr/bin/python3


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    opened= [0];

    for key in opened:
        for b in boxes[key]:
            if b < len(boxes) and b not in opened:
                opened.append(b);

    if len(boxes) == len(opened):
        return True;
    else:
        return False;
