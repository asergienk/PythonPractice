from stack import Stack

def convert_int_to_bin(dec_num):
  my_stack = Stack()
  my_string = ''
  result = dec_num // 2
  remainder = dec_num - (result * 2)
  dec_num = result
  my_stack.push(remainder)
  while result != 0:
    result = dec_num // 2
    remainder = dec_num - (result * 2)
    dec_num = result
    my_stack.push(remainder)

  while not my_stack.is_empty():
    item = my_stack.pop()
    my_string += str(item)
  
  return my_string
 
