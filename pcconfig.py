import pynecone as pc

class PoketypeConfig(pc.Config):
    pass

config = PoketypeConfig(
    app_name="poketype",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
