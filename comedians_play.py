# Assignment for Geowox
# Submission by Kunal Chaturvedi
# Dated - 22 January 2021

error = ""


def check_file_dimensions(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    if len(lines) > 0:
        line_count = int(lines[0])
        if line_count == (len(lines)-1):
            return True
    global error
    error = "The file does not have the number of lines as defined in the first line"
    return False


def check_file_legality(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    i = 0
    while i < len(lines):
        for character in lines[i]:
            if (48 > ord(character) or ord(character) > 57) and character != '\n' and character != ' ':
                global error
                error = "The file has a non integer character which is unexpected"
                return False
        i += 1
    return True


def check_file_dirty_lines(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    i = 1
    while i < len(lines):
        if lines[i]:
            line = lines[i].strip()
            two_numbers = line.split()
            if len(two_numbers) != 2:
                global error
                error = "The file has a line which is not in the expected format of two numbers separated by space"
                return False
        i += 1
    return True


def rev(num):
    reverse = 0
    while num > 0:
        d = num % 10
        reverse = reverse * 10 + d
        num = num//10
    return reverse


def primary_logic(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    for line in lines[1:]:
        line = line.strip()
        output = rev(sum([rev(int(num)) for num in line.split()]))
        print(output)


def main():

    file_path = input("Enter the file path: ")

    # We will have three preliminary checks for the file before moving on to the logic
    check_counter = 0
    if check_file_dimensions(file_path):
        check_counter += 1
    else:
        print(error)
        return

    if check_file_legality(file_path):
        check_counter += 1
    else:
        print(error)
        return

    if check_file_dirty_lines(file_path):
        check_counter += 1
    else:
        print(error)
        return

    # After passing through preliminary checks we will subject the file through the actual logic
    if check_counter == 3:
        primary_logic(file_path)


main()
