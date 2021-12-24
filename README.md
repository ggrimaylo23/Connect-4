# Connect-4
 A modified version of Connect 4 in Python. An agent is made using different search algorithms (minimax, depth limited minimax, alpha-beta pruning minimax), and this agent can play against humans or other automated agents. The game will continue until the board is full (even if a player achieves 4 in a row) and scores for each player will be calculated to determine who wins. 
 The score is evaluated like this: if a player has 3 in a row or greater, the player will receive points equal to the square of the amount of tiles they have in a row. So if they have 4 in a row, they get 16 points.
 To play a game, run connect4.py from the command line and give it arguments that determine how the game is played.
 For player 1, you can choose: 'r' (agent picks a random move), 'h' (human agent, you pick their moves), 'c' (your automated agent), 'o' (the other minimax heuristic agent that is used for testing).
 For player 2, you can choose 'r', 'h', 'c', or 'o' as well.
 For example, if you wanted your agent to play against a random agent on a 4x4 board, you would type " python connect4.py h c 4 4".
 To run depth-limited minimax against a human, you would type "python connect4.py c h 8 9 --depth 4"
 To run alpha-beta pruning minimax against a human, you would type "python connect4.py c 5 6 --prune"
 Note: Normal minimax will not run on a 6x7 board or larger, so you should run it on smaller boards. 
 connect4.py houses the information for the class for a connect4 game object. agents.py has the information for all the possible agents that you can play with. test_boards.py is just for the sake of testing.
 
