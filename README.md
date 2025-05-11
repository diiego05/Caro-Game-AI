# Game Caro AI - Nhóm 15

## Giới thiệu

Game Caro AI là một dự án của nhóm 15 triển khai trò chơi cờ caro kết hợp với trí tuệ nhân tạo.Người chơi có thể thi đấu với máy ở nhiều cấp độ khó khác nhau, từ dễ đến khó, hoặc với người chơi khác, hoặc có thể là cho máy đáu với máy.Dự án hỗ trợ trực quan hóa hiệu suất AI thông qua biểu đồ tỷ lệ thắng, giúp người dùng phân tích và so sánh các thuật toán.

## Tính năng - Giao diện

- **Chế độ chơi đa dạng**:
  - Người vs AI (nhiều cấp độ)
  - Người vs Người (cùng máy tính)
  - Ai vs Ai (tụ do chọn thuật toán)

- **Trí tuệ nhân tạo thông minh**:
  - Dùng nhiều thuật toán AI đa dạng: 
    + Genetic Algorithm
    + Simulated Annealing
    + Stochastic Hill Climbing
    + Uniform Cost Search
    + Backtracking
    + And-Or Search
    + Q-Learning

- **Giao diện người dùng thân thiện**:
![Hình ảnh menu](https://i.imgur.com/tlb2S7I.png)
  
- **Cài đặt tùy chỉnh**:
  - Điều chỉnh độ khó AI (Dễ, Trung bình, Khó)
  - Lựa chọn lượt đi đầu (AI hoặc Người chơi)
![Hình ảnh cài đặt](https://i.imgur.com/GmR4itz.png)


- **Trực quan hóa**:
  - Biểu đồ tròn hiển thị tỉ lệ thắng thua giữa các thuật toán AI
  - So sánh hiệu suất giữa các thuật toán

## Yêu cầu hệ thống
- Python 3.7+
- NumPy
- PyTorch (cho phiên bản AI sử dụng deep learning)
- Pygame (cho giao diện đồ họa)

## Cài đặt

```bash
# Chạy game
python main.py
```

## Cách chơi

1. **Khởi động trò chơi**: Chạy file `main.py`
2. **Chọn chế độ chơi**: Người vs AI hoặc Người vs Người
3. **Chọn cấp độ AI** (nếu chơi với máy): Dễ, Trung bình, Khó, Chuyên gia
4. **Luật chơi**: 
   - Người chơi đánh dấu X và O luân phiên nhau
   - Người chơi đầu tiên sử dụng X
   - Người thắng cuộc là người đầu tiên tạo được một hàng liên tiếp 5 quân (ngang, dọc hoặc chéo)

## Cấu trúc dự án

```
caro-ai-game/
├── main.py
|
├── ai.py
│   
├── assets/
│     
├── Buttons.py
│   
└── agent.py
│ 
└── settings.py
│   
└── menu.py            
```

## Thuật toán AI

Game Caro AI sử dụng nhiều thuật toán AI tiên tiến để cung cấp trải nghiệm chơi thách thức:

### Thuật toán Minimax với cắt tỉa Alpha-Beta
- Tìm kiếm nước đi tối ưu bằng cách đánh giá các trạng thái tương lai
- Cắt tỉa Alpha-Beta giúp tăng tốc độ tìm kiếm
- Độ sâu tìm kiếm thay đổi theo cấp độ khó

### Monte Carlo Tree Search (MCTS)
- Mô phỏng hàng nghìn ván đấu để đánh giá chất lượng nước đi
- Cân bằng giữa khám phá và khai thác
- Hiệu quả với không gian trạng thái lớn

### Đánh giá bàn cờ
- Phân tích mẫu (patterns) trên bàn cờ
- Đánh giá vị trí chiến lược và tiềm năng tấn công/phòng thủ
- Học từ dữ liệu ván đấu trước đó




