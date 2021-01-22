
def login(id)
    members = ['tom', 'jerry', 'snoopy']
    for member in members do
        if member == id
            return true
        end
    end
    return false
end


def real_login()
    puts("Enter your id!\n")
    input_id = gets.chomp
    if login(input_id)
        puts("Hello!, " +input_id)
    else
        puts("Check your id!")
    end
end


puts(real_login())