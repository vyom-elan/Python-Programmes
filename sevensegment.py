#Python Programme displaying 4 Seven Segment
#Sample Number to be displayed = 64:53
seven_segment= {
    '0': 'abcdef',
    '1': 'bc',
    '2': 'abdeg',
    '3': 'abcdg',
    '4': 'bcfg',
    '5': 'acdfg',
    '6': 'acdefg',
    '7': 'abc',
    '8': 'abcdefg',
    '9': 'abcdfg'
}

def display_number_so(number):
    pattern = seven_segment[str(number)]
    for segment in 'abcdefg':
        if segment in pattern:
            print('1', end=' ')  #give res in the form of 0 and 1
        else: 
            print('0', end=' ')
    print()
def display_number_st(number):
    pattern = seven_segment[str(number)]
    for segment in 'abcdefg':
        if segment in pattern:
            print('1', end=' ')  #give res in the form of 0 and 1
        else: 
            print('0', end=' ')
    print()
def display_number_mo(number):
    pattern = seven_segment[str(number)]
    for segment in 'abcdefg':
        if segment in pattern:
            print('1', end=' ')  #give res in the form of 0 and 1
        else: 
            print('0', end=' ')
    print()
def display_number_mt(number):
    pattern = seven_segment[str(number)]
    for segment in 'abcdefg':
        if segment in pattern:
            print('1', end=' ')  #give res in the form of 0 and 1
        else: 
            print('0', end=' ')
    print()
display_number_so(3)
display_number_st(5)
display_number_mo(4)
display_number_mt(6)
