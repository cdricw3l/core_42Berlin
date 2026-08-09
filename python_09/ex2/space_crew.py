from pydantic import Field, ValidationError, BaseModel, model_validator
from enum import Enum
from datetime import datetime
from typing import Self, Any


class Color_line():
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    RESET: str = "\033[0m"


class RankEnum(Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> Self:
        # custom model validation rules
        if self.mission_id[0:1] != 'M':
            raise Exception(f"{Color_line.RED}"
                            f"Mission ID must start with 'M'."
                            f"{Color_line.RESET}")
        rank_check_list: list[CrewMember] = [member for
                                             member in self.crew
                                             if member.rank ==
                                             RankEnum.commander
                                             or
                                             member.rank == RankEnum.captain
                                             ]
        if len(rank_check_list) == 0:
            raise Exception(f"{Color_line.RED}"
                            f"Mission must have at least"
                            f" one Commander or Captain{Color_line.RESET}")
        if self.duration_days > 365:
            experience_check: list[CrewMember] = [member for
                                                  member in self.crew
                                                  if
                                                  member.years_experience > 5]
            if len(experience_check) < len(self.crew) / 2:
                raise Exception(f"{Color_line.RED}Long missions "
                                f"(> 365 days) need 50% experienced "
                                f"crew (5+ years){Color_line.RESET}")
        if len([member for
                member in self.crew if member.is_active is False]) > 0:
            raise Exception(f"{Color_line.RED}All crew members "
                            f"must be active{Color_line.RESET}")
        return self

    def display_model(self) -> None:
        print(f"{Color_line.GREEN}Valid mission created:{Color_line.RESET}")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for member in self.crew:
            print(f"- {member.name} "
                  f"({member.rank.value}) "
                  f"- {member.specialization}")


def mission_validation(model: dict[str, Any]) -> None:
    try:
        mission: SpaceMission = SpaceMission.model_validate(model)
        mission.display_model()
        print("\n=========================================")
    except ValidationError as err:
        print(err)
        for e in err.errors():
            if e['type'] == 'missing':
                print(f"{Color_line.RED}"
                      f"{e.get('msg')}: "
                      f"{e.get('loc')[0]}{Color_line.RESET}")
            else:
                print(f"{Color_line.RED}{e.get('msg')}{Color_line.RESET}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")

    valide_mission: dict[str, Any] = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'commander',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2550.1
    }
    invalide_mission: dict[str, Any] = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 1,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 1,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 10,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'cadet',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2550.1
    }

    mission_validation(valide_mission)
    print("Expected validation error:")
    mission_validation(invalide_mission)
