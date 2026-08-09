from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional


# line color
class Color_line():
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    RESET: str = "\033[0m"


# SpaceStation class inherit from BaseModel
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str | None] = Field(default=None, max_length=200)

    def display_model(self) -> None:
        print(f"{Color_line.GREEN}Valid station created:{Color_line.RESET}")
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print("Status: Operational") if self.is_operational\
            else print("Status: No Operational")


if __name__ == "__main__":
    # valide space station model
    valide_model = {
        'station_id': 'LGW723',
        'name': 'Mars Orbital Platform',
        'crew_size': 11,
        'power_level': 90.8,
        'oxygen_level': 87.3,
        'last_maintenance': '2023-08-24T20:00:00',
        'is_operational': True,
        'notes': 'System diagnostics required'
    }
    # invalide space station model
    invalide_model = {
        'station_id': 'LGW723',
        'name': 'Mars Orbital Platform',
        'crew_size': 22,
        'power_level': 0,
        'oxygen_level': 87.3,
        'last_maintenance': '2023-09-25T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    }
    print("Space Station Data Validation\n"
          "=======================================")
    try:
        valide_space_station: SpaceStation = SpaceStation\
            .model_validate(valide_model)
        valide_space_station.display_model()
        print("=======================================")
        print("Expected validation error:")
        invalide_space_station: SpaceStation = SpaceStation\
            .model_validate(invalide_model)
        invalide_space_station.display_model()
    except ValidationError as err:
        for e in err.errors():
            # check if the field is missing
            # and display the field with message error
            if e['type'] == 'missing':
                print(f"{Color_line.RED}"
                      f"{e.get('msg')}: {e.get('loc')[0]}"
                      f"{Color_line.RESET}")
            else:
                print(f"{Color_line.RED}{e.get('msg')}{Color_line.RESET}")
    except Exception as err:
        print(err)
