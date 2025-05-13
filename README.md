# Game Caro AI - Nhóm 15

## Giới thiệu

Game Caro AI là một dự án của nhóm 15 triển khai trò chơi cờ caro kết hợp với trí tuệ nhân tạo.Người chơi có thể thi đấu với máy ở nhiều cấp độ khó khác nhau, từ dễ đến khó, hoặc với người chơi khác, hoặc có thể là cho máy đáu với máy.Dự án hỗ trợ trực quan hóa hiệu suất AI thông qua biểu đồ tỷ lệ thắng, giúp người dùng phân tích và so sánh các thuật toán.

## Tính năng - Giao diện

- **Chế độ chơi đa dạng**:
  - Người vs AI (nhiều cấp độ)
  - Người vs Người (cùng máy tính)
  - Ai vs Ai (tự do chọn thuật toán)

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
  - Điều chỉnh độ khó AI (Dễ, Trung bình, Khó)
  - Lựa chọn lượt đi đầu (AI hoặc Người chơi)
  
  - ![Giao diện menu](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzZ1djk4ejkxZjJtZms5bzFuZnBuZHRsaXV0aGtzcnV1cmZrZ3ppMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bKhSNCiacGIipyIY9f/giphy.gif)

  - Chế độ chơi: Người vs Người
  - ![Người vs Người](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYW12OHM1cXh6OXN3cTBtM2ptdDMxcmQ0b28zdHlndnF1Y2w3dXJzaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iATf6JY9q5srhFi39r/giphy.gif)

  - Chế độ chơi: Người vs AI
  - ![Người vs AI](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmZndGJhNXl6bDFzeTVxYjluamU3eXFteHZjZDNoaHB0OXlsbWFobSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1q23tkZhpdGtBucVuf/giphy.gif)
 
  - Chế độ chơi: AI vs AI (chọn nhiều thuật toán khác nhau cho 2 AI, dưới đây là chọn 2 thuật toán Greedy và Simulated Annealing)
  - ![AI vs AI](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXk3MTh4cDR0bzUzNWU1YTQ5Y2xlaGNzMWg4ZjludDMwaDR1N3N2eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NuJkH84UgzmfzQcGH3/giphy.gif)

- **Trực quan hóa**:
  - Biểu đồ tròn hiển thị tỉ lệ thắng thua giữa các thuật toán AI
  - So sánh hiệu suất giữa các thuật toán
  ![Hiệu suất thuật toán](https://github.com/user-attachments/assets/c4d401bd-5deb-4d33-af45-99055e1bd841)


## Hưỡng dẫn chơi

1. **Khởi động trò chơi**: Chạy file `main.py`
2. **Chọn cấp độ AI** (chơi với máy): Dễ, Trung bình, Khó
3. **Chọn chế độ chơi**: Người vs AI, Người vs Người hoặc AI vs AI
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

## Đội ngũ phát triển

**Nhóm 14 - Trí Tuệ Nhân Tạo**

**Thành viên**:
  - Nguyễn Duy Cường - 23110189
  - Nguyễn Thành Tin - 23110340
  - Lâm Văn Dỉ - 23110191





