from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    TAPS_AMOUNT: list[int] = [5, 8]
    SLEEP_AFTER_TAP: int = 2
    SLEEP_NOT_ENOUGH_TAPS: list[int] = [2000, 3600]

    SPIN_THE_WHEEL: bool = True
    CLAIM_REFERRALS_REWARD: bool = True


settings = Settings()
