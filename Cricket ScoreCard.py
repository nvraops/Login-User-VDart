print("*****Welcome to Cricket ScoreCard*****")

import time # To add a small delay for better readability

def play_innings(team_number, total_overs):
    """Simulates a single innings of cricket for a generic team with user-inputted ball progression."""
    score = 0
    wickets = 0
    balls_bowled = 0

    print(f"\n--- Team {team_number} Batting ---")
    print(f"Total overs: {total_overs}")

    for over in range(1, total_overs + 1):
        if wickets >= 10: # All out condition
            print(f"\nTeam {team_number} All Out!")
            break

        print(f"\n--- Over {over} ---")
        for ball_in_over in range(1, 7): # 6 balls per over
            if wickets >= 10: # Check again after each ball in case it was the 10th wicket
                break

            current_overs_display = balls_bowled // 6
            current_balls_display = balls_bowled % 6
            print(f"\nScore: {score}/{wickets} ({current_overs_display}.{current_balls_display} Overs)")

            user_input = ""
            while True:
                user_input = input(f"Enter outcome for Ball {ball_in_over} of Over {over} (0, 1, 2, 3, 4, 6, or 'W' for Wicket): ").strip().upper()
                if user_input in ['0', '1', '2', '3', '4', '6', 'W']:
                    break
                else:
                    print("Invalid input. Please enter 0, 1, 2, 3, 4, 6, or 'W'.")

            time.sleep(0.2) # Small delay for better UX

            balls_bowled += 1

            if user_input == "W":
                wickets += 1
                print(f"  > WICKET! {wickets} down.")
            else:
                runs = int(user_input)
                score += runs
                print(f"  > {runs} run(s) scored.")

            # Check if all overs are completed or all wickets are down
            if balls_bowled == total_overs * 6 or wickets >= 10:
                break
        
        if wickets >= 10: # Break outer loop if all out mid-over
            break

    print(f"\n--- End of Team {team_number} Innings ---")
    current_overs_display = balls_bowled // 6
    current_balls_display = balls_bowled % 6
    print(f"Final Score: {score}/{wickets} in {current_overs_display}.{current_balls_display} Overs")
    return score, wickets

# --- Match Simulation ---
if __name__ == "__main__":
    # You can change the number of overs here
    match_overs = 2 # Setting a very small number for quick demonstration

    print("--- User-Controlled Cricket Match ---")
    print(f"Match set for {match_overs} overs per innings.")

    # Innings 1 for Team 1
    team1_score, team1_wickets = play_innings(1, match_overs)

    # Innings 2 for Team 2
    team2_score, team2_wickets = play_innings(2, match_overs)

    print("\n--- Match Summary ---")
    print(f"Team 1: {team1_score}/{team1_wickets} in {match_overs} Overs")
    print(f"Team 2: {team2_score}/{team2_wickets} in {match_overs} Overs")

    if team1_score > team2_score:
        print(f"\nTeam 1 wins by {team1_score - team2_score} runs!")
    elif team2_score > team1_score:
        print(f"\nTeam 2 wins by {team2_score - team1_score} runs!")
    else:
        print("\nIt's a tie!")