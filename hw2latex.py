import jinja2
import os

# Custom jinja2 environment configured for LaTeX
latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('templates'))
)

print('DOCUMENT INPUT')
author = input('Your name: ')
class_name = input('Class name: ')
assignment_number = input('Assignment Number: ')
term = input('Term (i.e. Summer 2017): ')
due_date = input('Due Date: ')

problem_set = []
print('\n* PROBLEM INPUT *\n')
while True:
    number = input('Problem number: ')
    description = input('Problem description: ')
    excerpt = input('Short excerpt of problem: ')
    points = input('Points: ')
    #parts = []

    problem_set.append({'Points': points, 'Number': number,
                        'Description': description, 'Excerpt': excerpt})

    if input('Hit enter to continue. Type "exit" to exit. ') == 'exit':
        break

template = latex_jinja_env.get_template('template.tex')

homework = open('Assignment' + assignment_number + '.tex', 'w')
homework.write(template.render(
    author=author,
    class_name=class_name,
    assignment_number=assignment_number,
    term=term,
    due_date=due_date,
    problems=problem_set
))
