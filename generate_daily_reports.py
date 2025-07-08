#!/usr/bin/env python3
"""
Script tự động sinh file báo cáo hàng ngày cho FCJ Internship Program
Author: Linh Dang Dev
Created: 2025-07-08
"""

import os
import logging
from datetime import datetime, timedelta
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('report_generation.log'),
        logging.StreamHandler()
    ]
)

class DailyReportGenerator:
    def __init__(self, start_date_str="2025-05-12", end_date_str="2025-07-20"):
        self.start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        self.report_dir = Path("worklog/Report")
        self.weekdays_vn = {
            0: "Thứ Hai",
            1: "Thứ Ba", 
            2: "Thứ Tư",
            3: "Thứ Năm",
            4: "Thứ Sáu",
            5: "Thứ Bảy",
            6: "Chủ Nhật"
        }
        
        self.report_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Khởi tạo generator từ {start_date_str} đến {end_date_str}")

    def calculate_week_day(self, current_date):
        days_diff = (current_date - self.start_date).days
        week_number = (days_diff // 7) + 1
        day_in_week = (days_diff % 7) + 1
        return week_number, day_in_week

    def get_weekday_vietnamese(self, date):
        return self.weekdays_vn[date.weekday()]

    def generate_report_content(self, date, week_num, day_num):
        weekday_vn = self.get_weekday_vietnamese(date)
        date_str = date.strftime("%d/%m/%Y")
        
        template = f"""# Worklog - Ngày {date_str}

## 📅 Thông tin cơ bản
- **Ngày**: {date_str}
- **Thứ**: {weekday_vn}
- **Tuần thực tập**: Tuần thứ {week_num}/8
- **Thời gian làm việc**: 8:00 - 17:00
- **Mood**: 😊 Ready for new challenges

## 🎯 Mục tiêu ngày hôm nay
- [ ] Mục tiêu 1 - Cần cập nhật
- [ ] Mục tiêu 2 - Cần cập nhật
- [ ] Mục tiêu 3 - Cần cập nhật
- [ ] Mục tiêu 4 - Cần cập nhật

## 💼 Công việc đã thực hiện

### 1. Task 1 ⏱️ 8:00-10:00
- **Mô tả**: 
  - Cần cập nhật mô tả công việc
  - Chi tiết các bước thực hiện
  - Kết quả đạt được
- **Kết quả**: 
  - Kết quả cụ thể
  - Metrics hoặc deliverables
- **Tools/Tech**: AWS Services, Tools sử dụng
- **Links**: 
  - [Link tài liệu](https://example.com)

### 2. Task 2 ⏱️ 10:30-12:00
- **Mô tả**: 
  - Cần cập nhật mô tả công việc
  - Chi tiết các bước thực hiện
- **Kết quả**: 
  - Kết quả cụ thể đạt được
- **Tools/Tech**: AWS Services, Tools sử dụng
- **Links**: 
  - [Link tài liệu](https://example.com)

### 3. Task 3 ⏱️ 13:00-15:30
- **Mô tả**: 
  - Cần cập nhật mô tả công việc
  - Chi tiết learning objectives
- **Kết quả**: 
  - Kiến thức học được
  - Skills phát triển
- **Tools/Tech**: AWS Training, Documentation
- **Links**: 
  - [Learning Resource](https://example.com)

### 4. Task 4 ⏱️ 15:30-17:00
- **Mô tả**: 
  - Cần cập nhật mô tả công việc
  - Documentation và planning
- **Kết quả**: 
  - Deliverables hoàn thành
- **Tools/Tech**: GitHub, VS Code, Markdown
- **Links**: 
  - [Repository](https://github.com/example)

## 📚 Kiến thức học được

### 🔧 Technical Skills
- **AWS Services**: 
  - Service 1 - concepts và use cases
  - Service 2 - hands-on experience
- **Programming**: 
  - Language/Framework skills
- **DevOps**: 
  - Tools và best practices
- **Architecture**: 
  - Design patterns học được

### 💡 Concepts & Theory
- **New Concepts**: 
  - Concept 1 và ứng dụng
  - Concept 2 và best practices
- **Best Practices**: 
  - Security considerations
  - Performance optimization
- **Industry Knowledge**: 
  - Market trends
  - Technology adoption

### 🤝 Soft Skills
- **Communication**: 
  - Meeting participation
  - Documentation skills
- **Problem Solving**: 
  - Debugging techniques
  - Research methodology
- **Time Management**: 
  - Planning strategies
  - Priority management
- **Learning**: 
  - Study techniques
  - Knowledge retention

## 🚧 Khó khăn và giải pháp

### Vấn đề 1: [Tên vấn đề]
- **Mô tả**: Chi tiết vấn đề gặp phải
- **Impact**: Ảnh hưởng đến công việc
- **Root Cause**: Nguyên nhân gốc rễ
- **Solution**: 
  - Bước 1 giải quyết
  - Bước 2 implement
  - Bước 3 verify
- **Result**: Kết quả sau khi giải quyết
- **Lesson**: Bài học rút ra

### Vấn đề 2: [Tên vấn đề]
- **Mô tả**: Chi tiết vấn đề gặp phải
- **Impact**: Ảnh hưởng đến timeline
- **Root Cause**: Nguyên nhân chính
- **Solution**: 
  - Approach đã sử dụng
  - Tools hỗ trợ
- **Result**: Outcome đạt được
- **Lesson**: Key takeaway

## 💭 Reflection & Insights

### What went well today?
- Thành công 1 - chi tiết
- Thành công 2 - impact
- Thành công 3 - learning

### What could be improved?
- Cải thiện 1 - specific area
- Cải thiện 2 - action plan
- Cải thiện 3 - timeline

### Key Insights
- **Technical**: Technical learning highlights
- **Career**: Professional development insights
- **Personal**: Personal growth observations

### Questions & Curiosities
- Câu hỏi 1 về technical concepts?
- Câu hỏi 2 về best practices?
- Câu hỏi 3 về career development?
- Câu hỏi 4 về industry trends?

## 📋 Kế hoạch ngày mai

### Priority Tasks
- [ ] **High**: Task quan trọng nhất
- [ ] **High**: Task ưu tiên cao thứ 2
- [ ] **Medium**: Task ưu tiên trung bình

### Learning Goals
- [ ] Learning objective 1
- [ ] Learning objective 2
- [ ] Learning objective 3
- [ ] Learning objective 4

### Meetings & Deadlines
- [ ] Meeting 1 at [time]
- [ ] Meeting 2 at [time]
- [ ] Deadline for deliverable

## 📊 Self Assessment

### Productivity
- **Score**: ?/10
- **Reason**: Đánh giá productivity
- **Improvement**: Cách cải thiện

### Learning
- **Score**: ?/10
- **New Knowledge**: Kiến thức mới học được
- **Application**: Ứng dụng thực tế

### Collaboration
- **Score**: ?/10
- **Interactions**: Tương tác với team
- **Contributions**: Đóng góp cho dự án

### Overall Satisfaction
- **Score**: ?/10
- **Highlights**: Điểm nổi bật trong ngày
- **Areas for Growth**: Lĩnh vực cần phát triển

## 📎 Attachments & Links

### Code & Projects
- [GitHub Repository](https://github.com/example)
- [Code Samples](https://gist.github.com/example)

### Learning Resources
- [AWS Documentation](https://docs.aws.amazon.com)
- [Training Materials](https://example.com)
- [Best Practices Guide](https://example.com)

### Screenshots & Demos
- ![Screenshot 1](screenshots/example1.png)
- ![Screenshot 2](screenshots/example2.png)
- ![Demo Video](screenshots/demo.mp4)

---

**📝 Notes for tomorrow:**
- Note 1 cho ngày mai
- Note 2 về preparation
- Note 3 về follow-up tasks

**🎯 Week Progress:**
Day {day_num}/5 completed. Progress update và next steps.

---
*Worklog created by: Linh Dang Dev - FCJ Intern Batch 2025*  
*Next review: {(date + timedelta(days=1)).strftime("%d/%m/%Y")} - Daily standup*
"""
        return template

    def generate_filename(self, week_num, day_num):
        return f"week-{week_num:02d}-day-{day_num:02d}.md"

    def create_report_file(self, date, week_num, day_num):
        filename = self.generate_filename(week_num, day_num)
        filepath = self.report_dir / filename
        
        if filepath.exists():
            logging.warning(f"File {filename} đã tồn tại, bỏ qua...")
            return False
        
        content = self.generate_report_content(date, week_num, day_num)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            logging.info(f"✅ Tạo thành công: {filename} cho ngày {date.strftime('%d/%m/%Y')}")
            return True
        except Exception as e:
            logging.error(f"❌ Lỗi tạo file {filename}: {str(e)}")
            return False

    def generate_all_reports(self):
        logging.info("🚀 Bắt đầu tạo các file báo cáo...")
        
        current_date = self.start_date
        created_count = 0
        skipped_count = 0
        
        while current_date <= self.end_date:
            week_num, day_num = self.calculate_week_day(current_date)
            
            if self.create_report_file(current_date, week_num, day_num):
                created_count += 1
            else:
                skipped_count += 1
            
            current_date += timedelta(days=1)
        
        logging.info(f"🎉 Hoàn thành! Tạo mới: {created_count} files, Bỏ qua: {skipped_count} files")
        return created_count, skipped_count

def main():
    print("=" * 60)
    print("📋 FCJ INTERNSHIP DAILY REPORT GENERATOR")
    print("=" * 60)
    print("Author: Linh Dang Dev")
    print("Tạo file báo cáo hàng ngày từ 12/05/2025 đến 20/07/2025")
    print("=" * 60)
    
    try:
        generator = DailyReportGenerator()
        created, skipped = generator.generate_all_reports()
        
        print(f"\n📊 KẾT QUẢ:")
        print(f"✅ Files tạo mới: {created}")
        print(f"⏭️  Files bỏ qua: {skipped}")
        print(f"📁 Thư mục: worklog/Report/")
        print(f"📝 Log file: report_generation.log")
        
    except Exception as e:
        logging.error(f"❌ Lỗi chương trình: {str(e)}")
        print(f"❌ Có lỗi xảy ra: {str(e)}")

if __name__ == "__main__":
    main()
