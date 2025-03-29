from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    TAPS_AMOUNT: list[int] = [10, 20]
    SLEEP_AFTER_TAP: list[int] = [6, 10]
    SLEEP_NOT_ENOUGH_TAPS: list[int] = [2000, 3600]

    SPIN_THE_WHEEL: bool = True
    CLAIM_REFERRALS_REWARD: bool = True
    CLAIM_COLLECTIONS_CARDS: bool = True
    UPGRADE_CARDS: bool = False

settings = Settings()
