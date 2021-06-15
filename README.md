# ReadingFrame
# Language: Python
# Input: CSV
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes as input as CSV file with genes as rows,
assumed to have columns for start and end.

It then adds a column (readingFrame) to this CSV file, for each
gene the distance (in nucleotides) between its start and the end of the
previous gene

