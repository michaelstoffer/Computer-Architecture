00000001              
00000001  # print_tim 
01000011  # print_num
01100011   # the number 99
10000100  # save
00101010 # the number 42
00000010
10000100  # save
00101010 # the number 42
00000011 # into R3
10000110 # registers[2] = registers[2] + registers[3] 
00000010  #R2
00000011  # R3
01000101 # print register
00000010  # R2
01000111  # PUSH     
00000010  # from R2
01001000  # POP              <-- PC
00000000  # into R0
01000101 # print register
00000000 # R0
00000010  # Halt

# TIM
# TIM
# 99
# 84
# 84