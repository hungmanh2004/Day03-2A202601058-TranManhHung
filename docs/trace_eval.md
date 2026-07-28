# 📊 BÁO CÁO GIÁM SÁT & ĐÁNH GIÁ (OBSERVABILITY TRACE LOGS)
*Dành cho Role 5: Observability & Reviewer*

---

## 🎯 1. BẢNG CHẤM ĐIỂM AGENTIC FIT (SCORING MATRIX)

**Đề tài:** Chatbot Định Hướng Sự Nghiệp cho học sinh/sinh viên

| Tiêu chí | Điểm (1-5) | Lý do đánh giá |
| :--- | :---: | :--- |
| 🧠 **Multi-step Reasoning** | `5/5` | Người dùng thường cần cung cấp nhiều thông tin như sở thích, năng lực, mục tiêu, điều kiện học tập và tài chính, rồi mới có thể đề xuất hướng đi phù hợp. |
| 🛠️ **Tool Interaction** | `4/5` | Có thể cần dùng công cụ tra cứu ngành nghề, khóa học, thị trường việc làm hoặc dữ liệu nghề nghiệp để đưa ra gợi ý sát thực tế. |
| 🔀 **Dynamic Decision** | `5/5` | Mỗi câu trả lời của người dùng sẽ ảnh hưởng đến câu hỏi tiếp theo, cách tư vấn và loại đề xuất phù hợp. |
| ⏳ **Long Horizon** | `4/5` | Quy trình tư vấn thường gồm nhiều bước: hiểu nhu cầu → phân tích → đề xuất nghề/khóa học → gợi ý hành động tiếp theo. |
| **TỔNG ĐIỂM FIT** | **18/20** | **KẾT LUẬN: BÀI TOÁN RẤT NÊN DÙNG REACT AGENT!** |

---

## 💡 Nhận xét chung

Chatbot định hướng sự nghiệp phù hợp với mô hình Agent vì nó không chỉ trả lời đơn thuần mà còn cần:
- suy luận nhiều bước,
- tương tác với công cụ hoặc dữ liệu thực tế,
- điều chỉnh quyết định theo phản hồi của người dùng.

Ví dụ: khi người dùng nói “Tôi thích toán nhưng cũng thích sáng tạo, muốn làm việc gần công nghệ”, Agent cần hỏi thêm, phân tích và đề xuất nghề phù hợp thay vì chỉ đưa câu trả lời chung chung.

---

## ⚠️ 2. FAILURE MODES & PHƯƠNG ÁN PHÒNG VỆ (ROLE 3)

Các trường hợp lỗi dưới đây được xác định dựa trên luồng khảo sát và danh sách công cụ hiện có trong `src/tools.py`.

