import copy
from caro import Caro
import random

INF = 999999999999

class Minimax:
     @staticmethod
     def minimax(game: Caro, depth: int, alpha: int, beta: int, maximizing_player: int, heuristic_func) -> tuple[int, list[int]]:
        '''
        Implement the Minimax algorithm with Alpha-Beta pruning.

        Parameters:
        -----------
        game: The Caro object, representing the current state of the game.
        depth: The current depth in the minimax tree.
        alpha: Maximum heuristic for alpha-beta pruning optimization.
        beta: Minimum heuristic for alpha-beta pruning optimization.
        maximizing_player: 1 if we need to maximize heuristic, 0 otherwise.
        heuristic_func: Function to calculate the heuristic value of the game state.

        Returns:
        --------
        The score of the best move and the best move coordinate.
        '''
        if depth == 0 or game.get_winner() != -1:
            return heuristic_func(game), None

        possible_moves = Minimax.get_possible_moves_optimized(game)

        if maximizing_player:
            max_eval = -INF
            best_move = possible_moves[0]

            for move in possible_moves:
                x, y = move
                new_game = copy.deepcopy(game)
                new_game.make_move(x, y)

                eval, _ = Minimax.minimax(new_game, depth - 1, alpha, beta, 0, heuristic_func)

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

            for move in possible_moves:
                x, y = move
                new_game = copy.deepcopy(game)
                new_game.make_move(x, y)

                eval, _ = Minimax.minimax(new_game, depth - 1, alpha, beta, 1, heuristic_func)

                if eval < min_eval:
                    min_eval = eval
                    best_move = [x, y]

                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
   

     @staticmethod
     def get_possible_moves_optimized(game: Caro) -> list[list[int]]:
        '''
        Get possible moves near existing pieces to optimize the search space.

        Parameters:
        -----------
        game: The Caro object, representing the current state of the game.

        Returns:
        --------
        A list of possible moves.
        '''
        dx = [1, 1, 1, -1, -1, -1, 0, 0]
        dy = [1, -1, 0, 1, -1, 0, 1, -1]
        visited = [[0 for _ in range(game.cols)] for _ in range(game.rows)]
        result = []

        for x in range(game.rows):
            for y in range(game.cols):
                if game.grid[x][y] == '.':
                    continue
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < game.rows and 0 <= ny < game.cols and game.grid[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        result.append([nx, ny])

        return result

class Greedy:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func) -> list[int]:
        '''
        Implement a greedy algorithm to select the best move based on heuristic evaluation.

        Parameters:
        -----------
        game: The Caro object, representing the current state of the game.
        heuristic_func: Function to calculate the heuristic value of the game state.

        Returns:
        --------
        The best move coordinate.
        '''
        possible_moves = Minimax.get_possible_moves_optimized(game)
        best_move = None
        best_score = -INF

        for move in possible_moves:
            x, y = move
            new_game = copy.deepcopy(game)
            new_game.make_move(x, y)

            score = heuristic_func(new_game)
            if score > best_score:
                best_score = score
                best_move = [x, y]

        return best_move

class UCS:
    @staticmethod
    def get_best_move(game: Caro, cost_func) -> list[int]:
        '''
        Implement Uniform Cost Search (UCS) to find the best move based on cost evaluation.

        Parameters:
        -----------
        game: The Caro object, representing the current state of the game.
        cost_func: Function to calculate the cost of the game state.

        Returns:
        --------
        The best move coordinate.
        '''
        from queue import PriorityQueue

        possible_moves = Minimax.get_possible_moves_optimized(game)
        pq = PriorityQueue()

        for move in possible_moves:
            x, y = move
            new_game = copy.deepcopy(game)
            new_game.make_move(x, y)
            cost = cost_func(new_game)
            pq.put((cost, [x, y]))

        # UCS selects the move with the lowest cost
        _, best_move = pq.get()
        return best_move

class GeneticAlgorithm:
    @staticmethod
    def get_best_move(game, heuristic_func, population_size=10, generations=50, mutation_rate=0.1):
        '''
        Implement a genetic algorithm to find the best move.

        Parameters:
        -----------
        game: The Caro object, representing the current state of the game.
        heuristic_func: Function to calculate the heuristic value of the game state.
        population_size: Number of individuals in the population.
        generations: Number of generations to evolve.
        mutation_rate: Probability of mutation.

        Returns:
        --------
        The best move coordinate.
        '''
        def initialize_population():
            return [random.choice(Minimax.get_possible_moves_optimized(game)) for _ in range(population_size)]

        def fitness(move):
            x, y = move
            new_game = copy.deepcopy(game)
            new_game.make_move(x, y)
            return heuristic_func(new_game)

        def crossover(parent1, parent2):
            return random.choice([parent1, parent2])

        def mutate(move):
            if random.random() < mutation_rate:
                return random.choice(Minimax.get_possible_moves_optimized(game))
            return move

        # Initialize population
        population = initialize_population()

        for _ in range(generations):
            # Evaluate fitness
            population = sorted(population, key=fitness, reverse=True)

            # Select top individuals
            next_generation = population[:population_size // 2]

            # Crossover and mutation
            while len(next_generation) < population_size:
                parent1, parent2 = random.sample(next_generation, 2)
                child = crossover(parent1, parent2)
                child = mutate(child)
                next_generation.append(child)

            population = next_generation

        # Return the best move
        return max(population, key=fitness)