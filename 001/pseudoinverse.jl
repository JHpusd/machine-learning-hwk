function run()
    y = [0; 1; 4; 9]
    data = [0 1; 1 1; 2 1; 3 1]
    trans = transpose(data)
    square = trans * data
    inverse = inv(square)
    answer = inverse * trans * y
end

start = time_ns()
for i in 1:10
    run()
end
stop = time_ns()
print("Julia: ", (stop-start)/(10^10))

