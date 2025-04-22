from caro import Caro
import copy
import random

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

    def __init__(self, max_depth: int, XO: str, algorithm: str = 'minimax') -> None:
        '''
        Parameters
            ----------------
            max_depth: Maximum depth for the Minimax tree
            XO: 'X' or 'O', depend on the agent's turn
            algorithm: The algorithm to use ('minimax', 'greedy', 'ucs', 'genetic')
        '''
        self.max_depth = max_depth
        self.XO = XO
        self.algorithm = algorithm.lower()

        print(f"max_depth: {max_depth}; XO: {XO}; algorithm: {algorithm}")

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

    def get_move(self, game: Caro) -> list[list[int]]:
        '''
            Parameters
            ----------

            game: Caro object, represent current game state

            Return
            --------------
            The best move of the current position
        '''
        if len(game.last_move) < 1:
            possible_moves = game.get_possible_moves()
            move = random.choice(possible_moves)
            return move
        elif len(game.last_move) == 1:
            possible_moves = self.get_possible_moves_optimized(game)
            move = random.choice(possible_moves)
            return move

        best_score, best_move = self.minimax(
            game, self.max_depth, -INF * 10, INF * 10)

        return best_move
        
    def minimax(self, game: Caro, depth: int, alpha: int, beta: int, maximizing_player: int = 1) -> tuple[int, list[int]]:
        '''
            Implement the Minimax algorithm.

            Parameters
            ------------
            game: The Caro object, represent the current state of the game.

            depth: The current depth in minimax tree.

            alpha: maximum heuristic for alpha-beta pruning optimization.

            beta: minimum heuristic for alpha-beta pruning optimization.

            maximizing_player: 1 if we need to maximize heuristic, 0 otherwise.

            Return
            ------------
            The score of the best move and the best move coordinate.

        '''

        if depth == 0 or game.get_winner() != -1:
            return self.get_heuristic(game), None

        possible_moves = self.get_possible_moves_optimized(game)
        # possible_moves = game.get_possible_moves()

        if maximizing_player:
            max_eval = -INF
            best_move = possible_moves[0]

            for possible_move in possible_moves:
                x = possible_move[0]
                y = possible_move[1]

                new_game = copy.deepcopy(game)
                new_game.make_move(x, y)

                eval, move = self.minimax(new_game, depth - 1,
                                          alpha, beta, maximizing_player ^ 1)

                if eval > max_eval:
                    max_eval = eval
                    best_move = [x, y]

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = INF
            best_move = possible_moves[0]

            for possible_move in possible_moves:
                x = possible_move[0]
                y = possible_move[1]

                new_game = copy.deepcopy(game)
                new_game.make_move(x, y)

                eval, move = self.minimax(new_game, depth - 1,
                                          alpha, beta, maximizing_player ^ 1)

                if eval < min_eval:
                    min_eval = eval
                    best_move = [x, y]

                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

   
    
    def greedy(self, game: Caro) -> list[int]:
        possible_moves = self.get_possible_moves_optimized(game)
        best_move = None
        best_score = -INF
        
        for move in possible_moves:
            x, y = move
            game.grid[x][y] = self.XO
            score = self.get_heuristic(game)
            game.grid[x][y] = '.'  
            if score > best_score:
                best_score = score
                best_move = [x, y]
        
       
        if best_move is None:
            return [game.ROWNUM // 2, game.COLNUM // 2] 
        return best_move
    
    def genetic(self, game: Caro, population_size: int = 10, generations: int = 50, mutation_rate: float = 0.1) -> list[int]:
        '''
            Implement a genetic algorithm to find the best move.
            Parameters
            -----------
            game: The Caro object, representing the current state of the game.
            population_size: Number of individuals in the population.
            generations: Number of generations to evolve.
            mutation_rate: Probability of mutation.
            Return
            --------
            The best move coordinate.
        '''
        def initialize_population():
            return [random.choice(self.get_possible_moves_optimized(game)) for _ in range(population_size)]

        def fitness(move):
            x, y = move
            new_game = copy.deepcopy(game)
            new_game.make_move(x, y)
            return self.get_heuristic(new_game)

        def crossover(parent1, parent2):
            return random.choice([parent1, parent2])

        def mutate(move):
            if random.random() < mutation_rate:
                return random.choice(self.get_possible_moves_optimized(game))
            return move

        population = initialize_population()
        for _ in range(generations):
            population = sorted(population, key=fitness, reverse=True)
            next_generation = population[:population_size // 2]
            while len(next_generation) < population_size:
                parent1, parent2 = random.sample(next_generation, 2)
                child = crossover(parent1, parent2)
                child = mutate(child)
                next_generation.append(child)
            population = next_generation
        return max(population, key=fitness)
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

    agent = Agent(max_depth=2, XO='X')
    possible_moves = agent.get_possible_moves_optimized(game)
    print(f'possible_moves: {possible_moves}')
    best_move = agent.get_move(game)

    print(best_move)
    game.make_move(best_move[0], best_move[1])

    print(game.grid)
