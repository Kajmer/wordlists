#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getPasswd(file):
    output = ''
    counter = 0
    for line in file:
        password = line[line.find(':') + 1::]
        output += password
        counter += 1
    print ("Stage strings: {}". format(counter))
    return output

#inputFile = open('tests.txt', 'r')
inputFile_gmail = open('gmail.txt', 'r')
inputFile_mail = open('mail.txt', 'r')
inputFile_yandex = open('yandex.txt', 'r')
outputFile = open('passwords_result.txt', 'w')

passwords = getPasswd(inputFile_gmail) #+ getPasswd(inputFile_mail) + getPasswd(inputFile_yandex)

inputFile_yandex.close()
inputFile_mail.close()
inputFile_gmail.close()
outputFile.close()