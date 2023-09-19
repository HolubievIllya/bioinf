# Вправа 1. Знайдіть і виведіть на екран довжину ori холерного вібріона, яка наведена вище. 
# В Python є готова команда len(ori) для знаходження кількості символів у рядку. Але ви спробуйте самостійно написати таку функцію.

ori_vibrio_cholerae = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"

def ori_len(ori: str) -> int:
    len = 0
    for _ in ori:
        len += 1
    return len

# Вправа 2. Спробуємо створити функцію PatternCount(Pattern, Text), яка визначатиме кількість разів, 
# коли k-мер Pattern з'являється як підрядок тексту. За наведеним вище прикладом, результатом функції буде
# PatternCount ("ACTAT", "ACAACTATGCATACTATCGGGAACTATCCT") = 3.

pattern = "ACTAT"
text = "ACAACTATGCATACTATCGGGAACTATCCT"

def PatternCount(pattern: str, text: str) -> int:
    sum = 0
    for i in range(len(text[:-len(pattern)])):
        if text[i:i+len(pattern)] == pattern:
            sum += 1
    return sum