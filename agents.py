import random
import math


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def __init__(self, sd=None):
        if sd is None:
            self.st = None
        else:
            random.seed(sd)
            self.st = random.getstate()

    def get_move(self, state):
        if self.st is not None:
            random.setstate(self.st)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state):
        """Determine the minimax utility value of the given state.

        Args:
            state: a connect4.GameState object representing the current board

        Returns: the exact minimax utility value of the state
        """
        #
        # Fill this in!
        #

        # recursively traverse the game tree, eventually determining the value for that state
        # the utility of the terminal states is calculated using the GameState.utility() method
        # determine if state is terminal if the successors() function returns
        if state.is_full():
            return state.utility()
        if state.next_player() == 1:
            negative_infinity = float('-inf')
            value = negative_infinity
            for key, board in state.successors():
                value = max(value, self.minimax(board))
            return value
        else:
            positive_infinity = float('inf')
            value = positive_infinity
            for key, board in state.successors():
                value = min(value, self.minimax(board))
            return value


class MinimaxHeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.

        The depth data member (set in the constructor) determines the maximum depth of the game
        tree that gets explored before estimating the state utilities using the evaluation()
        function.  If depth is 0, no traversal is performed, and minimax returns the results of
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect4.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        #
        # Fill this in!
        #
        if self.depth_limit == 0:
            return self.evaluation(state)

        if self.depth_limit is None:
            return self.minimax(state)

        return self.depth_minimax(state, self.depth_limit)

    # if current_depth becomes greater than depth_limit, estimate the state utilities using the evaluation function
    # at terminal state, delegate to utility function
    def depth_minimax(self, state, current_depth):
        if state.is_full():
            return state.utility()
        elif current_depth <= 1:
            return self.evaluation(state)

        if state.next_player() == 1:
            negative_infinity = float('-inf')
            value = negative_infinity
            for key, board in state.successors():
                value = max(value, self.depth_minimax(board, current_depth - 1))
            return value
        else:
            positive_infinity = float('inf')
            value = positive_infinity
            for key, board in state.successors():
                value = min(value, self.depth_minimax(board, current_depth - 1))
            return value

    # count the number of possible 4 in rows that each player can still make and subtract that from each other.
    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in constant time for all states!

        Args:
            state: a connect4.GameState object representing the current board

        Returns: a heuristic estimate of the utility value of the state
        """
        #
        # Fill this in!
        #
        p1_score = 0
        p2_score = 0
        for run in state.get_rows() + state.get_cols() + state.get_diags():
            for elt, length in self.streaks2(run):
                if elt == 1 and length == 4:
                    p1_score += 1
                elif elt == -1 and length == 4:
                    p2_score += 1
        return p1_score - p2_score  # Change this line!

    def streaks2(self, lst):
        """Get the lengths of all the streaks of the same element in a sequence."""
        rets = []  # list of (element, length) tuples
        prev = lst[0]
        curr_len = 1
        for curr in lst[1:]:
            if curr == prev:
                curr_len += 1
            else:
                rets.append((prev, curr_len))
                prev = curr
                curr_len = 1
        rets.append((prev, curr_len))
        return rets


class MinimaxPruneAgent(MinimaxAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the
        algorithm should do less work.  You can check this by inspecting the value of the class
        variable GameState.state_count, which keeps track of how many GameState objects have been
        created over time.  This agent does not use a depth limit like MinimaxHeuristicAgent.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args:
            state: a connect4.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        #
        # Fill this in!
        #
        return self.alpha_beta_helper(state, float('-inf'), float('inf'))

    def alpha_beta_helper(self, state, alpha, beta):
        if state.is_full():
            return state.utility()
        if state.next_player() == 1:
            negative_infinity = float('-inf')
            value = negative_infinity
            for key, board in state.successors():
                value = max(value, self.alpha_beta_helper(board, alpha, beta))
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value
        else:
            positive_infinity = float('inf')
            value = positive_infinity
            for key, board in state.successors():
                value = min(value, self.alpha_beta_helper(board, alpha, beta))
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value


# N.B.: The following class is provided for convenience only; you do not need to implement it!

class OtherMinimaxHeuristicAgent(MinimaxAgent):
    """Alternative heursitic agent used for testing."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state."""
        #
        # Fill this in, if it pleases you.
        #
        return 26  # Change this line, unless you have something better to do.