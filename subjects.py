import csv
import os

class Node:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.subject_codes = []
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_subject(self, subject_name, subject_codes):
        if not self.head or self.head.subject_name != subject_name:
            new_node = Node(subject_name)
            new_node.subject_codes.extend(subject_codes)
            new_node.next_node = self.head
            self.head = new_node
        else:
            self.head.subject_codes.extend(subject_codes)

    def display_subjects(self):
        current_node = self.head
        while current_node:
            print(f"Subject Name: {current_node.subject_name}, Subject Codes: {', '.join(current_node.subject_codes)}")
            current_node = current_node.next_node

    def to_csv(self, filename='subjects.csv'):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Subject Name', 'Subject Codes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            current_node = self.head
            while current_node:
                writer.writerow({'Subject Name': current_node.subject_name,
                                 'Subject Codes': ', '.join(current_node.subject_codes)})
                current_node = current_node.next_node

def main():
    subject_list = LinkedList()

    num_subjects = int(input("Enter the number of subjects: "))
    for _ in range(num_subjects):
        subject_name = input("Enter subject name: ")
        num_codes = int(input(f"Enter the number of codes for {subject_name}: "))
        subject_codes = [input(f"Enter subject code {i + 1}: ") for i in range(num_codes)]
        subject_list.add_subject(subject_name, subject_codes)

    print("\nList of Subjects:")
    subject_list.display_subjects()

    # Get the current directory
    current_directory = os.getcwd()

    # Save to CSV in the current directory
    csv_file_path = os.path.join(current_directory, 'subjects.csv')
    subject_list.to_csv(filename=csv_file_path)
    print(f"Subjects saved to '{csv_file_path}'.")

if __name__ == "__main__":
    main()
