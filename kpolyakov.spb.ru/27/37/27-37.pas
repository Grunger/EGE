## assign(input, '27-37b.txt');
var n := ReadInteger;
var k := |0| * 10001;
var count := 0;
loop n do begin
  var x := ReadInteger;
  var i := 1;
  while i < x-i do begin
    count += k[i]*k[x - i];
    i += 1;
  end;
  if i = x-i then
    count += k[i]*(k[i] - 1) div 2;
  k[x] += 1;
end;
print( count );

{
// Перебор: не сработает для варианта В
## assign(input, '27-37a.txt');
var n := ReadInteger;
var a := ReadArrInteger(n);
var count := 0;
for var i := 0 to n-3 do
  for var j := i+1 to n-2 do
    for var k := j+1 to n-1 do 
      if a[i]+a[j]=a[k] then 
        count += 1;
print( count );
}
