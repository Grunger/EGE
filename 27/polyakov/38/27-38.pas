## // Keys 43 61 254363 
assign(input, '27-38a.txt'); 
var (a, s):=(|0|*10, 0); 
loop ReadInteger do a[ReadInteger] +=1; 
for var j:=1 to 9 do s += a[j] div 2 * 2 * j; 
Print(s + a.Indices(x-> x.IsOdd).Last);

