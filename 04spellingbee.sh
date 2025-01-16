gunzip -c ../MCB185/data/dictionary.gz | grep -E "^[zonicar]*r[zonicar]*$" | grep -E "^.{4,}$"

