password_rule_mapping = []

with open('2020day2input', 'r', encoding='utf-8') as fo:
    for line in fo:
        rule_num, rule_letter, password = line.split()
        lower_bound = int(rule_num.split('-')[0])
        upper_bound = int(rule_num.split('-')[1])
        letter = rule_letter.split(':')[0]
        password_rule_mapping.append((password, lower_bound, upper_bound, letter))

print('part 1')
num_valid_passwords = 0
for entry in password_rule_mapping:
    password = entry[0]
    lower_bound = entry[1]
    upper_bound = entry[2]
    letter = entry[3]
    count = len([c for c in password if c == letter])
    #print(password, count, lower_bound, upper_bound, letter)
    if count >= lower_bound and count <= upper_bound:
        #print('valid')
        num_valid_passwords += 1
print(num_valid_passwords)

print('part 2')
num_valid_passwords = 0
for entry in password_rule_mapping:
    password = entry[0]
    position1 = entry[1]
    position2 = entry[2]
    letter = entry[3]
    print(password, position1, position2, letter)
    if (password[position1 - 1] == letter) ^ (password[position2 - 1] == letter):
        print('valid')
        num_valid_passwords += 1
print(num_valid_passwords)
