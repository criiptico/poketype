import pynecone as pc

class MainConfig(pc.Config):
    pass

config = MainConfig(
    app_name="main",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
