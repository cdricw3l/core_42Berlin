from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime
from typing import Optional, Any, Self


class Color_line():
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    RESET: str = "\033[0m"


# Contact type Enum
class ContactType(Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


# AlienContact class inherit from BaseModel
class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str | None]\
        = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    # custom model validation rules
    @model_validator(mode='after')
    def custom_validation(self) -> Self:
        if self.contact_id[0:2] != 'AC':
            raise Exception(f"{Color_line.RED}"
                            f"Contact ID must start with 'AC' (Alien Contact)."
                            f"{Color_line.RESET}")
        if self.contact_type.value == ContactType.physical.value \
                and self.is_verified is False:
            raise Exception(f"{Color_line.RED}"
                            f"Physical contact reports must be verified."
                            f"{Color_line.RESET}")
        if self.contact_type.value == ContactType.telepathic.value\
                and self.witness_count < 3:
            raise Exception(f"{Color_line.RED}"
                            f"Telepathic contact requires "
                            "at least 3 witnesses."
                            f"{Color_line.RESET}")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise Exception(f"{Color_line.RED}"
                            f"Strong signals (> 7.0) "
                            "should include received messages."
                            f"{Color_line.RESET}")
        return self

    def display_model(self) -> None:
        print(f"{Color_line.GREEN}Valid contact report:{Color_line.RESET}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: {self.message_received}")


def validation_model_test(model: dict[str, Any]) -> None:
    try:
        alien: AlienContact = AlienContact.model_validate(model)
        alien.display_model()
        print()
    except ValidationError as err:
        for e in err.errors():
            if e['type'] == 'missing':
                print(f"{Color_line.RED}"
                      f"{e.get('msg')}: {e.get('loc')[0]}"
                      f"{Color_line.RESET}")
            else:
                print(f"{Color_line.RED}{e.get('msg')}{Color_line.RESET}")
        print()
    except Exception as err:
        print(err)


if __name__ == "__main__":

    # valide model
    valide_model = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }
    # invalide model: Contact ID must start with "AC" (Alien Contact)
    invalide_model_1 = {
        'contact_id': 'CA_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }
    # invalide model: physical contact reports must be verified
    invalide_model_2 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': False
    }
    # invalide model: telepathic contact_type requires at least 3 witnesses
    invalide_model_3 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'telepathic',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 2,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': False
    }
    # Strong signals (> 7.0) should include received messages
    invalide_model_4 = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': None,
        'is_verified': True
    }

    print("Space Station Data Validation\n"
          "=======================================")
    validation_model_test(valide_model)
    validation_model_test(invalide_model_1)
    validation_model_test(invalide_model_2)
    validation_model_test(invalide_model_3)
    validation_model_test(invalide_model_4)
