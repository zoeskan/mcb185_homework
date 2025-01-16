gunzip -c ../MCB185/data/dictionary.gz | grep -E "^[zonriac]*r[zonriac]*$" | grep -E "^.{4,}$"

