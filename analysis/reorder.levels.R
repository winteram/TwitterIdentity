reorder.levels <- function(x, list) 
{
	list <- rev(list)
	for(factor in list)
	{
		x <- relevel(x, factor)
	}
	x
}