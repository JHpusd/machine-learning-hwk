
function proj(A,x)
    return A * inv(transpose(A) * A) * transpose(A) * x
end

function mag(x)
    return sqrt(sum([i^2 for i in x]))
end

function dot(x,y)
    return sum([x[i]+y[i] for i in 1:length(x)])
end

function proj_ang(A,x)
    projection = proj(A,x)
    dot_p = dot(projection, x)
    mags = mag(projection) * mag(x)
    return acos(dot_p / mags)
end

function distance(x,y)
    return sqrt(sum([(x[i] - y[i])^2 for i in 1:length(x)]))
end

function proj_distance(A,x)
    projection = proj(A,x)
    return distance(projection, x)
end

A = [1 1; -1 1; -1 0]
x = [4; -6; -2]
print(proj(A,x))