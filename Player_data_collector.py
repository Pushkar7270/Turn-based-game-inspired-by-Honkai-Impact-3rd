import json
import os
from datetime import datetime


class PlayerDataCollector:
    def __init__(self, filename="player_data.json"):
        self.filename = filename
        self.current_battle = None
        
    def start_battle(self, player, boss):
        self.current_battle = {
            "battle_id": self._get_next_battle_id(),
            "timestamp": datetime.now().isoformat(),
            "match_up": f"{player.name} vs {boss.name}",
            "player_stats": {
                "name": player.name,
                "hp": player.max_hp,
                "speed": player.speed,
                "crit_rate": player.crit_rate,
                "defence": player.defence
            },
            "boss_stats": {
                "name": boss.name,
                "hp": boss.max_hp,
                "speed": boss.speed,
                "crit_rate": boss.crit_rate,
                "defence": boss.defence
            },
            "winner": None,
            "turns": [],
            "total_turns": 0
        }
        
    def log_turn(self, actor, move_used, damage_base, result_log, target_hp_remaining):
        if not self.current_battle:
            return
            
        turn_data = {
            "turn": len(self.current_battle["turns"]) + 1,
            "actor": actor,
            "move_used": move_used,
            "damage_base": damage_base,
            "result_log": result_log,
            "target_hp_remaining": max(0, target_hp_remaining)
        }
        self.current_battle["turns"].append(turn_data)
        
    def end_battle(self, winner):
        if not self.current_battle:
            return
            
        self.current_battle["winner"] = winner
        self.current_battle["total_turns"] = len(self.current_battle["turns"])
        self._save_battle_data()
        self.current_battle = None
        
    def _get_next_battle_id(self):
        existing_data = self._load_existing_data()
        return len(existing_data) + 1
        
    def _load_existing_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
            
    def _save_battle_data(self):
        existing_data = self._load_existing_data()
        existing_data.append(self.current_battle)
        
        with open(self.filename, 'w') as f:
            json.dump(existing_data, f, indent=2)