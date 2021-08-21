function n_sum(n)
    total = 0
    for i in 1:n
        total = total + i
    end
    return total
end

start = time_ns()
for i in 1:10
    n_sum(1000000)
end
stop = time_ns()
print((stop-start)/10000000000)