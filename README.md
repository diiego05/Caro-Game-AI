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
  - Hình ảnh menu
![Hình ảnh menu](https://i.imgur.com/tlb2S7I.png)

  - Hình ảnh giao diện game
  
- **Cài đặt tùy chỉnh**:
  - Điều chỉnh độ khó AI (Dễ, Trung bình, Khó)
  - Lựa chọn lượt đi đầu (AI hoặc Người chơi)
![Hình ảnh cài đặt](https://i.imgur.com/GmR4itz.png)


- **Trực quan hóa**:
  - Biểu đồ tròn hiển thị tỉ lệ thắng thua giữa các thuật toán AI
  - So sánh hiệu suất giữa các thuật toán


## Hưỡng dẫn chơi

1. **Khởi động trò chơi**: Chạy file `main.py`
2. **Chọn chế độ chơi**: Người vs AI, Người vs Người hoặc AI vs AI
3. **Chọn cấp độ AI** (chơi với máy): Dễ, Trung bình, Khó
4. **Luật chơi**: 
   - Người chơi đánh dấu X và O luân phiên nhau
   - Người thắng cuộc là người đầu tiên tạo được một hàng liên tiếp 5 quân (ngang, dọc hoặc chéo)

## Cấu trúc dự án

```
caro-ai-game/
├── assets/
├── agent.py
├── algorithm.py  
├── Buttons.py
└── caro.py
└── main.py
└── settings.py
└── menu.py            
```





