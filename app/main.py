import queries
import typer
from alembic import command
from alembic.config import Config
from config import DATABASE_URL
from seed import populate_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = typer.Typer()


def run_migrations():
    """Выполняет миграции базы данных до последней версии."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@app.command()
def init_db():
    """Инициализирует и заполняет базу данных."""
    typer.echo("Выполняется миграция базы данных...")
    run_migrations()
    typer.echo("Миграция завершена.")

    typer.echo("Заполнение базы данных...")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    populate_database(session)

    session.close()
    typer.echo("База данных заполнена.")


@app.command()
def query1():
    """Выполняет Задание 1."""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    queries.query_1(session)

    session.close()


@app.command()
def query2():
    """Выполняет Задание 2."""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    queries.query_2(session)

    session.close()


@app.command()
def query3():
    """Выполняет Задание 3."""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    queries.query_3(session)

    session.close()


@app.command()
def query4():
    """Выполняет Задание 4."""
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    queries.query_4(session)

    session.close()


@app.command()
def query5():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    queries.query_5(session)

    session.close()


if __name__ == "__main__":
    app()
