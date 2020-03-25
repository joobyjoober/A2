"""CSC148 Assignment 2

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, David Liu, Mario Badr, Sophia Huynh, Misha Schwartz,
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) Diane Horton, David Liu, Mario Badr, Sophia Huynh,
Misha Schwartz, and Jaisie Sin

=== Module Description ===

This file contains the hierarchy of Goal classes.
"""
from __future__ import annotations
import math
import random
from typing import List, Tuple
from block import Block
from settings import colour_name, COLOUR_LIST


def generate_goals(num_goals: int) -> List[Goal]:
    """Return a randomly generated list of goals with length num_goals.

    All elements of the list must be the same type of goal, but each goal
    must have a different randomly generated colour from COLOUR_LIST. No two
    goals can have the same colour.

    Precondition:
        - num_goals <= len(COLOUR_LIST)
    """
    x = COLOUR_LIST
    n = random.randint(0, 1)
    temp = []
    colour = []
    if n == 1:
        while len(temp) < num_goals:
            color = COLOUR_LIST[random.randint(0, len(x)-1)]
            if not colour.__contains__(color):
                colour.append(colour_name(color))
                temp.append(PerimeterGoal(color))

        while len(temp) < num_goals:
            color = COLOUR_LIST[random.randint(0, len(x) - 1)]

            if not colour.__contains__(colour_name(color)):
                colour.append(colour_name(color))
                temp.append(BlobGoal(color))
    return temp


def _flatten(block: Block) -> List[List[Tuple[int, int, int]]]:
    """Return a two-dimensional list representing <block> as rows and columns of
    unit cells.

    Return a list of lists L, where,
    for 0 <= i, j < 2^{max_depth - self.level}
        - L[i] represents column i and
        - L[i][j] represents the unit cell at column i and row j.

    Each unit cell is represented by a tuple of 3 ints, which is the colour
    of the block at the cell location[i][j]

    L[0][0] represents the unit cell in the upper left corner of the Block.
    """
    flat = block._unit_copy()
    if not flat.children:
        return [[flat.colour]]
    else:
        l0 = _flatten(flat.children[0])
        l1 = _flatten(flat.children[1])
        l2 = _flatten(flat.children[2])
        l3 = _flatten(flat.children[3])
        i = 0
        while len(l0) > 0:
            l1[i] += l0[0]
            l0.pop(0)
            l2[i] += l3[0]
            l3.pop(0)
            i+=1


        return l1+l2




class Goal:
    """A player goal in the game of Blocky.

    This is an abstract class. Only child classes should be instantiated.

    === Attributes ===
    colour:
        The target colour for this goal, that is the colour to which
        this goal applies.
    """
    colour: Tuple[int, int, int]

    def __init__(self, target_colour: Tuple[int, int, int]) -> None:
        """Initialize this goal to have the given target colour.
        """
        self.colour = target_colour

    def score(self, board: Block) -> int:
        """Return the current score for this goal on the given board.

        The score is always greater than or equal to 0.
        """
        raise NotImplementedError

    def description(self) -> str:
        """Return a description of this goal.
        """
        raise NotImplementedError


class PerimeterGoal(Goal):
    def score(self, board: Block) -> int:
        # TODO: Implement me
        return 148  # FIXME

    def description(self) -> str:
        # TODO: Implement me
        return 'DESCRIPTION'  # FIXME


class BlobGoal(Goal):
    def score(self, board: Block) -> int:
        # TODO: Implement me
        return 148  # FIXME

    def _undiscovered_blob_size(self, pos: Tuple[int, int],
                                board: List[List[Tuple[int, int, int]]],
                                visited: List[List[int]]) -> int:
        """Return the size of the largest connected blob that (a) is of this
        Goal's target colour, (b) includes the cell at <pos>, and (c) involves
        only cells that have never been visited.

        If <pos> is out of bounds for <board>, return 0.

        <board> is the flattened board on which to search for the blob.
        <visited> is a parallel structure that, in each cell, contains:
            -1 if this cell has never been visited
            0  if this cell has been visited and discovered
               not to be of the target colour
            1  if this cell has been visited and discovered
               to be of the target colour

        Update <visited> so that all cells that are visited are marked with
        either 0 or 1.
        """
        # TODO: Implement me
        pass  # FIXME

    def description(self) -> str:
        # TODO: Implement me
        return 'DESCRIPTION'  # FIXME


if __name__ == '__main__':
    """import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': [
            'doctest', 'python_ta', 'random', 'typing', 'block', 'settings',
            'math', '__future__'
        ],
        'max-attributes': 15
    })
"""
    b = block = Block((0, 0), 64, (0, 0, 0), 0, 1)
    b.smash()
    print(_flatten(b))
