# Library imports
import os

# File imports
import file_manipulator as fm

# Error imports
from Errors import TooManyInvalidTriesError


class SoftUni:

    def __init__(self):
        directory = [file[2:] for file in os.listdir("Advanced")[:-3]] # -> ['Stacks, Queues, Tuples and Sets', 'Multidimensional Lists', 'Functions Advanced', 'Error Handling', 'File Handling']
        # print(directory)
        self.directory = {index: file for index, file in enumerate(directory)} # -> {0: 'Stacks, Queues, Tuples and Sets', 1: 'Multidimensional Lists', 2: 'Functions Advanced', 3: 'Error Handling', 4: 'File Handling'}
        # print(self.directory)

    def get_path(self):

        for index, file in self.directory.items():
            print(f"[{index}] {file}")

        print()

        loop_breaker = 0
        path = input("Choose path by its number: ")
        while path not in ["0", "1", "2", "3", "4"]:
            loop_breaker += 1

            for index, file in self.directory.items():
                print(f"[{index}] {file}")

            print()

            path = input("Choose path by its number: ")

            if loop_breaker == 10:
                raise TooManyInvalidTriesError("Too many tries! Take a break.")

        path_number = int(path)

        return path_number

    def get_exercises(self, path_num: int):

        # Getting Exercises
        directory = [file for file in os.listdir("Advanced")[:-3]]
        dir = {index: file for index, file in enumerate(directory)}

        dipat = os.listdir(f"Advanced/{dir[path_num]}")

        dirpath = {index: file for index, file in enumerate(dipat)}

        for index, file in dirpath.items():
            print(f"[{index}] {file}")

        print()

        loop_breaker = 0
        path = input("Choose path by its number: ")
        while path not in [str(index) for index in range(0, len(dirpath))]:
            loop_breaker += 1

            for index, file in dirpath.items():
                print(f"[{index}] {file}")

            print()

            path = input("Choose path by its number: ")

            if loop_breaker == 10:
                raise TooManyInvalidTriesError("Too many tries! Take a break.")

        path_number = int(path)

        # Appending exercises
        exercises = os.listdir(f"Advanced/{dir[path_num]}/{dirpath[path_number]}")

        #
        # Printing Exercises
        build_link_demo = "https://github.com/MitkoVtori/SoftUni-Python-Advanced-OOP-2023-01/tree/main/Advanced"

        exercises_dict = {} # Will need this for the result.html and result.txt

        for exercise in exercises:
            exercise_link = f"{build_link_demo}/{(dir[path_num])}/{dirpath[path_number]}/{exercise}"

            #
            # Validating url
            exercise_link = exercise_link.replace(" ", "%20")
            exercise_link = exercise_link.replace("?", "%3F")
            exercise_link = exercise_link.replace("!", "%21")
            exercise_link = exercise_link.replace("@", "%40")
            exercise_link = exercise_link.replace("=", "%3D")
            exercise_link = exercise_link.replace("&", "%26")
            exercise_link = exercise_link.replace("$", "%24")
            exercise_link = exercise_link.replace("‘", "%60")
            exercise_link = exercise_link.replace("'", "%27")
            exercise_link = exercise_link.replace("*", "%2A")
            exercise_link = exercise_link.replace(",", "%2C")
            #
            #

            # Appending the exercise in the exercises dict
            exercises_dict[exercise] = exercise_link

            # Printing result
            print(f"{exercise} ", exercise_link, "\n")

        return exercises_dict

    def save_result_html(self, exercises: dict):
        # Create file or if it exists, remove content
        fm.create_file("result.html")

        # Creating html page
        html = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>SoftUni Advanced Exercises Solutions</title></head><body style="background-color: #272529"><h1 style="color: #FFF416; font-size: 50px; margin-left: 50px;">### Result</h1>'''

        for exercise, exercise_link in exercises.items():
            # Appending every exercise
            result = f"""<h2 style="color: #CA38F5; font-size: 40px; margin-left: 50px;">{exercise} -<a style="color: #17CEDD" href="{exercise_link}"> https://github.com/softuni/judge/{'%20'.join(exercise.split())}</a></h2>"""
            html += result

        # Adding some info
        html += '''<h2 style="color: #CA38F5; font-size: 20px; margin-left: 10px;">GitHub MitkoVtori: <a style="color: #17CEDD" href="https://github.com/MitkoVtori">https://github.com/MitkoVtori</a></h2><h2 style="color: #CA38F5; font-size: 20px; margin-left: 10px;">If there's an Error, please submit it here: <a style="color: #17CEDD" href="https://github.com/MitkoVtori/softuni_exercise_solutions/issues/new/choose">https://github.com/softuni%20exercise%20solutions</a></h2>'''

        # Finishing page
        html += "</body></html>"

        fm.add_content("result.html", html)

    def save_result_txt(self, exercises: dict):
        # Create file or if it exists, remove content
        fm.create_file("result.txt")

        for exercise, exercise_link in exercises.items():
            fm.add_content("result.txt", f"{exercise} - {exercise_link}\n")
        fm.add_content("result.txt", "\nGitHub MitkoVtori: https://github.com/MitkoVtori\nif there's an Error, please submit it here: https://github.com/MitkoVtori/softuni_exercise_solutions/issues/new/choose")

    def __repr__(self):
        return '''

the result of your search is saved in result.txt and result.html

GitHub MitkoVtori: https://github.com/MitkoVtori
If there's an Error, please submit it here: https://github.com/MitkoVtori/softuni_exercise_solutions/issues/new/choose
'''


softuni = SoftUni()

pth = softuni.get_path()
exs = softuni.get_exercises(pth)

softuni.save_result_html(exs)
softuni.save_result_txt(exs)

print(softuni)
