
function test(A)
    return A * inv(transpose(A) * A) * transpose(A)
end

A = [1 1; 1 2; 2 -1]
print(7 * test(A))