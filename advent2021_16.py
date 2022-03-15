from math import exp


inp = "D2FE28"
inp = "38006F45291200"
inp = "EE00D40C823060"
inp = "8A004A801A8002F478"
inp = "620080001611562C8802118E34"
inp = "620D7B005DF2549DF6D51466E599E2BF1F60016A3F980293FFC16E802B325332544017CC951E3801A19A3C98A7FF5141004A48627F21A400C0C9344EBA4D9345D987A8393D43D000172329802F3F5DE753D56AB76009080350CE3B44810076274468946009E002AD2D9936CF8C4E2C472400732699E531EDDE0A4401F9CB9D7802F339DE253B00CCE77894EC084027D4EFFD006C00D50001098B708A340803118E0CC5C200A1E691E691E78EA719A642D400A913120098216D80292B08104DE598803A3B00465E7B8738812F3DC39C46965F82E60087802335CF4BFE219BA34CEC56C002EB9695BDAE573C1C87F2B49A3380273709D5327A1498C4F6968004EC3007E1844289240086C4D8D5174C01B8271CA2A880473F19F5024A5F1892EF4AA279007332980CA0090252919DEFA52978ED80804CA100622D463860200FC608FB0BC401888B09E2A1005B725FA25580213C392D69F9A1401891CD617EAF4A65F27BC5E6008580233405340D2BBD7B66A60094A2FE004D93F99B0CF5A52FF3994630086609A75B271DA457080307B005A68A6665F3F92E7A17010011966A350C92AA1CBD52A4E996293BEF5CBFC3480085994095007009A6A76DF136194E27CE34980212B0E6B3940B004C0010A8631E20D0803F0F21AC2020085B401694DA4491840D201237C0130004222BC3F8C2200DC7686B14A67432E0063801AC05C3080146005101362E0071010EC403E19801000340A801A002A118012C0200B006AC4015088018000B398019399C2FC432013E3003551006E304108AA000844718B51165F35FA89802F22D3801374CE3C3B2B8B5B7DDC11CC011C0090A6E92BF5226E92BF5327F3FD48750036898CC7DD9A14238DD373C6E70FBCA0096536673DC9C7770D98EE19A67308154B7BB799FC8CE61EE017CFDE2933FBE954C69864D1E5A1BCEC38C0179E5E98280"
# inp = "00569F4A0488043262D30B333FCE6938EC5E5228F2C78A017CD78C269921249F2C69256C559CC01083BA00A4C5730FF12A56B1C49A480283C0055A532CF2996197653005FC01093BC4CE6F5AE49E27A7532200AB25A653800A8CAE5DE572EC40080CD26CA01CAD578803CBB004E67C573F000958CAF5FC6D59BC8803D1967E0953C68401034A24CB3ACD934E311004C5A00A4AB9CAE99E52648401F5CC4E91B6C76801F59DA63C1F3B4C78298014F91BCA1BAA9CBA99006093BFF916802923D8CC7A7A09CA010CD62DF8C2439332A58BA1E495A5B8FA846C00814A511A0B9004C52F9EF41EC0128BF306E4021FD005CD23E8D7F393F48FA35FCE4F53191920096674F66D1215C98C49850803A600D4468790748010F8430A60E1002150B20C4273005F8012D95EC09E2A4E4AF7041004A7F2FB3FCDFA93E4578C0099C52201166C01600042E1444F8FA00087C178AF15E179802F377EC695C6B7213F005267E3D33F189ABD2B46B30042655F0035300042A0F47B87A200EC1E84306C801819B45917F9B29700AA66BDC7656A0C49DB7CAEF726C9CEC71EC5F8BB2F2F37C9C743A600A442B004A7D2279125B73127009218C97A73C4D1E6EF64A9EFDE5AF4241F3FA94278E0D9005A32D9C0DD002AB2B7C69B23CCF5B6C280094CE12CDD4D0803CF9F96D1F4012929DA895290FF6F5E2A9009F33D796063803551006E3941A8340008743B8D90ACC015C00DDC0010B873052320002130563A4359CF968000B10258024C8DF2783F9AD6356FB6280312EBB394AC6FE9014AF2F8C381008CB600880021B0AA28463100762FC1983122D2A005CBD11A4F7B9DADFD110805B2E012B1F4249129DA184768912D90B2013A4001098391661E8803D05612C731007216C768566007280126005101656E0062013D64049F10111E6006100E90E004100C1620048009900020E0006DA0015C000418000AF80015B3D938"
# inp = "C200B40A82"
# inp = "880086C3E88112"
# inp = "9C0141080250320F1802104A08"
# inp = "04005AC33890"
# inp = "880086C3E88112"
# inp = "CE00C43D881120"
# inp = "D8005AC2A8F0"
# inp = "F600BC2D8F"
# inp = "9C005AC2F8F0"
# inp = "9C0141080250320F1802104A08"

