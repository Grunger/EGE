##
Assign(input, '27-75b.txt');
var N := ReadINteger;
var K := 43;
var tailSum := |0| + |-1|*(K-1);
var tailLen := |0|*K;
var (maxSum, minLen) := (0, 10**10);
var totalSum := 0;
for var i:=0 to N-1 do begin
  var x := ReadInteger;
  totalSum += x;
  var r := totalSum mod K;
  if tailSum[r] <> -1 then begin
    var curSum := totalSum - tailSum[r];
    var curLen := i - tailLen[r] + 1;
    if (curSum > maxSum) or 
       ((curSum = maxSum) and (curLen < minLen)) then begin
      maxSum := curSum;
      minLen := curLen;
    end
  end else begin
    tailSum[r] := totalSum;
    tailLen[r] := i+1;
  end
end;
print( minLen );
