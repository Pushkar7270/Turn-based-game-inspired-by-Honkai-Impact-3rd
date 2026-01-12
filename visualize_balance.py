import matplotlib.pyplot as plt
import File_handler as fh
import numpy as np

def create_visualizations():
    data = fh.load_data("Balance_Report.json")
    if not data:
        print("Error: Balance_Report.json not found")
        return
    
    # 1. Win Rate Comparison
    win_data = data["Win_Rate_Discrepancy"]
    categories = list(win_data.keys())
    win_rates = [float(win_data[cat]["win_rate"].replace('%', '')) for cat in categories]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, win_rates, color=['#FF6B6B', '#4ECDC4'])
    plt.title('Win Rate Comparison: Bots vs Human Players')
    plt.ylabel('Win Rate (%)')
    plt.ylim(0, 100)
    
    for bar, rate in zip(bars, win_rates):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{rate}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('win_rate_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. Top Moves by Damage
    move_data = data["Move_Effectiveness"]["top_5_moves_by_average_damage_dealt"]
    move_names = [move["move_name"] for move in move_data]
    damages = [float(move["average_damage_dealt"]) for move in move_data]
    
    plt.figure(figsize=(12, 6))
    bars = plt.barh(move_names, damages, color='#FF9F43')
    plt.title('Top 5 Moves by Average Damage')
    plt.xlabel('Average Damage')
    
    for bar, damage in zip(bars, damages):
        plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                f'{damage:.0f}', ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('top_moves_damage.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 3. Hit Rate vs Damage Scatter
    all_moves = data["Move_Effectiveness"]["all_moves_analysis"]
    hit_rates = [float(move["hit_rate_percent"].replace('%', '')) for move in all_moves]
    avg_damages = [float(move["average_damage_dealt"]) for move in all_moves]
    move_names = [move["move_name"] for move in all_moves]
    
    plt.figure(figsize=(10, 8))
    plt.scatter(hit_rates, avg_damages, s=100, alpha=0.7, c='#6C5CE7')
    plt.xlabel('Hit Rate (%)')
    plt.ylabel('Average Damage')
    plt.title('Move Effectiveness: Hit Rate vs Average Damage')
    
    for i, name in enumerate(move_names):
        plt.annotate(name, (hit_rates[i], avg_damages[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('hit_rate_vs_damage.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 4. Strategy Comparison
    strategy_data = data["Strategy_Extraction"]
    if "player_move_frequencies_human_players" in strategy_data:
        human_data = strategy_data["player_move_frequencies_human_players"]
        bot_data = strategy_data["player_move_frequencies_simulation_bots"]
        
        if "Kiana Kaslana" in human_data and "Kiana Kaslana" in bot_data:
            human_moves = human_data["Kiana Kaslana"]
            bot_moves = bot_data["Kiana Kaslana"]
            
            moves = list(human_moves.keys())
            human_percentages = [float(human_moves[move]["percentage"].replace('%', '')) for move in moves]
            bot_percentages = [float(bot_moves[move]["percentage"].replace('%', '')) for move in moves]
            
            x = np.arange(len(moves))
            width = 0.35
            
            plt.figure(figsize=(12, 6))
            plt.bar(x - width/2, human_percentages, width, label='Human Players', color='#00B894')
            plt.bar(x + width/2, bot_percentages, width, label='Bot Players', color='#E17055')
            
            plt.xlabel('Moves')
            plt.ylabel('Usage Percentage (%)')
            plt.title('Kiana Kaslana: Human vs Bot Move Usage')
            plt.xticks(x, moves, rotation=45)
            plt.legend()
            
            plt.tight_layout()
            plt.savefig('strategy_comparison.png', dpi=300, bbox_inches='tight')
            plt.show()
    
    print("All visualizations saved as PNG files!")

if __name__ == "__main__":
    create_visualizations()