| Failure mode | Biểu hiện có thể xảy ra | Tool liên quan | Phương án phòng vệ trong Prompt/Guardrail |
| :--- | :--- | :--- | :--- |
| **Thiếu thông tin khảo sát** | Agent đưa ra định hướng nghề nghiệp khi người dùng chưa trả lời đủ 5 câu hỏi. | `is_survey_completed`, `build_career_profile` | Chỉ tạo hồ sơ và tư vấn khi khảo sát hoàn tất; nếu chưa đủ, gọi `get_next_question` để hỏi tiếp. |
| **Chỉ số câu hỏi không hợp lệ** | Agent truyền chỉ số ngoài khoảng 1–5 hoặc truyền sai kiểu dữ liệu. | `get_question`, `validate_answer`, `save_answer` | Không tự đoán câu hỏi; đọc thông báo lỗi, dùng đúng chỉ số được trả về bởi hệ thống và không lặp lại Action sai. |
| **Câu trả lời rỗng hoặc ngoài lựa chọn** | Người dùng bỏ trống hoặc nhập đáp án không thuộc danh sách cho phép. | `validate_answer` | Không lưu đáp án sai; giải thích ngắn gọn và yêu cầu người dùng chọn lại một trong các phương án hợp lệ. |
| **State sai hoặc bị thiếu** | Trạng thái khảo sát không phải dictionary, thiếu `answers` hoặc có cấu trúc không hợp lệ. | `save_answer`, `is_survey_completed`, `build_career_profile`, `get_next_question` | Không tự tạo dữ liệu khảo sát; khởi tạo lại bằng `reset_survey` hoặc `start_career_survey`, sau đó thông báo cho người dùng. |
| **Ghi đè hoặc lưu trùng đáp án** | Agent gọi `save_answer` nhiều lần cho cùng một câu hỏi, làm thay đổi lựa chọn trước đó ngoài ý muốn. | `save_answer` | Chỉ lưu sau khi `validate_answer` trả về hợp lệ; nếu sửa đáp án cũ, phải xác nhận rõ ý định của người dùng. |
| **Gọi tool sai thứ tự** | Agent tạo hồ sơ trước khi kiểm tra khảo sát hoàn tất hoặc lưu câu trả lời trước khi kiểm tra tính hợp lệ. | Toàn bộ tool khảo sát | Tuân thủ luồng: khởi tạo → lấy câu hỏi → kiểm tra đáp án → lưu đáp án → kiểm tra hoàn tất → tạo hồ sơ. |
| **Gọi tool không tồn tại hoặc sai tham số** | Agent tự tạo tên tool, thiếu tham số hoặc truyền sai thứ tự tham số. | `AVAILABLE_TOOLS` | Chỉ gọi đúng tool đã đăng ký và đúng schema; khi chưa đủ tham số, hỏi lại người dùng thay vì tự suy đoán. |
| **Repeated Action** | Agent gọi lại cùng một tool với cùng tham số dù kết quả không thay đổi hoặc đã báo lỗi. | Toàn bộ tool khảo sát | Theo dõi Action đã thực hiện; không lặp cùng Action và tham số, đồng thời dừng khi đạt `MAX_ITERATIONS`. |
| **Bịa kết quả khi tool lỗi** | Agent tự tạo hồ sơ, nghề phù hợp, mức lương hoặc dữ liệu thị trường khi không có Observation hợp lệ. | `build_career_profile` và các tool dữ liệu mở rộng | Chỉ dùng dữ liệu xuất hiện trong Observation; nếu tool lỗi hoặc không có dữ liệu, phải nói rõ giới hạn và đưa ra safe fallback. |
| **Kết luận nghề nghiệp tuyệt đối** | Agent khẳng định người dùng chắc chắn phù hợp hoặc thành công với một nghề duy nhất. | Bước tạo Final Answer | Đưa ra 2–3 lựa chọn mang tính tham khảo, giải thích lý do và để người dùng tự quyết định. |
| **Định kiến và dữ liệu nhạy cảm** | Agent giới hạn nghề theo giới tính, quê quán, hoàn cảnh hoặc yêu cầu thông tin cá nhân không cần thiết. | Bước hội thoại và Final Answer | Chỉ đánh giá dựa trên thông tin nghề nghiệp liên quan; không dùng đặc điểm nhạy cảm để loại trừ nghề và không thu thập dữ liệu không cần thiết. |
| **Prompt injection** | Người dùng yêu cầu Agent bỏ qua quy tắc, giả mạo Observation hoặc tiết lộ chỉ dẫn hệ thống. | Toàn bộ ReAct loop | Không thay đổi System Prompt theo nội dung người dùng; chỉ tin Observation do ứng dụng cung cấp và không tiết lộ chỉ dẫn nội bộ. |
| **Không dừng an toàn** | Agent tiếp tục gọi tool vô hạn khi không thể hoàn tất khảo sát. | ReAct loop | Giới hạn `MAX_ITERATIONS = 3`; khi hết số bước, dừng và trả lời lịch sự, nêu rõ thông tin còn thiếu hoặc lỗi gặp phải. |

### Luồng gọi tool an toàn đề xuất

```text
start_career_survey
→ get_next_question
→ validate_answer
→ save_answer
→ is_survey_completed
→ lặp lại câu hỏi nếu chưa hoàn tất
→ build_career_profile
→ Final Answer
```

---

## BASELINE CHATBOT

**Môi trường chạy thực tế:** `MockProvider (Offline Mock Mode)`

**Test case dùng để quan sát:** `test_cases[0]`

**Câu hỏi**: *"Nghề Data Analyst cần làm những công việc gì?"*

### 🤖 Chatbot Baseline:

- **Phản hồi**: *"🤖 [Mock Provider]: Phản hồi giả lập offline cho bài test."*
- **Nhận xét**: Baseline chatbot trong lần chạy này chưa tạo được câu trả lời nghề nghiệp thực tế vì đang sử dụng dữ liệu phản hồi giả lập.

---

## 🔎 REACT TRACE LOG — THOUGHT → ACTION → OBSERVATION

**Thời điểm chạy:** 28/07/2026

**Provider:** `OpenAIProvider`

**Model:** `gpt-4o-mini`

**Guardrail:** Tối đa 6 vòng lặp

**Kết quả:** Hoàn thành sau 4 bước, không kích hoạt guardrail.

**Câu hỏi người dùng:**

> Tôi tốt nghiệp Công nghệ Thông tin, biết Python và Excel, thích làm việc với dữ liệu và logic. Tôi nên theo nghề gì và cần học thêm những kỹ năng nào?

### Step 1 — Chuẩn hóa hồ sơ người dùng

```text
Thought: Tôi cần thu thập thông tin về sở thích, kỹ năng và học vấn của
người dùng để tìm nghề phù hợp.

Action: assess_user_profile[{
  "education": "Công nghệ Thông tin",
  "skills": ["Python", "Excel"],
  "interests": ["Dữ liệu", "Logic"],
  "personality": "",
  "goals": ""
}]

Observation: {
  "education": "Công nghệ Thông tin",
  "normalized_skills": ["Python", "Excel"],
  "normalized_interests": ["Dữ Liệu", "Logic"],
  "personality": "",
  "career_goals": "",
  "suggested_fields": ["Công nghệ / Dữ liệu"],
  "profile_summary": "Người dùng có nền tảng 'Công nghệ Thông tin',
  sở hữu 2 kỹ năng, quan tâm đến 2 lĩnh vực. Định hướng phù hợp:
  Công nghệ / Dữ liệu."
}
```

