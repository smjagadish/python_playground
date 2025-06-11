import struct,array
def performOps():
    '''
             this function is a super simple demo for the memoryview operation in python
             we will have samples to have a byte array of string , integers (8-bit)
             and a byte array object (for 32-bit integers)
             memoryview operation will be done on each of these entities to do basic seek and/or manipulation
    :return:
    nothing
    '''

    #byte array of string
    b_str = bytearray(b'Hello World')
    mem_view_b_str = memoryview(b_str)
    str_slice = mem_view_b_str[:]
    print(f'seek of a bytes object holding a string ref\'d from memory view:{bytes(str_slice)}')
    # str_slice ref now points to a new object that is reverse of the mem_view (mapped to b_str)
    str_slice = str_slice[::-1]
    print(f'manipulation of the bytes object holding a string ref\'d from memory view. string is reversed: {bytes(str_slice)}')
    print(f'unmodified memory view rep: {bytes(mem_view_b_str)}')
    # memoryview manipulation
    mem_view_b_str[0] = 105
    print(f'memory view manipulated: {bytes(mem_view_b_str)}')
    print(f'modified original string: {bytes(b_str)}')

    #byte array of integers
    int_arr = array.array('i',[1,2,3,4])
    print(f'the unmodified array:{int_arr.tolist()}')
    mem_view_int_arr = memoryview(int_arr)
    mem_view_int_arr[0] = 115857
    print(f'the modified memory view rep:{bytes(mem_view_int_arr)}')
    print(f'the modified original array: {int_arr.tolist()}')

    #bytearray object of 8-bit int
    val = 8
    bval = bytearray([val])
    mem_view_b_val = memoryview(bval)
    print(f'original 8-bit int value:{bval}')
    mem_view_b_val[0] = 5
    print(f'memory view modified 8-bit int value:{bval}')

    #bytes object of 32-bit int
    byte_struct_int32 = bytearray(struct.pack('i',3000))
    mem_view_bs_int32 = memoryview(byte_struct_int32)
    print(f'original value of the 32-bit int:{byte_struct_int32}')
    mem_view_bs_int32.cast('i')[0] = 2500 #access underlying bytearray content as unsigned int 32-bit
    #mem_view_bs_int32[0] = 2500
    elem = struct.unpack('i',mem_view_bs_int32.tobytes())[0] #result is a tuple. so i get the first element since that is the only value
    print(f'memoryview modified val:{elem}')

    bb = 345678
   # len = (bb.bit_length()+7)//8
    blb = bb.to_bytes(4,"little")
    blb_arr = bytearray(blb)
    mm = memoryview(blb_arr)
    mm.cast('i')[0] = 245678
    print(f'the raw value:{blb_arr}')



if __name__ == '__main__':
    performOps()