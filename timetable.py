import pandas as pd

def read_subjects_csv(file_path='subjects.csv'):
    subjects_df = pd.read_csv(file_path)
    return subjects_df

def read_weekly_schedule_csv(file_path='weekly_schedule.csv'):
    schedule_df = pd.read_csv(file_path, index_col=0)
    return schedule_df

def map_subjects_to_schedule(subjects_df, schedule_df):
    mapped_schedule_df = schedule_df.copy()

    for day in mapped_schedule_df.index:
        for period in mapped_schedule_df.columns:
            subject_code = mapped_schedule_df.loc[day, period]
            subject_name = subjects_df.loc[subjects_df['Subject Codes'].str.contains(subject_code), 'Subject Name'].values
            if subject_name:
                mapped_schedule_df.loc[day, period] = subject_name[0]
    
    return mapped_schedule_df

def save_timetable_to_csv(timetable_df, file_path='timetable.csv'):
    timetable_df.to_csv(file_path)
    print(f"Timetable saved to '{file_path}'.")

def main():
    # Read subjects and weekly schedule CSVs
    subjects_df = read_subjects_csv()
    weekly_schedule_df = read_weekly_schedule_csv()

    # Map subjects to the weekly schedule
    mapped_schedule_df = map_subjects_to_schedule(subjects_df, weekly_schedule_df)

    # Display the new timetable with subjects
    print("\nWeekly Schedule with Subjects:")
    print(mapped_schedule_df)

    # Save the new timetable to a CSV file
    save_timetable_to_csv(mapped_schedule_df)

if __name__ == "__main__":
    main()
