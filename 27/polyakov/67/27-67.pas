###
//assign(input,'/tmp/27/67/27-67a.txt');

var (diffO,diffE,diffP) := |maxint|*3;
var sum := 0;
var a := new List<int>;
loop readInteger do begin
  a.Clear; var mo := maxint; 
  
  var minE := maxint; 
  var k := readInteger;
  loop k do begin
    var x := readinteger;
    sum += x;
    if x.IsOdd then begin
      remin(mo, x);
      a.Add(x); // нечетные
    end else if x.NotDivs(10) then remin(minE,x);
  end;
  var kE := k-a.Count; // кол-во четных
  if (k-a.Count>1) or (a.Count>=2) then remin(diffE,minE); // можно забрать четное
  
  if a.Count.IsOdd then begin 
    sum -= mo; // теперь сумма группы будет четная
    a.Remove(mo); // чтобы ниже не мешался,т.к. мы его уже не берем
    // меняем нечетное на нечетное, если придется
    foreach var e in a do 
      if (e-mo).NotDivs(10) then 
        remin(diffO,e-mo);
  end;
  
  // отбрасываем пару нечетных, если придется 
  if (a.count>2) or (kE>0) then 
    for var i := 0 to a.Count-2 do
      for var j := i+1 to a.Count-1 do
        if (a[i]+a[j]).ND(10) then 
          remin(diffP,a[i]+a[j]);
end;

println(sum,diffO,diffE,diffP); //см. что нашли
if sum.Divs(10) then sum -= min(diffO,diffE,diffP);

println(sum);
MillisecondsDelta.Print

//4  4 1 7 7 14  2 1 1  2 5 8  2 7 12