### Step 2 — Tìm các nghề phù hợp

```text
Thought: Tôi đã có đủ thông tin về hồ sơ người dùng và giờ tôi sẽ tìm
kiếm các nghề phù hợp dựa trên sở thích và kỹ năng của họ.

Action: search_careers[{
  "interests": ["Dữ Liệu", "Logic"],
  "skills": ["Python", "Excel"]
}]

Observation: [
  {
    "career_code": "data_analyst",
    "career_name": "Chuyên viên Phân tích Dữ liệu (Data Analyst)",
    "field": "Công nghệ / Dữ liệu",
    "match_score": 10,
    "reason": "phù hợp sở thích: logic, dữ liệu; có sẵn kỹ năng:
    python, excel"
  },
  {
    "career_code": "software_developer",
    "career_name": "Lập trình viên Phần mềm (Software Developer)",
    "field": "Công nghệ / Kỹ thuật",
    "match_score": 5,
    "reason": "phù hợp sở thích: logic; có sẵn kỹ năng: python"
  },
  {
    "career_code": "data_scientist",
    "career_name": "Nhà Khoa học Dữ liệu (Data Scientist)",
    "field": "Công nghệ / Dữ liệu",
    "match_score": 5,
    "reason": "phù hợp sở thích: dữ liệu; có sẵn kỹ năng: python"
  },
  {
    "career_code": "business_analyst",
    "career_name": "Chuyên viên Phân tích Nghiệp vụ (Business Analyst)",
    "field": "Kinh doanh / Quản lý",
    "match_score": 5,
    "reason": "phù hợp sở thích: logic; có sẵn kỹ năng: excel"
  }
]
```

### Step 3 — Phân tích khoảng cách kỹ năng

```text
Thought: Tôi đã tìm thấy một số nghề phù hợp với hồ sơ của bạn, đặc biệt
là "Chuyên viên Phân tích Dữ liệu". Giờ tôi sẽ phân tích kỹ năng cần
thiết cho nghề này để xác định những kỹ năng bạn cần học thêm.

Action: analyze_skill_gap[{
  "user_skills": ["Python", "Excel"],
  "target_career": "Chuyên viên Phân tích Dữ liệu"
}]

Observation: {
  "career_code": "data_analyst",
  "career_name": "Chuyên viên Phân tích Dữ liệu (Data Analyst)",
  "matched_skills": ["Python", "Excel"],
  "missing_skills": ["SQL", "Thống kê", "Trực quan hóa dữ liệu"],
  "match_percentage": 40.0,
  "summary": "Bạn đã đáp ứng 2/5 kỹ năng yêu cầu cho nghề
  'Chuyên viên Phân tích Dữ liệu (Data Analyst)' (đạt 40.0%)."
}
```

### Step 4 — Kết luận

```text
Thought: Tôi đã có đủ thông tin để trả lời.

Final Answer: Bạn có thể xem xét theo nghề "Chuyên viên Phân tích Dữ
liệu (Data Analyst)" vì nó phù hợp với sở thích và kỹ năng hiện tại
của bạn. Để hoàn thiện hơn, bạn nên học thêm các kỹ năng sau: SQL,
Thống kê và Trực quan hóa dữ liệu.
```

### Đánh giá trace

| Tiêu chí | Kết quả | Nhận xét |
| :--- | :---: | :--- |
| Đúng chu trình ReAct | Đạt | Mỗi bước có `Thought`, `Action` và `Observation`; bước cuối dùng `Final Answer`. |
| Tool hợp lệ | Đạt | Chỉ gọi các tool đã đăng ký trong `AVAILABLE_TOOLS`. |
| Tham số hợp lệ | Đạt | Tham số JSON đúng với chữ ký của từng tool. |
| Dựa trên Observation | Đạt | Nghề đề xuất và ba kỹ năng còn thiếu đều xuất phát từ kết quả tool. |
| Không lặp Action | Đạt | Không có tool nào bị gọi lại với cùng tham số. |
| Guardrail số vòng | Đạt | Agent kết thúc ở bước 4/6. |
| Mức độ hoàn chỉnh | Đạt một phần | Agent xác định được skill gap nhưng chưa gọi `recommend_learning_path`, nên chưa tạo lộ trình học chi tiết. |

**Kết luận:** Trace chứng minh Agent có thể dùng dữ liệu từ tool để đưa ra
khuyến nghị có căn cứ hơn chatbot baseline. Điểm cần cải thiện là tiếp tục
gọi `recommend_learning_path` sau khi nhận được `missing_skills`, nếu người
dùng yêu cầu một kế hoạch học cụ thể.
