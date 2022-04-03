var N, i, a, b : integer;
begin
  Assign(input, '27-b.txt');
  Readln( N );
  var s := 0;
  var dMin := MaxInt;
  for i:=1 to N do begin
    Readln( a, b );
    s += Max(a,b);
    var d := Abs(a-b);
    if d mod 3 <> 0 then
      dMin := Min(d, dMin)
  end;
  if s mod 3 <> 0 then
       Writeln( s )
  else Writeln( s-dMin );
end.
