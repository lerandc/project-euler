clearvars
natural = 1:100;


sum_square = sum(natural.^2);
square_sum = (sum(natural))^2;

answer = abs(sum_square - square_sum)