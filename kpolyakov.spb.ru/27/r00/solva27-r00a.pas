###
// Автор: А. Богданов
var data := ReadLines('27-a.txt').Skip(1)  // выбросили N
  .Sel(s->s.ToIntegers).ToA;
var sMax := data.Sum(x->x.Max);
var rMin := data.Sel(x->abs(x[0]-x[1])).Wh(r->r.ND(3)).Min; 
//Println( sMax, rMin );    
Println( sMax.ND(3)? sMax: sMax-rMin );    
