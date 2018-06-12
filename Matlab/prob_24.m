clearvars

vec_orig = 0:9;
combos = zeros(factorial(10),10);
count = 1;
tic
for q = 1:10
    [val1,vec1] = create_set(vec_orig,q);
    for w = 1:9
        [val2,vec2] = create_set(vec1,w);
        for e = 1:8
            [val3,vec3] = create_set(vec2,e);
            for r = 1:7
                [val4,vec4] = create_set(vec3,r);
                for t = 1:6
                    [val5,vec5] = create_set(vec4,t);
                    for y = 1:5
                        [val6,vec6] = create_set(vec5,y);
                        for u = 1:4
                            [val7,vec7] = create_set(vec6,u);
                            for i = 1:3
                                [val8,vec8] = create_set(vec7,i);
                                for j = 1:2
                                    [val9,vec9] = create_set(vec8,j);
                                    combos(count,[1 2 3 4 5 6 7 8 9 10]) = [val1 val2 val3 val4 val5 val6 val7 val8 val9 vec9];
                                    count = count+1;
                                end
                            end
                        end
                    end
                end
            end
        end
    end
end
toc
answer2 = (combos(1e6,:));
%[test,next] = looper(vec1,1)
%
%2*factorial(9)+6*factorial(8)+6*factorial(7)+2*factorial(6)+5*factorial(5)+factorial(4)+2*factorial(3)+2*factorial(2)
%
coefficients = [2 6 6 2 5 1 2 2 1 0];
coef = coefficients + 1;
answer = zeros(1,10);
vec = 1:10;
for i = 1:10
   [answer(i), vec] = create_set(vec,coef(i));
end

answer = answer - 1;
function [value, vec] = create_set(vec,iter)
    value = vec(iter);
    vec(iter) = [];
end

function [val, next] = looper(set,iter)
    next = zeros(length(set),1);
    for i = iter:length(set)
        for j = 1:length(set)-1
            [val,new_set] = create_set(set,i);
            [out1 out2] = looper(new_set,j);
            next = [val out2];
        end
        if length(set) == 1
            val = set;
            next = [];
        end
    end
end