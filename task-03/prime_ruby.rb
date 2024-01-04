def is_prime(n)
    if n <= 1
        return false
    end
    for i in 2..(n - 1)
        if n % i == 0
            return false
        end
    end
    return true
end

def print_prime(n)
    for i in 2..n
        if is_prime(i)
            print "#{i} "
        end
    end
end

puts "Enter a number:"
n = gets.chomp.to_i
print_prime(n)
