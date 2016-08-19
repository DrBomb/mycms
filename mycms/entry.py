from App import create_app
import os

if os.getenv("REACT") is not None:  
    from settings import react_settings as settings
    print("React Mode Running")
elif os.getenv("DEBUG"):
    from settings import debug_settings as settings
    print("Debug Mode Running")
else:
    from settings import base_settings as settings

app = create_app(settings)

if __name__ == "__main__":
    app.run()
