def generate_feedback(data):
    game = data.get("game")
    matches = data.get("matches", 0)
    wins = data.get("wins", 0)
    mistakes = data.get("mistakes", 0)
    endgame_losses = data.get("endgame_losses", 0)
    safe_moves = data.get("safe_moves", 0)
    risky_moves = data.get("risky_moves", 0)

    if matches == 0:
        return "Play more matches to receive AI feedback."

    win_rate = (wins / matches) * 100

    advice = []

    if win_rate > 70:
        advice.append("Excellent performance. Maintain your strategy.")
    elif win_rate > 40:
        advice.append("Good performance. Focus on reducing mistakes.")
    else:
        advice.append("Low win rate. Improve decision-making.")

    if mistakes > safe_moves:
        advice.append("You take too many risky moves. Play safer.")
    else:
        advice.append("Good balance between risk and safety.")

    if endgame_losses > 5:
        advice.append("Work on endgame strategy and patience.")

    if game == "snake":
        advice.append("Avoid risky rolls near ladders and snakes.")
    elif game == "chess":
        advice.append("Improve opening control and endgame planning.")
    elif game == "ludo":
        advice.append("Prioritize safe zones and token coordination.")
    elif game == "uno":
        advice.append("Track opponent cards and manage wild cards wisely.")

    return " ".join(advice)
