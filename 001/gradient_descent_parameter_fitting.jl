
function rss(b0,b1)
    return (b0)^2 + (b0+b1-1)^2 + (b0+2*b1-4)^2
end

function run(b0,b1)
    for i in 1:2
        rss_b0 = (rss(b0+0.05,b1)-rss(b0-0.05,b1)) / 0.1
        rss_b1 = (rss(b0,b1+0.05)-rss(b0,b1-0.05)) / 0.1
        b0 -= 0.001*rss_b0
        b1 -= 0.001*rss_b1
    end
    return (b0,b1)
end

start = time_ns()
for i in 1:10
    run(0,2)
end
stop = time_ns()

print("julia: ", (stop-start)/10^10)
