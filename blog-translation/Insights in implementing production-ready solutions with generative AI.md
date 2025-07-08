<!-- markdownlint-disable MD041 -->
<!-- spell-checker: disable -->

<style>
.justify-text {
    text-align: justify;
    text-justify: inter-word;
}

p {
    text-align: justify;
    text-justify: inter-word;
}
</style>

# Những Hiểu Biết Sâu Sắc Trong Việc Triển Khai Các Giải Pháp Production-Ready Với Generative AI


**📖 Bài viết gốc**: *[Insights in implementing production-ready solutions with generative AI](https://aws.amazon.com/blogs/machine-learning/insights-in-implementing-production-ready-solutions-with-generative-ai/).*
**👤 Tác giả**: *Giorgio Pessot, Amer Elhabbash, Aamna Najmi, Anwar Rizal, Dragica Boca, Subhro Bose, Sri Elaprolu, Hassen Riahi, Marco Guerriero, Nicolo Cosimo Albanese, Diar Sabri, and Daniel Zagyva.*
**📅 Ngày xuất bản**: *30/04/2025*
**🌐 Nguồn**: *[AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/)*
**👨‍💻 Người dịch**: *Dang Duy Linh - FCJ Intern*
**📅 Ngày dịch**: 02/07/2025
**⏱️ Thời gian đọc**: *10 phút*

---

## 📋 Tóm tắt

> Bài viết này chia sẻ những hiểu biết sâu sắc và bài học kinh nghiệm từ các khách hàng AWS tại khu vực EMEA về việc triển khai thành công các giải pháp AI tạo sinh sẵn sàng cho môi trường production. Nội dung tập trung vào việc chuyển đổi từ giai đoạn pre-production sang triển khai quy mô lớn, bao gồm các thách thức về vận hành, kỹ thuật, bảo mật và tuân thủ quy định. Bài viết cung cấp roadmap chi tiết với các case studies thực tế từ Il Sole 24 Ore, Booking.com, ENGIE, Iveco Group, Accor Group, Danske Bank và Schaeffler Group, giúp các tổ chức khác có thể áp dụng thành công AI tạo sinh trong môi trường doanh nghiệp.

**🎯 Đối tượng đọc**: Cloud Architects, DevOps Engineers, AI/ML Engineers, Technical Leaders
**📊 Độ khó**: Intermediate to Advanced
**🏷️ Tags**: *[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/),  [Generative AI](https://aws.amazon.com/generative-ai/), [AWS Well-Architecture Framework](https://aws.amazon.com/blogs/machine-learning/category/aws-well-architected/aws-well-architected-framework/), [Best Practices](https://aws.amazon.com/blogs/machine-learning/category/post-types/best-practices/), [Customer Solutions](https://aws.amazon.com/blogs/machine-learning/category/post-types/best-practices/), [Experience-Based Acceleration](https://aws.amazon.com/blogs/machine-learning/category/post-types/customer-solutions/experience-based-acceleration/), [Thought Leadership](https://aws.amazon.com/blogs/machine-learning/category/post-types/thought-leadership/)*

---

## 📚 Mục lục

- [1. Giới thiệu](#1-giới-thiệu)
- [2. Xây dựng Business Case vững chắc](#2-xây-dựng-business-case-vững-chắc)
  - [2.1 Case Study: Il Sole 24 Ore](#21-case-study-il-sole-24-ore)
  - [2.2 Case Study: Booking.com](#22-case-study-bookingcom)
  - [2.3 Case Study: ENGIE](#23-case-study-engie)
- [3. Vượt qua các thách thức triển khai](#3-vượt-qua-các-thách-thức-triển-khai)
  - [3.1 Đạt được quy mô, độ tin cậy và tuân thủ](#31-đạt-được-quy-mô-độ-tin-cậy-và-tuân-thủ)
  - [3.2 Hạ tầng Production-Ready](#32-hạ-tầng-production-ready)
- [4. Bảo mật, tuân thủ và AI có trách nhiệm](#4-bảo-mật-tuân-thủ-và-ai-có-trách-nhiệm)
- [5. Kết luận](#5-kết-luận)
- [Glossary - Thuật ngữ](#glossary---thuật-ngữ)
- [Tài liệu tham khảo](#tài-liệu-tham-khảo)

---

## 1. Giới thiệu

<div style="text-align: justify;">
Khi <a href="https://aws.amazon.com/generative-ai/">AI tạo sinh</a> đang cách mạng hóa các ngành công nghiệp, các tổ chức đang hứng thú đề khai thác tiềm năng của nó. Tuy nhiên, hành trình chuyển đổi từ một giải pháp đang vận hành sang triển khai trên một quy mô lớn hơn thường đặt ra những thách thức về mặt kỹ thuật và vận hành. Trong bài viết này chúng ta sẽ đi khám phá về những phát hiện quan trọng và bài học kinh nghiệm từ các khách hàng AWS tại khu vực Châu ÂU, Trung Đông và Châu Phi (EMEA) họ đã thành công trong việc triển khai AI tạo sinh trong môi trường doanh nghiệp, và cung cấp cho mọi người một lộ trình chi tiết để theo dõi nếu như muốn triển khai giải pháp này cho doanh nghiệp của mình.
</div>

## 2. Xây dựng đề án kinh doanh (Business Case) vững chắc: xuất sắc trong việc vận hành và thức đẩy trải nghiệm cho khách hàng

<div class="justify-text">
Nền tảng cho sự thành công triển khai AI tạo sinh là các đề án kinh doanh phải có các giá trị rõ ràng, phù hợp với mục tiêu tổ chức, ví dụ như nâng cao hiệu suất, tiết kiệm chi phí hoặc tăng trưởng doanh thu. Các ví dụ điển hình bao gồm cải thiện trải nghiệm khách hàng, tối ưu hóa vận hành và duy trì tuân thủ các tiêu chuẩn pháp lý, cải thiện mức độ dịch vụ hoặc tăng năng suất nhân viên.
</div>

Các công ty tại EMEA đã sử dụng các dịch vụ AWS để chuyển đổi hoạt động và cải thiện trải nghiệm khách hàng bằng AI tạo sinh, với những câu chuyện của họ minh họa cách một đề án kinh doanh mạnh mẽ có thể dẫn đến kết quả hữu hình trên các ngành công nghiệp khác nhau.

### 2.1 Case Study: Il Sole 24 Ore

[Il Sole 24 Ore](https://www.ilsole24ore.com/), tập đoàn xuất bản đa phương tiện hàng đầu của Italy, đã hợp tác với [AWS Professional Services](https://aws.amazon.com/professional-services/) làm thúc đẩy hiệu quả của một dịch vụ lịch sử, L'Esperto Risponde, nơi người dùng có thể đặt câu hỏi về thuế và nhận phản hồi từ đội ngũ chuyên gia.

Il Sole 24 Ore đã tận dụng kiến thức nội bộ rộng lớn với giải pháp Retrieval Augmented Generation (RAG) được hỗ trợ bởi AWS. Giải pháp này duy trì độ chính xác trên 90% trong các phản hồi và giảm thời gian các chuyên gia dành cho việc tìm kiếm và xử lý thông tin, giúp họ tập trung vào các nhiệm vụ chiến lược hơn.

Bên cạnh đó, công ty đang liên tục nhận các phản hồi của người dùng cuối và cải thiện dịch vụ để giữ cho dịch vụ phù hợp với nhu cầu của khách hàng.

Để biết thêm thông tin, bạn có thể xem bài thuyết trình [AWS Summit Milan 2024](https://www.youtube.com/watch?v=hHiGLL0Ccvw).


### 2.2 Case Study: Booking.com

[Booking.com](http://booking.com/), một trong những ông lớn dịch vụ du lịch kỹ thuật số hàng đầu thế giới, đang sử dụng AWS để cung cấp công nghệ AI ở quy mô lớn, tạo ra trải nghiệm khách hàng được cá nhân hóa đồng thời đạt được khả năng mở rộng và hiệu quả cao hơn trong hoạt động của họ. Booking.com sử dụng [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/) để cung cấp các đề xuất chỗ ở được cá nhân hóa cao cho khách hàng.

> *"Một trong những điều chúng tôi thực sự thích về cách tiếp cận AI tạo sinh của AWS là sự lựa chọn. Chúng tôi yêu thích mã nguồn mở và cảm thấy nó sẽ đóng vai trò quan trọng trong sự phát triển của AI tạo sinh,"*
>
> – Rob Francis, Giám đốc Công nghệ của Booking.com.

Với sự hỗ trợ của AWS, Booking.com đang nâng cao khả năng của AI tạo sinh, và định vị cho sự phát triển trong tương lai của ngành du lịch và khách sạn. Để biết thêm thông tin chi tiết, bạn có thể đón xem [Bài phát biểu quan trọng của Booking.com tại AWS re:Invent 2023](https://aws.amazon.com/solutions/case-studies/booking-keynote-aws-reinvent-2023/) và bài thuyết trình trên [AI tạo sinh từ ý tưởng đến sản phẩm triển khai trên AWS tại AWS London Summit 2024](https://www.youtube.com/watch?v=AUBw3d3NjGw)


### 2.3 Case Study: ENGIE

[ENGIE](https://www.engie.com/en) là một công ty điện lực và tiện ích toàn cầu, với 25 đơn vị kinh doanh đang hoạt động trên toàn thế giới. Đội ngũ One Data của ENGIE đã hợp tác với AWS Professional Services để phát triển chatbot được hỗ trợ bởi AI cho phép tìm kiếm hội thoại bằng ngôn ngữ tự nhiên trong data lake Common Data Hub của ENGIE, với hơn 3 petabyte dữ liệu.

Giải pháp này bổ sung cho tìm kiếm dựa trên từ khóa truyền thống bằng cách cho phép người dùng khám phá bộ dữ liệu (datasets) thông qua các truy vấn hội thoại đơn giản, giúp dễ dàng tìm thấy dữ liệu liên quan trong hàng chục nghìn tập dữ liệu được chia sẻ trong tổ chức.

Những ví dụ này đã hứng minh một phần nào đó về cách mà các công ty trong các lĩnh vực khác nhau đã sử dụng thành công khả năng AI tạo sinh của AWS để giải quyết các thách thức kinh doanh cụ thể và đem lại lợi ích cho công ty


## 3. Vượt qua các thách thức triển khai

Mặc dù cần thiết, một đề án kinh doanh vững chắc chỉ là bước đầu tiên. Khi các tổ chức đẩy mạnh các sáng kiến AI tạo sinh của họ, song họ vẫn thường gặp phải những thách thức mới liên quan đến việc làm cho giải pháp có thể mở rộng, đáng tin cậy và tuân thủ các quy định của tổ chức. Vì vậy hãy cùng khám phá bí quyết để đưa các dự án AI Tạo sinh từ giai đoạn phát triển ra vận hành thực tế một cách thành công, sao cho những lợi ích đã cam kết ban đầu được phát huy tối đa trong ứng dụng thực tiễn.

### 3.1 Đạt được quy mô, độ tin cậy và tuân thủ các quy định của tổ chức

Các yếu tố cần được đặt lên bàn cân để xem xét trong việc chuyển đổi sang production quy mô đầy đủ bao gồm khả năng mở rộng, quản trị dữ liệu, quyền riêng tư, hành vi AI nhất quán và có trách nhiệm, bảo mật, tích hợp với hệ thống hiện có, giám sát, thu thập phản hồi từ người dùng cuối và đo lường tác động kinh doanh.

### 3.2 Hạ tầng Production-Ready

Với sự gia tăng về phạm vi, số lượng và độ phức tạp của các ứng dụng AI tạo sinh, các tổ chức có nhu cầu tăng lên để giảm nỗ lực không có sự khác biệt và đặt ra tiêu chuẩn chất lượng cao cho các ứng dụng sẵn sàng cho production.

Các thực hành phát triển tiêu chuẩn và mô hình vận hành đám mây hiệu quả, như [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) và [AWS Cloud Adoption Framework for AI, ML, and Generative AI](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html), là chìa khóa để cho phép các đội ngũ dành phần lớn thời gian cho các nhiệm vụ có giá trị kinh doanh cao, thay vì các hoạt động thủ công lặp lại.

**Case Study: Iveco Group**

[Iveco Group](https://www.ivecogroup.com/), một nhà lãnh đạo ô tô toàn cầu hoạt động trong lĩnh vực Xe thương mại và chuyên dụng, Powertrain, đã áp dụng mô hình vận hành đám mây có cấu trúc, tận dụng IaC thông qua Terraform để triển khai nhất quán và có thể lặp lại trên các môi trường.

**Case Study: Accor Group**

[Accor Group](https://group.accor.com/en), một công ty khách sạn lớn đã phát triển ứng dụng đặt phòng được hỗ trợ bởi AI tạo sinh, đã triển khai chiến lược kiểm thử ba lớp toàn diện:
1. **Unit tests**: Xác minh rằng các prompts tạo ra phản hồi chấp nhận được từ chatbot
2. **Integration tests**: Xác minh luồng end-to-end của REST API
3. **Functional testing**: Kiểm thử thủ công với các kịch bản được xác định trước

## 4. Bảo mật, tuân thủ và AI có trách nhiệm

Khi các ứng dụng AI tạo sinh của tổ chức mở rộng để xử lý dữ liệu ngày càng nhạy cảm, bảo mật, tuân thủ và quản trị phải được ưu tiên tương ứng. Điều này bao gồm triển khai xác thực và kiểm soát truy cập, mã hóa dữ liệu khi nghỉ và trong quá trình truyền tải, giám sát và kiểm toán truy cập và sử dụng hệ thống, duy trì tuân thủ các quy định (như GDPR và EU AI Act gần đây), cũng như thiết lập các chính sách rõ ràng cho việc xử lý dữ liệu và sử dụng mô hình.

**Ví dụ từ Il Sole 24 Ore**: Công ty đã triển khai bộ quy tắc tự kỷ luật cho ứng dụng AI đạo đức, bao gồm tuân thủ quy định, duy trì nguồn gốc và độ tin cậy của dữ liệu, kết hợp giám sát con người thông qua human-in-the-loop.

**Ví dụ từ Accor Group**: Để đảm bảo chatbot cung cấp dịch vụ khách hàng hiệu quả trong khi hoạt động trong các ranh giới đạo đức nghiêm ngặt, họ đã thiết lập các biện pháp bảo vệ cụ thể:
- Chặn phản hồi đối với các truy vấn phân biệt đối xử
- Từ chối phản hồi đối với các hoạt động bất hợp pháp
- Triển khai guardrails để giữ cuộc hội thoại trong bối cảnh kinh doanh phù hợp
- Bảo vệ chống lại prompt injections

## 5. Kết luận

Quá trình chuyển đổi từ preproduction sang triển khai quy mô đầy đủ cho các ứng dụng AI tạo sinh đưa ra những thách thức và cơ hội mới. Nó đòi hỏi việc xác định business case vững chắc, duy trì tiêu chuẩn cao cho hạ tầng và quy trình, tư duy chiến lược trong việc chọn mô hình vận hành đám mây hiệu quả, quản trị dữ liệu mạnh mẽ, bảo mật, tuân thủ, thực hành AI đạo đức và nhiều hơn nữa.

Các tổ chức trên khắp EMEA đã chứng minh cách sử dụng các dịch vụ AWS có thể giúp vượt qua các rào cản và tăng tốc lợi thế của AI tạo sinh bằng cách áp dụng cách tiếp cận toàn diện. Bằng cách học hỏi từ các use case này, nhiều doanh nghiệp hơn có thể đạt được việc triển khai thành công các giải pháp AI tạo sinh và hưởng lợi từ công nghệ chuyển đổi này một cách đáng tin cậy, hiệu quả và có trách nhiệm.

---

## 📖 Glossary - Thuật ngữ

| English | Tiếng Việt | Định nghĩa |
|---------|------------|------------|
| Generative AI | AI tạo sinh | Công nghệ AI có khả năng tạo ra nội dung mới như văn bản, hình ảnh, mã nguồn |
| Production-Ready | Sẵn sàng cho production | Trạng thái hệ thống đã được kiểm thử và tối ưu để triển khai thực tế |
| RAG (Retrieval Augmented Generation) | Tăng cường tạo sinh với truy xuất | Kỹ thuật kết hợp truy xuất thông tin với AI tạo sinh |
| Business Case | Đề án kinh doanh | Tài liệu mô tả lý do và lợi ích của một dự án |
| Infrastructure as Code (IaC) | Hạ tầng dưới dạng mã | Quản lý hạ tầng thông qua mã nguồn thay vì cấu hình thủ công |
| CI/CD | Tích hợp và triển khai liên tục | Quy trình tự động hóa việc build, test và deploy ứng dụng |
| Compliance | Tuân thủ | Việc đáp ứng các yêu cầu pháp lý và quy định |
| GDPR | Quy định bảo vệ dữ liệu chung | Luật bảo vệ dữ liệu của Liên minh Châu Âu |
| Human-in-the-loop | Con người trong vòng lặp | Mô hình có sự tham gia của con người trong quy trình AI |
| Prompt Injection | Tấn công prompt | Kỹ thuật tấn công nhằm thao túng AI thông qua input độc hại |
| Guardrails | Rào cản bảo vệ | Các biện pháp kiểm soát và giới hạn hành vi của AI |
| Well-Architected | Kiến trúc tốt | Framework thiết kế hệ thống của AWS theo best practices |

## 🔗 Tài liệu tham khảo

### Tài liệu gốc
- [Insights in implementing production-ready solutions with generative AI](https://aws.amazon.com/blogs/machine-learning/insights-in-implementing-production-ready-solutions-with-generative-ai/): Bài viết gốc
- [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/): Blog chính thức về ML của AWS
- [AWS Summit Milan 2024 - Il Sole 24 Ore](https://www.youtube.com/watch?v=hHiGLL0Ccvw): Presentation về case study

### AWS Services và Framework
- [Amazon Bedrock](https://aws.amazon.com/bedrock/): Dịch vụ AI tạo sinh của AWS
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/): Platform ML toàn diện
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/): Framework thiết kế hệ thống
- [AWS Cloud Adoption Framework for AI](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html): Hướng dẫn áp dụng AI trên cloud
- [AWS Professional Services](https://aws.amazon.com/professional-services/): Dịch vụ tư vấn chuyên nghiệp

### Case Studies và Resources
- [Booking.com AWS re:Invent 2023 Keynote](https://aws.amazon.com/solutions/case-studies/booking-keynote-aws-reinvent-2023/): Keynote về AI tạo sinh
- [AWS Generative AI Use Cases](https://aws.amazon.com/ai/generative-ai/use-cases/): Các use case thực tế
- [AWS Customer Success Stories](https://aws.amazon.com/ai/generative-ai/customers/): Câu chuyện thành công của khách hàng
- [AWS Training and Certification](https://aws.amazon.com/training/): Đào tạo và chứng chỉ AWS

---

## 💬 Ghi chú của người dịch

Bài viết này cung cấp cái nhìn toàn diện về việc triển khai AI tạo sinh trong môi trường doanh nghiệp thực tế, với nhiều case studies cụ thể và actionable insights.

### Challenges trong quá trình dịch
- **Technical Terms**: Một số thuật ngữ như "production-ready", "guardrails" được giữ nguyên hoặc dịch kèm giải thích để đảm bảo tính chính xác
- **Cultural Context**: Các case studies từ châu Âu được giữ nguyên để thể hiện tính đa dạng và phạm vi ứng dụng toàn cầu
- **Complex Concepts**: Các khái niệm phức tạp như RAG, Human-in-the-loop được giải thích chi tiết trong glossary

### Insights gained
- **Technical Learning**: Hiểu sâu hơn về các thách thức thực tế khi triển khai AI tạo sinh ở quy mô doanh nghiệp
- **Language Skills**: Phát triển khả năng dịch thuật technical content một cách chính xác và dễ hiểu
- **Industry Knowledge**: Nắm bắt được xu hướng và best practices trong việc áp dụng AI tạo sinh

---

## 🤝 Đóng góp và Feedback

Bài dịch này được thực hiện trong khuôn khổ **FCJ Internship Program**.

**📧 Liên hệ**: dangduylinhforwork@gmail.com
**💬 Feedback**: Mọi góp ý để cải thiện chất lượng dịch thuật xin gửi về email trên
**🔄 Updates**: Bài dịch sẽ được cập nhật dựa trên feedback từ cộng đồng

---

*© 2025 - Bản dịch thuộc về Linh Dang Dev - FCJ Intern Batch 2025. Vui lòng credit khi sử dụng.*
