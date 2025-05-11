import copy
from caro import Caro
import random
import math
import time
import heapq
import pickle  # Add for saving/loading Q-table
INF = 999999999999

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

def g(game: Caro, x: int, y: int) -> float:
    """
    Hàm tính chi phí thực tế g(x) cho bước đi (x, y) trong trò chơi Caro.
    Chi phí được tính dựa trên các yếu tố: độ sâu của trạng thái, nguy hiểm từ đối thủ, cơ hội chiến thắng của người chơi.
    """
    # Chi phí cơ bản cho mỗi bước đi
    base_cost = 1  
    
    # Chi phí độ sâu (số bước di chuyển đã thực hiện)
    depth_cost = game.current_turn  # Số bước đi đã thực hiện
    
    # Lấy đối thủ và người chơi hiện tại
    opponent = 'O' if game.XO == 'X' else 'X'  # Đối thủ là người chơi đối lập
    player = game.XO  # Người chơi hiện tại

    # Tính chi phí nguy hiểm từ đối thủ
    opponent_danger = 0
    for direction in range(8):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < game.rows and 0 <= ny < game.cols:
            if game.grid[nx][ny] == opponent:
                opponent_danger += 1  # Đối thủ có thể tạo chuỗi có thể thắng

    # Tính chi phí đối thủ (chi phí tăng khi đối thủ có thể chiến thắng)
    opponent_cost = opponent_danger * 2  # Chi phí cao hơn khi đối thủ có thể thắng

    # Tính chi phí cơ hội cho người chơi
    player_opportunity = 0
    for direction in range(8):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < game.rows and 0 <= ny < game.cols:
            if game.grid[nx][ny] == player:
                player_opportunity += 1  # Người chơi có thể tạo chuỗi chiến thắng

    # Tính chi phí người chơi (giảm chi phí khi người chơi có cơ hội chiến thắng)
    player_cost = -player_opportunity * 1.5  # Thưởng khi người chơi có cơ hội chiến thắng

    # Tổng chi phí thực tế
    total_cost = base_cost + depth_cost + opponent_cost + player_cost
    return total_cost




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
class UCS:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func=None) -> list[int]:
        print("Hello UCS:")

        possible_moves = get_possible_moves_optimized(game)
        if not possible_moves:
            return None

        pq = []  # priority queue: (total_cost, move)
        for move in possible_moves:
            x, y = move
            cost = g(game, x, y)
            heapq.heappush(pq, (cost, move))

        best_move = None
        min_cost = INF

        while pq:
            cost, move = heapq.heappop(pq)
            if cost < min_cost:
                min_cost = cost
                best_move = move

        return best_move

from collections import defaultdict

class QLearning:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.2, q_table_file="q_table.pkl"):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table_file = q_table_file
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.load_q_table()

    def load_q_table(self):
        try:
            with open(self.q_table_file, "rb") as file:
                raw_q_table = pickle.load(file)
                self.q_table = defaultdict(lambda: defaultdict(float),
                                           {k: defaultdict(float, v) for k, v in raw_q_table.items()})
        except FileNotFoundError:
            self.q_table = defaultdict(lambda: defaultdict(float))

    def save_q_table(self):
        with open(self.q_table_file, "wb") as file:
            q_table_dict = {k: dict(v) for k, v in self.q_table.items()}
            pickle.dump(q_table_dict, file)

    def get_state_key(self, game: 'Caro'):
        return str(game.grid)

    def get_best_action(self, game: 'Caro'):
        state_key = self.get_state_key(game)
        possible_moves = get_possible_moves_optimized(game)
        if not possible_moves:
            return None
        if random.random() < self.epsilon or state_key not in self.q_table:
            return random.choice(possible_moves)
        return max(self.q_table[state_key], key=self.q_table[state_key].get)

    def update_q_value(self, game: 'Caro', move, reward, next_game: 'Caro'):
        state_key = self.get_state_key(game)
        next_state_key = self.get_state_key(next_game)
        move = tuple(move)

        max_next_q = max(self.q_table[next_state_key].values(), default=0.0)
        td_target = reward + self.gamma * max_next_q
        td_error = td_target - self.q_table[state_key][move]
        self.q_table[state_key][move] += self.alpha * td_error

    @staticmethod
    def get_best_move(game: 'Caro', q_learning_agent):
        return q_learning_agent.get_best_action(game)
    
class Backtracking:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func, max_depth=3) -> list[int]:
        print("Hello Backtracking:")

        def backtrack(current_game: Caro, depth: int, is_ai_turn: bool):
            # Replace is_game_over with get_winner
            if depth == 0 or current_game.get_winner() != -1:  # Check if the game has ended
                return heuristic_func(current_game), None

            possible_moves = get_possible_moves_optimized(current_game)
            if not possible_moves:
                return heuristic_func(current_game), None

            best_score = -INF if is_ai_turn else INF
            best_move = None

            for move in possible_moves:
                x, y = move
                new_game = copy.deepcopy(current_game)
                new_game.make_move(x, y)

                score, _ = backtrack(new_game, depth - 1, not is_ai_turn)

                if is_ai_turn:
                    if score > best_score:
                        best_score = score
                        best_move = move
                else:
                    if score < best_score:
                        best_score = score
                        best_move = move

            return best_score, best_move

        _, move = backtrack(game, max_depth, True)
        return move
class AndOr:
    @staticmethod
    def get_best_move(game: Caro, heuristic_func, max_depth=3) -> list[int]:
        def and_or_search(game: Caro, depth: int, is_ai_turn: bool):
            if depth == 0 or game.get_winner() != -1:
                return heuristic_func(game), None

            possible_moves = get_possible_moves_optimized(game)
            if not possible_moves:
                return heuristic_func(game), None

            if is_ai_turn:
                # OR node: chọn 1 nước đi tốt nhất
                best_score = -float('inf')
                best_move = None
                for move in possible_moves:
                    new_game = copy.deepcopy(game)
                    new_game.make_move(*move)
                    score, _ = and_or_search(new_game, depth - 1, False)  # Đến lượt đối thủ
                    if score > best_score:
                        best_score = score
                        best_move = move
                return best_score, best_move
            else:
                # AND node: đối thủ có thể đi bất kỳ đâu → AI phải chuẩn bị cho mọi trường hợp
                worst_score = float('inf')
                for move in possible_moves:
                    new_game = copy.deepcopy(game)
                    new_game.make_move(*move)
                    score, _ = and_or_search(new_game, depth - 1, True)  # Đến lượt AI lại
                    if score < worst_score:
                        worst_score = score
                return worst_score, None  # Không cần move vì AI không đi trong lượt này

        _, move = and_or_search(game, max_depth, True)
        return move