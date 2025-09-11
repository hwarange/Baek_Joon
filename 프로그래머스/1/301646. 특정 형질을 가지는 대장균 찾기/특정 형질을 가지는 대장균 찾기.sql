select count(*) as COUNT
from ECOLI_DATA 
where GENOTYPE % 4 <= 1 and (GENOTYPE % 2 = 1 or GENOTYPE % 8 >= 4)