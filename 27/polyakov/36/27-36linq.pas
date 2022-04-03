// На основе решения А. Богданова
const B = 10;
const D = 0;
function Nod(a, b: integer):integer;
begin
  while a*b <> 0 do
    (a,b) := (b, a mod b);
  Result:= a + b;
end;
begin
  var data := Readlines('27-36b.txt').Select(s->s.ToIntegers).ToArray;
  var n := data[0].First;
  var triples := data.Skip(1).Take(n).Select(x->|Nod(x[0],x[1]), Nod(x[0],x[2]), Nod(x[1],x[2])|);  
  var sum := triples.Sum(x->x.Max);
  triples.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на B
               .Select(x->x.Max)    // из каждой группы выбрать максимальное
               .ToArray)
    .Where(x->x mod B = D)
    .Max
    .Print;      
end.


