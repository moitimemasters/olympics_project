import datetime as dt
import random

import faker
import models
from sqlalchemy.orm import Session


def populate_database(session: Session):
    fake = faker.Faker()
    faker.Faker.seed(0)

    countries = list[models.Country]()
    for _ in range(10):
        country = models.Country(
            name=fake.country(),
            country_id=fake.unique.country_code(),
            area_sqkm=random.randint(1000, 17_098_242),
            population=random.randint(100_000, 1_400_000_000),
        )
        countries.append(country)
    session.add_all(countries)
    session.commit()

    # Создание Олимпиад
    olympic_years = [2000, 2004, 2008, 2012, 2016, 2020]
    olympics = list[models.Olympic]()
    for year in olympic_years:
        olympic = models.Olympic(
            olympic_id=f"O{year}",
            country_id=random.choice(countries).country_id,
            city=fake.city(),
            year=year,
            startdate=dt.datetime(year, 7, 15).date(),
            enddate=dt.datetime(year, 8, 1).date(),
        )
        olympics.append(olympic)
    session.add_all(olympics)
    session.commit()

    # Создание игроков
    players = list[models.Player]()
    for _ in range(100):
        player = models.Player(
            name=fake.name(),
            player_id=fake.unique.lexify(text="P?????"),
            country_id=random.choice(countries).country_id,
            birthdate=fake.date_of_birth(minimum_age=15, maximum_age=40),
        )
        players.append(player)
    session.add_all(players)
    session.commit()

    events = list[models.Event]()
    for _ in range(50):
        is_team = random.randint(0, 1)
        event = models.Event(
            event_id=fake.unique.lexify(text="E?????"),
            name=f"{fake.word().capitalize()} {fake.word().capitalize()}",
            eventtype=random.choice(["Sport", "Game", "Competition"]),
            olympic_id=random.choice(olympics).olympic_id,
            is_team_event=is_team,
            num_players_in_team=random.randint(2, 11) if is_team else None,
            result_noted_in=random.choice(["Time", "Score", "Distance"]),
        )
        events.append(event)
    session.add_all(events)
    session.commit()

    medals = ("GOLD", "SILVER", "BRONZE", None)
    results = list[models.Result]()
    for event in events:
        participants = random.sample(players, random.randint(3, 20))
        tie_result = random.uniform(9.0, 15.0)
        for idx, player in enumerate(participants):
            if idx < 2 and event.is_team_event == 0:  # type: ignore
                medal = "GOLD"
                result_value = tie_result
            else:
                medal = random.choice(medals)
                result_value = random.uniform(10.0, 100.0)
            result = models.Result(
                event_id=event.event_id,
                player_id=player.player_id,
                medal=medal,
                result=result_value,
            )
            results.append(result)
    session.add_all(results)
    session.commit()
