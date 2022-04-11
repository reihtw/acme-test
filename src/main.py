#!/usr/bin/env python3
from workhour.workhour import WorkHour


def main():

    file_lines = get_filelines('input.txt')
    
    workhours_list = list()
    relations_dict = dict()
    for file_line in file_lines:
        file_line = file_line.strip()
     
        employee_name, employee_workhours = file_line.split('=')
        
        for workhour in employee_workhours.split(','):
            workhour = WorkHour(employee_name, workhour)
            workhour.get_relations(workhours_list, relations_dict)
            workhours_list.append(workhour)
    
    print_result(relations_dict)
                

def get_filelines(file_name: str) -> list:
    with open(f'resources/{file_name}') as input_file:
        file_lines = input_file.readlines()
    return file_lines


def print_result(relations_dict: dict) -> None:
    for relation, amount in relations_dict.items():
        print(f'{relation}: {amount}')
    
if __name__ == '__main__':
    main()