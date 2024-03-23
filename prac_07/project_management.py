"""
CP1404/CP5632 Practical 7 - Client code to use the Project  class.
Estimate: 2 hours
Actual:   2.5 hours
"""
import datetime
from cp1404practicals.prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

FILE_NAME = 'project.txt'
NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
PERCENT_COMPLETE_INDEX = 4


def main():
    """The main function of the Project"""
    projects = load_projects(FILE_NAME)
    print(MENU)
    choice = input(">>> ").strip().lower()
    while choice != 'q':
        if choice == 'l':
            projects = load_projects(FILE_NAME)
            print("Projects loaded successfully.")
        elif choice == 's':
            save_projects(FILE_NAME, projects)
            print("Projects saved successfully.")
        elif choice == 'd':
            completed_projects, incomplete_projects = determine_incomplete_complete(projects)
            display_projects(completed_projects, incomplete_projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            try:
                date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
                filtered_projects = filter_projects_by_date(projects, date)
                sorted_filtered_projects = sorted(filtered_projects, key=sort_by_start_date)
                print("Filtered projects:")
                for project in sorted_filtered_projects:
                    print(project)
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            print("Projects:")
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            if 0 <= project_choice < len(projects):
                project = projects[project_choice]
                print(project)
                new_percent_complete = get_valid_input("New Percentage: ", project.percent_complete)
                new_priority = get_valid_input("New Priority: ", project.priority)
                project.percent_complete = new_percent_complete
                project.priority = new_priority
                print("Project updated successfully.")
            else:
                print("Invalid project choice.")
        else:
            print("Invalid choice. Please select a valid option.")
        print(MENU)
        choice = input(">>> ").strip().lower()

    print("Would you like to save to projects.txt? no, I think not.")
    print("Thank you for using custom-built project management software.")


def load_projects(file_name):
    """Load the date from the txt file and store in a list"""
    projects = []
    with open(file_name) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[NAME_INDEX]
            start_date = datetime.datetime.strptime(parts[DATE_INDEX].strip(), "%d/%m/%Y").date()
            priority = int(parts[PRIORITY_INDEX])
            cost_estimate = float(parts[COST_INDEX])
            percent_complete = int(parts[PERCENT_COMPLETE_INDEX])
            project = Project(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(project)
    return projects


def save_projects(file_name, projects):
    """Save all the data from the list to the txt file"""
    with open(file_name, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                           f"\t{project.cost_estimate:.1f}\t{project.percent_complete}\n")


def display_projects(completed_projects, incomplete_projects):
    """Display the Project list """
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("Completed projects:")
    for project in completed_projects:
        print(project)


def determine_incomplete_complete(projects):
    """Determine which project is complete or incomplete """
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.percent_complete < 100:
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    return completed_projects, incomplete_projects


def filter_projects_by_date(projects, date):
    """Filter project list by the date """
    filtered_projects = [project for project in projects if project.start_date >= date]
    return filtered_projects


def add_new_project(projects):
    """Add new project to the projects"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate ($): "))
    percent_complete = int(input("Percent complete (%): "))
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)
    print("New project added successfully.")


def get_valid_date(prompt):
    """Get the valid date"""
    is_finished = False
    while not is_finished:
        date_str = input(prompt)
        try:
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            is_finished = True
            return date
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")


def get_valid_input(prompt, old_value):
    """Get valid input """
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            return old_value
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input; enter a valid number.")


def sort_by_start_date(project):
    """create a key to sort the this by """
    return project.start_date


main()