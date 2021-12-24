"""Test boards for Connect4

Place test boards in this module to help test your code.  Note that since connect4.GameState
stores board contents as a 0-based list of lists, these boards are reversed to they can be written
right side up here.

"""

boards = {}  # dictionary with label, test board key-value pairs

boards['test_1'] = reversed([
    [  0,  0 ],
    [  1, -1 ],
    [  1, -1 ]
])

boards['test_2'] = reversed([
    [ -1,   0,  0, -1, -1 ],
    [ -1,   1, -1,  1,  1 ],
    [  1,  -1,  1, -1,  1 ],
    [  1,   1, -1,  1, -1 ]
])

boards['writeup_1'] = reversed([
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0, -1,  0,  0,  0 ],
    [  0,  0,  0,  1,  0,  0,  0 ],
    [  0,  1,  0, -1,  0,  1,  0 ]
])

boards['writeup_2'] = reversed([
    [ -1,  1, -1, -1 ],
    [  1, -1,  1, -1 ],
    [  1, -2, -1,  1 ],
    [  1, -2,  1, -1 ]
])

boards['your_test'] = reversed([0, 1, 1
                                -2, -2, -2,
                                -2, -2, -2])  # put something here!



