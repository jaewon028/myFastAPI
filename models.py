# 파이보: 질문 답변 게시판
# 질문과 답변에 해당하는 모델이 있어야 한다.

'''
[질문 모델 속성]

속성명	설명
id	질문 데이터의 고유 번호
subject	질문 제목
content	질문 내용
create_date	질문 작성일시
'''


'''
[답변 모델 속성]

속성명	설명
id	답변 데이터의 고유 번호
question_id	질문 데이터의 고유 번호(어떤 질문에 달린 답변인지 알아야 하므로 질문 데이터의 고유 번호가 필요하다)
content	답변 내용
create_date	답변 작성일시
'''

## 질문 모델 생성하기
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base


# Question이라는 모델 클래스
# database.py의 Base 클래스를 상속하여 생성
class Question(Base):
    # 모델에 의해 관리되는 테이블의 이름
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_data = Column(DateTime, nullable=False)

