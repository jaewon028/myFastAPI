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

from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base


# Question이라는 질문 모델 클래스
# database.py의 Base 클래스를 상속하여 생성
class Question(Base): # 질문 모델 생성
    # 모델에 의해 관리되는 테이블의 이름
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_data = Column(DateTime, nullable=False)

# Answer이라는 답변 모델 클래스
from sqlalchemy import ForeignKey
from sqlalchemy.orm import  relationship

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # question_id는 question 테이블의 id 컬럼과 연결됨.
    # question --> relationship: 답변 객체에서 연결된 질문의 제목을 answer.question.subject처럼 참조 가능
    # backref를 통해 질문에 달린 답변들을 참조
    # 예를 들어, 어떤 질문에 해당하는 객체가 a_question이라면, a_question.answers로 질문에 달린 답변들 참조 가능
    question = relationship("Question", backref="answers") #답변 모델에서 질문 모델을 참조


'''
[모델을 이용해 테이블 자동으로 생성하기]
alembic 설치
alembic: SQLAlchemy로 작성한 모델을 기반으로 데이터베이스를 쉽게 관리할 수 있게 도와줌.
즉, models.py 파일에 작성한 모델을 이용하여 테이블을 생성하고 변경 가능.

$ alembic init migrations
--> migrations 디렉터리와 alembic.ini 파일이 생긴다.
--> migrations 디렉터리: alembic 도구를 사용할 때 생성되는 리비전 파일들을 저장하는 용도로 사용
--> alembic.ini 파일: alembic의 환경설정 파일

** alembic을 이용하여 테이블을 생성 또는 변경할 때마다 작업 파일이 생성되는데 이 작업 파일을 리비전 파일이라고 한다. 
** 그리고 이 리비전 파일은 migrations 디렉터리에 저장된다.

< alembic 셋팅 1 >
이어서 alembic.ini 파일을 파이참으로 열어서 다음과 같이 수정하자.

[파일명: projects/myapi/alembic.ini]
(... 생략 ...)
sqlalchemy.url = sqlite:///./myapi.db
(... 생략 ...)

< migrations (env.py) 파일 셋팅 1 >

[파일명: projects/myapi/migrations/env.py]

(... 생략 ...)
import models
(... 생략 ...)
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = models.Base.metadata
(... 생략 ...)

< 리비전 파일 생성하기 >
$ alembic revision --autogenerate

9e3a56e86bfe_.py 생성됨.
리비전이란 이 파일에서 번호들을 가리킴.
리비전 파일에는 테이블을 생성 또는 변경하는 실행문들이 들어있음.

< 리비전 파일 생성하기 >
alembic upgrad head --> myapi.db가 생성됨.
myapi.db : SQLite 데이터베이스의 데이터 파일.


< alembic 없이 테이블 생성하기 >
main.py 파일에 다음의 문장을 삽입하면 FastAPI 실행시 필요한 테이블들이 모두 생성된다.

import models
from database import engine
models.Base.metadata.create_all(bind=engine)
매우 간단한 방법이지만 데이터베이스에 테이블이 존재하지 않을 경우에만 테이블을 생성한다. 
한번 생성된 테이블에 대한 변경 관리를 할 수는 없다. 
이러한 이유로 이 책에서는 이 방법을 사용하지 않고 alembic을 사용하여 데이터베이스를 관리할 것이다.
'''