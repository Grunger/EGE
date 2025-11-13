begin
  Assign(input,'27-b.txt');
  var (s, d) := (0, MaxInt);
  var n := ReadInteger;
  loop n do begin
    var (a,b) := ReadInteger2;
    s += Max(a,b);
    var diff := Abs(a-b);
    if diff mod 3 <> 0 then
      d := Min(d, diff)
    end;
  if s mod 3 <> 0 then
       Print(s)
  else Print(s-d);
end.
