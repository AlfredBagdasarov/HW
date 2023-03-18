packs_count = int(input('Кол-во пакетов: '))
bad_packs = 0
pack = []
decode = []

for i_pack in range(packs_count):
    print('\nПакет номер', i_pack + 1)
    for i_bit in range(4):
        bit = int(input(f'{i_bit + 1} бит: '))
        pack.append(bit)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете.')
        bad_packs += 1
    pack = []

print('Полученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', bad_packs)