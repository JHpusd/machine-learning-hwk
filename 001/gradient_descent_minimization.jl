
function f(x,y)
    return 1 + 2*(x^2) + 3*(y^2)
end

global d = 0.1
global a = 0.001

function run(x,y)
    for i in 1:2
        f_x = (f(x+0.5*d, y) - f(x-0.5*d, y)) / d
        f_y = (f(x, y+0.5*d) - f(x, y-0.5*d)) / d
        x -= a*f_x
        y -= a*f_y
    end
    return (x,y)
end

start = time_ns()
for i in 1:10
    run(1,2)
end
stop = time_ns()

print("julia: ",(stop-start)/10^10)