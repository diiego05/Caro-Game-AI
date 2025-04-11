# Game Caro AI

## Giới thiệu

Game Caro AI là một dự án triển khai trò chơi cờ caro (Gomoku/Tic-tac-toe mở rộng) kết hợp với trí tuệ nhân tạo. Người chơi có thể thi đấu với máy ở nhiều cấp độ khó khác nhau, từ dễ đến khó, hoặc với người chơi khác.

## Tính năng

- **Chế độ chơi đa dạng**:
  - Người vs AI (nhiều cấp độ)
  - Người vs Người (cùng máy tính)
  - Chế độ trực tuyến (đấu với người chơi khác)

- **Trí tuệ nhân tạo thông minh**:
  - Sử dụng thuật toán Minimax với cắt tỉa Alpha-Beta
  - Hỗ trợ thuật toán Monte Carlo Tree Search (MCTS)
  - AI tự học và thích nghi qua các ván đấu

- **Bàn cờ tùy chỉnh**:
  - Kích thước bàn cờ linh hoạt (15x15, 19x19, tùy chỉnh)
  - Luật chơi đa dạng (cờ caro thông thường, luật Gomoku quốc tế)

- **Tính năng bổ sung**:
  - Lưu và tải ván đấu
  - Phát lại các nước đi
  - Thống kê và xếp hạng
  - Gợi ý nước đi tốt nhất

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

## Đóng góp

Chúng tôi luôn chào đón đóng góp từ cộng đồng! Nếu bạn muốn cải thiện Game Caro AI:

1. Fork repository
2. Tạo nhánh tính năng mới (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi của bạn (`git commit -m 'Add some amazing feature'`)
4. Push lên nhánh của bạn (`git push origin feature/amazing-feature`)
5. Mở Pull Request

## Giấy phép

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## Liên hệ

Tên của bạn - [@twitter_handle](https://twitter.com/twitter_handle) - email@example.com

Project Link: [https://github.com/username/caro-ai-game](https://github.com/username/caro-ai-game)
