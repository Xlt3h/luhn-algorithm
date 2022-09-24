# luhn-algorithm
Decoding the ID number
A South African ID number is a 13-digit number which is defined by the following format: YYMMDDSSSSCAZ.

The first six digits (YYMMDD) are based on your date of birth. For example, 23 January 1988 becomes 880123. Although rare, it can happen that someone’s birth date does not correspond with their ID number.
The next four digits (SSSS) are used to define your gender, with only the first digit of the sequence relevant. Females have a number of 0 to 4, while males are 5 to 9.
The next digit (C) is 0 if you are an SA citizen, or 1 if you are a permanent resident.
The next digit (A) was used until the late 1980s to indicate a person’s race. This has been eliminated and old ID numbers were reissued to remove this.
The last digit (Z) is a checksum digit, used to check that the number sequence is accurate using the Luhn algorithm.
