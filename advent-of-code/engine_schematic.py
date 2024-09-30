from puzzle_input import fetch_input
from utilities import find_number_indexes,find_symbol_indexes
import json

example_input = """467%.114..
...*......
..35..633.
......#...
617*......
..$..+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def find_parts(input_lines):

      # I need to look at 2 lines at a time and record the index of each symbol
      previous_line = {
            'input_line_index': None,
            'previous_line_numbers': [],
            'previous_line_symbols': []
      }
      current_line = {
            'input_line_index': None,
            'current_line_numbers': [],
            'current_line_symbols': []
      }

      found_parts = set()
      
      for input_line_index, input_line in enumerate(input_lines):

            #assign the 2 lines to compare
            
            previous_line['input_line_index'] = current_line['input_line_index']
            previous_line['previous_line_numbers'] = current_line['current_line_numbers']
            previous_line['previous_line_symbols'] = current_line['current_line_symbols']

            current_line['input_line_index'] = input_line_index
            current_line['current_line_numbers'] = find_number_indexes(input_line)
            current_line['current_line_symbols'] = find_symbol_indexes(input_line)


            #current line: check if symbol is adjacent to number
            for symbol in current_line['current_line_symbols']:
                  symbol_index = symbol['symbol_indexes'][0]
                  for number in current_line['current_line_numbers']:
                        for index in number['number_indexes']:
                              if symbol_index == index - 1 or symbol_index == index + 1:
                                    found_parts.add(json.dumps(number))

            if previous_line['input_line_index']:

                  #current line: check if symbol is adjacent to number on previous line
                  for symbol in current_line['current_line_symbols']:
                        symbol_index = symbol['symbol_indexes'][0]
                        for number in previous_line['previous_line_numbers']:
                              for index in number['number_indexes']:
                                    if symbol_index == index or symbol_index == index - 1 or symbol_index == index + 1:
                                          found_parts.add(json.dumps(number))
                  #previous line: check if symbol is adjacent to number on current line
                  for symbol in previous_line['previous_line_symbols']:
                        symbol_index = symbol['symbol_indexes'][0]
                        for number in current_line['current_line_numbers']:
                              for index in number['number_indexes']:
                                    if symbol_index == index or symbol_index == index - 1 or symbol_index == index + 1:
                                          found_parts.add(json.dumps(number))
                  #check if number has already been added to found parts

      return found_parts

def sum_engine_parts(input):
      #create an array of input lines
      input_lines = input.splitlines()
      #find valid parts
      found_parts = find_parts(input_lines)
      print(found_parts)

sum_engine_parts(example_input)