import sqlalchemy as al
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Country(Base):
    __tablename__ = "countries"
    name = al.Column(al.String(40))
    country_id = al.Column(al.String(3), primary_key=True)
    area_sqkm = al.Column(al.Integer)
    population = al.Column(al.Integer)
    players = relationship("Player", back_populates="country")
    olympics = relationship(
        "Olympic",
        back_populates="country",
        cascade="all, delete-orphan",
    )


class Olympic(Base):
    __tablename__ = "olympics"
    olympic_id = al.Column(al.String(7), primary_key=True)
    country_id = al.Column(al.String(3), al.ForeignKey("countries.country_id"))
    city = al.Column(al.String(50))
    year = al.Column(al.Integer)
    startdate = al.Column(al.Date)
    enddate = al.Column(al.Date)
    country = relationship("Country", back_populates="olympics")
    events = relationship(
        "Event",
        back_populates="olympic",
        cascade="all, delete-orphan",
    )


class Player(Base):
    __tablename__ = "players"
    name = al.Column(al.String(40))
    player_id = al.Column(al.String(10), primary_key=True)
    country_id = al.Column(al.String(3), al.ForeignKey("countries.country_id"))
    birthdate = al.Column(al.Date)
    country = relationship("Country", back_populates="players")
    results = relationship(
        "Result",
        back_populates="player",
        cascade="all, delete-orphan",
    )


class Event(Base):
    __tablename__ = "events"
    event_id = al.Column(al.String(7), primary_key=True)
    name = al.Column(al.String(40))
    eventtype = al.Column(al.String(20))
    olympic_id = al.Column(al.String(7), al.ForeignKey("olympics.olympic_id"))
    is_team_event = al.Column(al.Integer, al.CheckConstraint("is_team_event IN (0,1)"))
    num_players_in_team = al.Column(al.Integer)
    result_noted_in = al.Column(al.String(100))
    olympic = relationship("Olympic", back_populates="events")
    results = relationship(
        "Result", back_populates="event", cascade="all, delete-orphan"
    )


class Result(Base):
    __tablename__ = "results"
    event_id = al.Column(
        al.String(7),
        al.ForeignKey("events.event_id"),
        primary_key=True,
    )
    player_id = al.Column(
        al.String(10),
        al.ForeignKey("players.player_id"),
        primary_key=True,
    )
    medal = al.Column(al.String(7))
    result = al.Column(al.Float)  # type: ignore
    player = relationship("Player", back_populates="results")
    event = relationship("Event", back_populates="results")
