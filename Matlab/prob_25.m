clearvars
seq = [1e-200 1e-200]';

while(floor(log10(seq(end))) < 300)
    seq(end+1) = seq(end)+seq(end-1);
end

answer = length(seq)

seq2 = [seq(end-1) seq(end)].*1e-100.*1e-100.*1e-100.*1e-100.*1e-100;

while(floor(log10(seq2(end))) < 299)
    seq2(end+1) = seq2(end)+seq2(end-1);
end

