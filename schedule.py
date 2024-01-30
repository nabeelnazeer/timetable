import pandas as pd

def create_schedule():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods = [f"Period {i}" for i in range(1, 9)]

    schedule_data = {day: ["" for _ in range(8)] for day in days_of_week}
    schedule_df = pd.DataFrame(schedule_data, index=periods)

    return schedule_df

def input_subject_codes(schedule_df):
    for day in schedule_df.columns:
        for period in schedule_df.index:
            subject_code = input(f"Enter subject code for {day}, {period}: ")
            schedule_df.loc[period, day] = subject_code

def main():
    schedule_df = create_schedule()

    print("Enter subject codes for each cell in the schedule:")
    input_subject_codes(schedule_df)

    print("\nWeekly Schedule:")
    print(schedule_df)

    # Save to CSV
    schedule_df.to_csv('weekly_schedule.csv')
    print("Weekly schedule saved to 'weekly_schedule.csv'.")

if __name__ == "__main__":
    main()
