from dotenv import load_dotenv

from src.engine import SpotifyEngine

if __name__ == "__main__":
    load_dotenv()
    
    Engine = SpotifyEngine()
    Engine.start()
