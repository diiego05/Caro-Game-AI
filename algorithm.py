import copy
from caro import Caro
import random
import math
import time
INF = 999999999999

def get_possible_moves_optimized(game: Caro) -> list[list[int]]:
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

class Minimax:
    @staticmethod
    def minimax(game: Caro, depth: int, alpha: int, beta: int, maximizing_player: int, heuristic_func) -> tuple[int, list[int]]:
        print("Hello:ok")
        if depth == 0 or game.get_winner() != -1:
            return heuristic_func(game), None

        possible_moves = get_possible_moves_optimized(game)

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

class Greedy:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func) -> list[int]:
        print("Hello Greedy:")
        possible_moves = get_possible_moves_optimized(game)
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



class GeneticAlgorithm:
    @staticmethod
    def get_best_move(game, heuristic_func, population_size=10, generations=50, mutation_rate=0.1):
        def initialize_population():
            moves = get_possible_moves_optimized(game)
            return random.sample(moves, min(population_size, len(moves)))

        def fitness(move):
            x, y = move
            new_game = copy.deepcopy(game)
            new_game.make_move(x, y)
            return heuristic_func(new_game)  # Nếu càng cao càng tốt

        def crossover(parent1, parent2):
            # Ưu tiên chọn move nào có fitness cao hơn
            return parent1 if fitness(parent1) >= fitness(parent2) else parent2

        def mutate(move, all_moves):
            if random.random() < mutation_rate:
                other_moves = [m for m in all_moves if m != move]
                if other_moves:
                    return random.choice(other_moves)
            return move

        print("Hello Genetic:")
        population = initialize_population()

        for _ in range(generations):
            all_moves = get_possible_moves_optimized(game)

            # Đánh giá và sắp xếp
            population = sorted(population, key=fitness, reverse=True)

            # Elitism: giữ lại move tốt nhất
            next_generation = population[:1]

            # Chọn top 50% để lai
            selected = population[:max(2, population_size // 2)]

            # Sinh thế hệ mới
            while len(next_generation) < population_size:
                parent1, parent2 = random.sample(selected, 2)
                child = crossover(parent1, parent2)
                child = mutate(child, all_moves)
                next_generation.append(child)

            population = next_generation

        return max(population, key=fitness)
    
class SimulatedAnnealing:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func, initial_temp=100.0, cooling_rate=0.95, time_limit=1.0):
        print("Hello SA:")
        possible_moves = get_possible_moves_optimized(game)
        if not possible_moves:
            return None

        # Khởi tạo lời giải ban đầu
        current_move = random.choice(possible_moves)
        best_move = current_move
        current_score = heuristic_func(SimulatedAnnealing.simulate_move(game, current_move))
        best_score = current_score

        temp = initial_temp
        start_time = time.time()

        while time.time() - start_time < time_limit and temp > 1e-3:
            next_move = random.choice(possible_moves)
            next_score = heuristic_func(SimulatedAnnealing.simulate_move(game, next_move))

            delta = next_score - current_score
            if delta > 0 or random.random() < math.exp(delta / temp):
                current_move = next_move
                current_score = next_score

                if current_score > best_score:
                    best_score = current_score
                    best_move = current_move

            temp *= cooling_rate

        return best_move

    @staticmethod
    def simulate_move(game: Caro, move: list[int]) -> Caro:
        x, y = move
        new_game = copy.deepcopy(game)
        new_game.make_move(x, y)
        return new_game
    
class StochasticHillClimbing:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func) -> list[int]:
        print("Hello Stochastic Hill Climbing:")

        possible_moves = get_possible_moves_optimized(game)
        if not possible_moves:
            return None
        
        # Khởi tạo lời giải ban đầu ngẫu nhiên
        current_move = random.choice(possible_moves)
        best_move = current_move
        current_score = heuristic_func(SimulatedAnnealing.simulate_move(game, current_move))
        best_score = current_score

        while True:
            # Tạo danh sách các bước đi kế tiếp (neighbors)
            neighbors = get_possible_moves_optimized(game)
            neighbors.remove(current_move)  # Loại bỏ bước đi hiện tại
            
            if not neighbors:
                break  # Dừng lại nếu không còn bước đi nào để chọn

            # Chọn ngẫu nhiên một bước đi trong các neighbors
            next_move = random.choice(neighbors)
            next_score = heuristic_func(SimulatedAnnealing.simulate_move(game, next_move))

            # Nếu bước đi tiếp theo tốt hơn, cập nhật
            if next_score > current_score:
                current_move = next_move
                current_score = next_score

                if current_score > best_score:
                    best_score = current_score
                    best_move = current_move
            else:
                break  # Dừng lại nếu không có bước đi nào cải thiện

        return best_move
    
