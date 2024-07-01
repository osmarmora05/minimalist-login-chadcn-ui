from ..db.client import connect
from ..models.user_model import Users
from sqlmodel import Session, select


def get_users():
    engine = connect()
    with Session(engine) as session:
        """
        https://sqlmodel.tiangolo.com/tutorial/select/
        query = select(Users)
        results = session.exec(query)
        # [User(...)]
        users = results.all()
        """

        # Compact version
        # [User(...)]
        results = session.exec(select(Users)).all()
        return results


def get_user(github_username: str, password: str):
    engine = connect()
    with Session(engine) as session:
        """
        https://sqlmodel.tiangolo.com/tutorial/where/
        """
        results = session.exec(select(Users).where(
            Users.github_username == github_username).where(Users.password == password)).all()

        return results


def delete_user(github_username: str, password: str):
    engine = connect()
    with Session(engine) as session:
        statement = select(Users).where(
            Users.github_username == github_username).where(Users.password == password)
        results = session.exec(statement).one()
        session.delete(results)
        session.commit()