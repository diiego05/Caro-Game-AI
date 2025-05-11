from caro import Caro
import copy
import random
from algorithm import Greedy, GeneticAlgorithm, SimulatedAnnealing, StochasticHillClimbing, UCS, QLearning, Backtracking, AndOr
TWO = 10
TWO_OBSTACLE = 5
THREE = 1000
THREE_OBSTACLE = 500
FOUR = 30000000
FOUR_OBSTACLE = 2000000
WINNING = 2000000000

TWO_OPPONENT = -20
TWO_OBSTACLE_OPPONENT = -3
THREE_OPPONENT = -2000
THREE_OBSTACLE_OPPONENT = -750
FOUR_OPPONENT = -40000000
FOUR_OBSTACLE_OPPONENT = -5000000
LOSING = -1000000000

INF = 999999999999

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]


class Agent:

    def __init__(self, XO: str, algorithm: str = 'greedy') -> None:
        '''
        Parameters
            ----------------
            XO: 'X' or 'O', depend on the agent's turn
            algorithm: The algorithm to use ('greedy', 'genetic', 'sa', 'stochastic', 'bfs')
        '''
        self.XO = XO
        self.algorithm = algorithm.lower()

        print(f"XO: {XO}; algorithm: {algorithm}")

        if self.algorithm == 'qlearning':
            self.q_learning_agent = QLearning()  # Initialize QLearning agent
        else:
            self.q_learning_agent = None

    def get_possible_moves_optimized(self, game: Caro) -> list[list[int]]:
        visited = [[0 for _ in range(game.cols)] for _ in range(game.rows)]
        result = []
        for x in range(game.rows):
            for y in range(game.cols):
                if game.grid[x][y] == '.':
                    continue
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx >= 0 and ny >= 0 and nx < game.rows and ny < game.cols and game.grid[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        result.append([nx, ny])

        return result

    def compute(self, sequences: list[list[str]]) -> int:
        '''
            Parameters
            ----------------
            sequences: consecutive cells from the board (rows, columns or diagonals)

            current: 'X' or 'O', depend on current player move

            Return
            ---------------- 
            Heuristic with the given sequences

        '''

        result = 0

        for sequence in sequences:
            player = 0
            opponent = 0
            obstacle = 1
            obstacle_player = 0
            obstacle_opponent = 0
            for c in sequence:
                if c == self.XO:
                    player += 1

                    if opponent != 0:
                        if opponent == 2 and obstacle_player == 0 and obstacle == 0:
                            result += TWO_OBSTACLE_OPPONENT
                        elif opponent == 3 and obstacle_player == 0 and obstacle == 0:
                            result += THREE_OBSTACLE_OPPONENT
                        elif opponent == 4 and obstacle_player == 0 and obstacle == 0:
                            result += FOUR_OBSTACLE_OPPONENT
                        elif opponent == 5:
                            result += LOSING

                    opponent = 0
                    obstacle_player = 1
                    # obstacle = 0

                elif c != '.':
                    opponent += 1

                    if player != 0:
                        if player == 2 and obstacle_opponent == 0 and obstacle == 0:
                            result += TWO_OBSTACLE
                        elif player == 3 and obstacle_opponent == 0 and obstacle == 0:
                            result += THREE_OBSTACLE
                        elif player == 4 and obstacle_opponent == 0 and obstacle == 0:
                            result += FOUR_OBSTACLE
                        elif player == 5:
                            result += WINNING

                    player = 0
                    # obstacle = 0
                    obstacle_opponent = 1

                else:
                    if player != 0:
                        if player == 2:
                            if obstacle_opponent == 1 or obstacle == 1:
                                result += TWO_OBSTACLE
                            else:
                                result += TWO
                        elif player == 3:
                            if obstacle_opponent == 1 or obstacle == 1:
                                result += THREE_OBSTACLE
                            else:
                                result += THREE
                        elif player == 4:
                            if obstacle_opponent == 1 or obstacle == 1:
                                result += FOUR_OBSTACLE
                            else:
                                result += FOUR
                        elif player == 5:
                            result += WINNING
                    player = 0

                    if opponent != 0:
                        if opponent == 2:
                            if obstacle_player == 1 or obstacle == 1:
                                result += TWO_OBSTACLE_OPPONENT
                            else:
                                result += TWO_OPPONENT
                        elif opponent == 3:
                            if obstacle_player == 1 or obstacle == 1:
                                result += THREE_OBSTACLE_OPPONENT
                            else:
                                result += THREE_OPPONENT
                        elif opponent == 4:
                            if obstacle_player == 1 or obstacle == 1:
                                result += FOUR_OBSTACLE_OPPONENT
                            else:
                                result += FOUR_OPPONENT
                        elif opponent == 5:
                            result += LOSING

                        opponent = 0

                    obstacle = 0
                    obstacle_player = 0
                    obstacle_opponent = 0

            if opponent != 0:
                if opponent == 2 and obstacle_player == 0 and obstacle == 0:
                    result += TWO_OBSTACLE_OPPONENT
                elif opponent == 3 and obstacle_player == 0 and obstacle == 0:
                    result += THREE_OBSTACLE_OPPONENT
                elif opponent == 4 and obstacle_player == 0 and obstacle == 0:
                    result += FOUR_OBSTACLE_OPPONENT
                elif opponent == 5:
                    result += LOSING

            if player != 0:
                if player == 2 and obstacle_opponent == 0 and obstacle == 0:
                    result += TWO_OBSTACLE
                elif player == 3 and obstacle_opponent == 0 and obstacle == 0:
                    result += THREE_OBSTACLE
                elif player == 4 and obstacle_opponent == 0 and obstacle == 0:
                    result += FOUR_OBSTACLE
                elif player == 5:
                    result += WINNING

        return result

    def get_heuristic(self, game: Caro) -> int:
        '''
            Parameters
            ----------

            game: Caro object, represent current game state

            Return
            --------------
            The heuristic corresponding to the current board and current player.
        '''

        return self.compute(game.get_all_rows()) + self.compute(game.get_all_diagonals()) + self.compute(game.get_all_colummns())

    def get_move(self, game: Caro) -> list[int]:
        if len(game.last_move) < 1:
            possible_moves = game.get_possible_moves()
            return random.choice(possible_moves)
        elif len(game.last_move) == 1:
            possible_moves = self.get_possible_moves_optimized(game)
            return random.choice(possible_moves)

        if self.algorithm == 'greedy':
            return Greedy.get_best_move(game, self.get_heuristic)

        elif self.algorithm == 'genetic':
            return GeneticAlgorithm.get_best_move(game, self.get_heuristic)
        elif self.algorithm == 'sa':
            return SimulatedAnnealing.get_best_move(game, self.get_heuristic)
        elif self.algorithm == 'stochastic':
            return StochasticHillClimbing.get_best_move(game, self.get_heuristic)
        elif self.algorithm == 'ucs':
            return UCS.get_best_move(game, self.get_heuristic)
        elif self.algorithm == 'qlearning':
            return QLearning.get_best_move(game, self.q_learning_agent)
        elif self.algorithm == 'backtracking':
            return Backtracking.get_best_move(game, self.get_heuristic)
        elif self.algorithm == 'andor':
                 return AndOr.get_best_move(game, self.get_heuristic)
        else:
            raise ValueError(f"Unknown algorithm: {self.algorithm}")

   
  
    
  
# Testing

if __name__ == '__main__':
    game = Caro(rows=5, cols=5)
    game.grid = [
        ['.', '.', '.', '.', '.'],
        ['.', '.', 'O', '.', '.'],
        ['.', '.', 'O', '.', '.'],
        ['.', '.', 'O', '.', '.'],
        ['.', '.', '.', '.', '.'],
    ]

    agent = Agent(XO='X')
    possible_moves = agent.get_possible_moves_optimized(game)
    print(f'possible_moves: {possible_moves}')
    best_move = agent.get_move(game)

    print(best_move)
    game.make_move(best_move[0], best_move[1])

    print(game.grid)
