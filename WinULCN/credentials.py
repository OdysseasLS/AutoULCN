with open('Credentials_copy.txt', 'r') as file:

    for line in file:
        variable, value = line.strip().split(' = ')
        value = value.strip('"')
        exec(f'{variable} = "{value}"')