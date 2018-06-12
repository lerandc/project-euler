clearvars

a = (1:999)';
b = ~(mod(a,3));
c = ~(mod(a,5));
d = ~~(b+c);
f = a.*d;
g = sum(f)