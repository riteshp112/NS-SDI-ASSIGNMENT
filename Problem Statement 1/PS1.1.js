function daybymon(month)
{if(month>12 || month<1)
 return "Invalid Month";
 helper=[31,28,31,30,31,30,31,31,30,31,30,31];
 return helper[month-1];
}
