// На основе решения А. Богданова
const B = 11;
const D = 0;
begin
  var data := Readlines('27-32b.txt').Select(s->s.ToIntegers).ToArray;
  var n := data[0].First;
  var triples := data.Skip(1).Take(n); 
  var sum := triples.Sum(x->x.Min);
  triples.Aggregate( |0|, 
      (a,x)-> a.Cartesian(x, (a,b)->a+b) // построить все комбинации сумм
               .GroupBy(x->x mod B) // сгруппировать по остаткам от деления на B
               .Select(x->x.Min)    // из каждой группы выбрать минимальное
               .ToArray)
    .Where(x->x mod B = D)
    .Min
    .Print;      
end.


