%generate triangle
clearvars
a =[];
i = 1;
divisors = 0;

while(divisors < 500)
    a = gen(i);
    divisors = check(a);
    i = i+1;
end

function tri = gen(n)
    tri = sum(1:n);
end

function total = check(n)
    total = 0;
    if ~(mod(sqrt(n),1))
        for i = 1:sqrt(n)-1
            if ~(mod(n,i))
                total = total+1;
            end
        end
        total = total*2+1;
    else
        for i = 1:floor(sqrt(n))
            if ~(mod(n,i))
                total = total+1;
            end
        end
        total = total*2;
    end
end