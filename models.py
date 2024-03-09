from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class ParticipantDefault(SQLModel):
    name: str
    email: str
    contact_number: str


class Participant(ParticipantDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    teams: List["Team"] = Relationship(back_populates="participants")


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    participants: List[Participant] = Relationship(back_populates="teams")
    tasks: List["Task"] = Relationship(back_populates="team")


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    requirements: str
    evaluation_criteria: str
    team_id: int = Field(foreign_key="team.id")
    team: Team = Relationship(back_populates="tasks")
    submissions: List["Submission"] = Relationship(back_populates="task")


class Submission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    participant_id: int = Field(foreign_key="participant.id")
    task_id: int = Field(foreign_key="task.id")
    submission_data: str
    participant: Participant = Relationship(back_populates="submissions")
    task: Task = Relationship(back_populates="submissions")
    evaluation: Optional[str]


class Hackathon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    start_date: str
    end_date: str
    tasks: List[Task] = Relationship(back_populates="hackathon")


class HackathonParticipant(SQLModel, table=True):
    participant_id: int = Field(foreign_key="participant.id", primary_key=True)
    hackathon_id: int = Field(foreign_key="hackathon.id", primary_key=True)
    role: str  # Additional field characterizing the relationship
