import models
import sqlalchemy as al
from sqlalchemy.orm import Session


def query_1(session: Session) -> None:
    olympic_2004 = (
        session.query(models.Olympic).filter(models.Olympic.year == 2004).first()
    )

    results = (
        session.query(
            al.func.extract("year", models.Player.birthdate).label("birth_year"),
            al.func.count(al.distinct(models.Player.player_id)).label("num_players"),
            al.func.count(models.Result.medal).label("num_gold_medals"),
        )
        .join(models.Result, models.Player.player_id == models.Result.player_id)
        .join(models.Event, models.Result.event_id == models.Event.event_id)
        .filter(
            models.Event.olympic_id == olympic_2004.olympic_id,  # type: ignore
            models.Result.medal == "GOLD",
        )
        .group_by("birth_year")
        .order_by("birth_year")
        .all()
    )

    for row in results:
        birth_year = int(row.birth_year)
        num_players = row.num_players
        num_gold_medals = row.num_gold_medals
        print(
            f"Год рождения: {birth_year}, Количество игроков: {num_players}, Количество золотых медалей: {num_gold_medals}"
        )


def query_2(session: Session) -> None:
    subquery = (
        session.query(
            models.Result.event_id,
            models.Result.result,  # type: ignore
            al.func.count(models.Result.player_id).label("num_gold_medalists"),
        )
        .join(models.Event, models.Result.event_id == models.Event.event_id)
        .filter(
            models.Event.is_team_event == 0,
            models.Result.medal == "GOLD",
        )
        .group_by(
            models.Result.event_id,
            models.Result.result,  # type: ignore
        )
        .having(al.func.count(models.Result.player_id) >= 2)
        .subquery()
    )

    events = (
        session.query(
            models.Event.name, subquery.c.num_gold_medalists, subquery.c.result
        )
        .join(subquery, models.Event.event_id == subquery.c.event_id)
        .all()
    )

    for event_name, num_gold_medalists, result in events:
        print(
            f"Событие: {event_name}, Количество золотых медалистов: {num_gold_medalists}, Результат: {result}"
        )


def query_3(session: Session) -> None:
    results = (
        session.query(models.Player.name, models.Event.olympic_id)
        .join(models.Result, models.Player.player_id == models.Result.player_id)
        .join(models.Event, models.Result.event_id == models.Event.event_id)
        .filter(models.Result.medal.in_(["GOLD", "SILVER", "BRONZE"]))
        .group_by(models.Player.name, models.Event.olympic_id)
        .order_by(models.Player.name)
        .all()
    )

    for player_name, olympic_id in results:
        print(f"Игрок: {player_name}, Олимпиада ID: {olympic_id}")


def query_4(session: Session) -> None:
    vowels = ("A", "E", "I", "O", "U")

    total_players_subq = (
        session.query(
            models.Player.country_id,
            al.func.count(models.Player.player_id).label("total_players"),
        )
        .group_by(models.Player.country_id)
        .subquery()
    )

    vowel_players_subq = (
        session.query(
            models.Player.country_id,
            al.func.count(models.Player.player_id).label("vowel_players"),
        )
        .filter(
            al.func.upper(al.func.substr(al.func.trim(models.Player.name), 1, 1)).in_(
                vowels
            )
        )
        .group_by(models.Player.country_id)
        .subquery()
    )

    percentage_query = (
        session.query(
            models.Country.name,
            (
                al.cast(vowel_players_subq.c.vowel_players, al.Float)
                / total_players_subq.c.total_players
                * 100
            ).label("percentage"),
        )
        .join(
            total_players_subq,
            models.Country.country_id == total_players_subq.c.country_id,
        )
        .join(
            vowel_players_subq,
            models.Country.country_id == vowel_players_subq.c.country_id,
        )
        .order_by(
            (
                al.cast(vowel_players_subq.c.vowel_players, al.Float)
                / total_players_subq.c.total_players
            ).desc()
        )
        .first()
    )

    if percentage_query:
        print(
            f"Страна: {percentage_query.name}, Процент: {percentage_query.percentage:.2f}%"
        )
    else:
        print("Нет данных для расчета.")


def query_5(session: Session):
    olympic_2000 = (
        session.query(models.Olympic).filter(models.Olympic.year == 2000).first()
    )
    olympic_id_2000 = olympic_2000.olympic_id  # type: ignore

    team_medals_subq = (
        session.query(
            models.Player.country_id,
            al.func.count(models.Result.medal).label("team_medals"),
        )
        .join(models.Result, models.Player.player_id == models.Result.player_id)
        .join(models.Event, models.Result.event_id == models.Event.event_id)
        .filter(
            models.Event.is_team_event == 1,  # Групповые события
            models.Event.olympic_id == olympic_id_2000,
            models.Result.medal.isnot(None),
        )
        .group_by(models.Player.country_id)
        .subquery()
    )

    population_subq = session.query(
        models.Country.country_id,
        models.Country.population.label("population"),
    ).subquery()

    ratio_query = (
        session.query(
            models.Country.name,
            (
                al.cast(team_medals_subq.c.team_medals, al.Float)
                / population_subq.c.population
            ).label("ratio"),
        )
        .join(
            team_medals_subq,
            models.Country.country_id == team_medals_subq.c.country_id,
        )
        .join(
            population_subq,
            models.Country.country_id == population_subq.c.country_id,
        )
        .order_by(
            (
                al.cast(team_medals_subq.c.team_medals, al.Float)
                / population_subq.c.population
            )
        )
        .limit(5)
        .all()
    )

    for country_name, ratio in ratio_query:
        print(f"Страна: {country_name}, Соотношение: {ratio}")
