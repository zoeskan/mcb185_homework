live Assessment
================

   1 CC tax_group:diatoms
 178 CC tax_group:fungi
 286 CC tax_group:insects
 103 CC tax_group:nematodes
 805 CC tax_group:plants
  94 CC tax_group:urochordates
 879 CC tax_group:vertebrates

11663 +
14811 -

History:
  cd Code/MCB185/data
  zless jaspar2024_core.transfac.gz| grep "tax_group" | sort | uniq -c > exam.sh nano exam.sh
  zless A.thaliana.gff.gz | cut -f7 | sort | uniq -c >> exam.sh
