def love_calculator():
    print("Welcome to the love calculator!")
    your_name = input("Please enter your name:\n").lower()
    partner_name = input("Please enter your partner's name:\n").lower()
    combined_name = your_name + partner_name
    true_count = 0
    love_count = 0
    for char in "true":
        true_count += combined_name.count(char)
    for char in "love":
        love_count += combined_name.count(char)
    combined_count = str(true_count) + str(love_count)
    print(combined_count)
love_calculator()
