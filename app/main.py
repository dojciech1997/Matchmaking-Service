from fastapi import FastAPI
from matchmaking import MatchmakingService

app = FastAPI()

matchmaking_service = MatchmakingService()

app.post("/join")
async def join_queue(player: str):
    game_id = matchmaking_service.add_player_to_queue(player)
    if game_id:
        return {"message": "Game started", "game_id": game_id}
    return {"message": "Waiting for another player"}
