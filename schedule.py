import pandas as pd
from itertools import combinations
from datetime import datetime, timedelta

def create_schedule(input_file, output_file, start_time="10:00", interval_minutes=30):
    # Read names from Excel
    df = pd.read_excel(input_file)
    names = df.iloc[:, 0].dropna().tolist()  # Take first column, drop blanks

    # Shuffle to avoid bias (optional)
    import random
    random.shuffle(names)

    # Ensure number of names is multiple of 4
    if len(names) % 4 != 0:
        print("⚠️ Warning: Number of participants is not divisible by 4. Some may be left out.")
    
    # Time slots setup
    base_time = datetime.strptime(start_time, "%H:%M")
    
    schedule = []
    for i in range(0, len(names), 4):
        group = names[i:i+4]
        if len(group) < 4:  # Skip incomplete groups
            break
        # Split into 2v2
        team1 = ", ".join(group[:2])
        team2 = ", ".join(group[2:])
        
        match_time = base_time + timedelta(minutes=(i//4)*interval_minutes)
        
        schedule.append({
            "Time": match_time.strftime("%H:%M"),
            "Team 1": team1,
            "Team 2": team2
        })

    # Convert to DataFrame
    schedule_df = pd.DataFrame(schedule)

    # Save to Excel
    schedule_df.to_excel(output_file, index=False)
    print(f"✅ Schedule saved to {output_file}")


# Example usage
create_schedule("participants.xlsx", "contest_schedule.xlsx", start_time="10:00", interval_minutes=30)
