import requests

class MatchmakingService:
    def __init__(self):
        self.waiting_players = []

    def add_player_to_queue(self, player: str):
        self.waiting_players.append(player)
        if len(self.waiting_players) >= 2:
            player1 = self.waiting_players.pop(0)
            player2 = self.waiting_players.pop(0)
            return self.start_game(player1, player2)
        return None

    def start_game(self, player1: str, player2: str):
        url = "http://game-logic-service:8000/start-game"
        response = requests.post(url, json={"player1": player1, "player2": player2})
        if response.status_code == 200:
            game_id = response.json().get("game_id")
            return game_id
        return None