def to_bin(hex_string):
    int_val = int(hex_string, 16)
    bin_val = bin(int_val)
    return bin_val[2:]

def read_version(bits):
    # print("READ_VERSION", bits)
    v = bits[:3]
    # print("READ VERSION bits", v)
    return (int(v, 2), bits[3:])

def read_packet_type(bits):
    p_type = bits[:3]
    return (int(p_type, 2), bits[3:])

def read_groups(bits, consumed):
    is_last = bits[0]
    # print('bits', bits)
    val = bits[1:5]
    # print('val to', val)
    c = consumed + 5
    if is_last == '0':
        # print('koncze')
        return val, c
    temp_val, temp_consumed = read_groups(bits[5:], c)
    return val + temp_val, temp_consumed

def pad_zeros(bits):
    l = len(bits)
    bit_len = 8
    missing_zeros = (bit_len - (l % bit_len)) % 8
    return '0' * missing_zeros + bits

def read_literal_groups(bits):
    # print("PARSUJE_LITERAL")
    bit_val, consumed = read_groups(bits, 0)
    int_val = int(bit_val, 2)
    # print("LITERAL VAL", int_val)
    return int_val, bits[consumed:]

def parse_operator(bits):
    # print("PARSUJE OPERATOR")
    # print(bits)
    len_len = 15 if bits[0]=='0' else 11
    # print("LEN_LEN", len_len)
    rest = bits[1:]
    # print("REST", rest)
    len_val = int(rest[:len_len], 2)
    rest = rest[len_len:]
    # print("LEN", len_val)
    # print("REST", rest)
    if len_len == 15:
        packets_to_parse = rest[:len_val]
        rest = rest[len_val:]
        packets = parse_until_bit_len(packets_to_parse)
        return packets, rest
    elif len_len == 11:
        # print("PAKIETOW JEST", len_val)
        packets, rest = parse_until_packet_len(rest, [], len_val)
        return packets, rest

def parse_until_bit_len(bits):
    # print("PARSUJE POKI EMPTY", bits)
    if not bits:
        return []
    version_parsed, not_parsed = parse_bits(bits)
    return [version_parsed] + parse_until_bit_len(not_parsed)

def parse_until_packet_len(bits, packets, i):
    # print("PARSUJE POKI PACKETS, DOTYCHCZASOWY WYNIK", bits, packets)
    if i == 0:
        return packets, bits
    version_parsed, not_parsed = parse_bits(bits)
    return parse_until_packet_len(not_parsed, packets + [version_parsed], i-1)

def parse_bits(bits):
    global version_count
    v, rest = read_version(bits)
    version_count += v
    # print("VER", v)
    # print(v, rest)
    ptype, rest = read_packet_type(rest)
    # print("PACKET TYPE", ptype)
    if ptype == 4:
        group_val, rest = read_literal_groups(rest)
        # print('val', group_val)
        return group_val, rest
    
    r, rest = parse_operator(rest)

    if ptype == 0:
        # expression.append('sum')
        return sum(r), rest
    elif ptype == 1:
        # expression.append('prod')
        return math.prod(r), rest
    elif ptype == 2:
        # expression.append('min')
        return min(r), rest
    elif ptype == 3:
        # expression.append('max')
        return max(r), rest
    elif ptype == 5:
        # expression.append('gt')
        return (1, rest) if r[0] > r[1] else (0, rest)
    elif ptype == 6:
        # expression.append('lt')
        return (1, rest) if r[0] < r[1] else (0, rest)
    elif ptype == 7:
        # expression.append('eq')
        return (1, rest) if r[0] == r[1] else (0, rest)
    # return r, rest
    # print(group_val)

# def sum_version_count(bits):
#     b = to_bin(bits)
#     b = pad_zeros(b)
#     v, rest = read_version(b)
#     ptype, rest = read_packet_type(rest)
#     if ptype == 4:
#         _group_val, rest = read_literal_groups(rest)
#         return v
#     r, rest = parse_operator(rest)
#     return r
#     # return v

version_count = 0

def solve_both(bits):
    global version_count
    b = to_bin(bits)
    # print("BIN", b, len(b))
    b = pad_zeros(b)
    # print("PADDED", b, len(b))
    r = parse_bits(b)
    print(version_count)
    return r

import math

r, rest = solve_both(inp)
print(r)
# print(sum_version_count(inp))
