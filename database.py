from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터 베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

# create_engine, sessionmaker 등을 사용하는 것은 SQLAlchemy 데이터베이스를 사용하기 위해 따라야할 규칙
# autocommit=False로 설정하면 데이터를 변경했을 때 commit이라는 사인을 주어야만 실제 저장이 된다.
# True로 설정한 경우 commit이라는 사인이 없어도 즉시 데이터베이스에 변경사항이 적용된다.
# False로 하면 잘못 저장했을 경우 rollback 사인으로 되돌리는것이 가능.
# create_engine은 커넥션 풀을 생성.
# !! 커넥션 풀: 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어놓고 돌려가며 사용하는 것.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session local : 데이터베이스에 접속하기 위해 필요한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()