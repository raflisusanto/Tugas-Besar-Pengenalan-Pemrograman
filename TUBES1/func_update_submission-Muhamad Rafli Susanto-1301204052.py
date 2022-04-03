def update_submission(dict_submission, list_topic, dict_activity, nim):
    '''
    Fungsi menampilkan semua topik, meminta user memilih topik.
    Lalu menampilkan detil activity bertipe assignment di topik tersebut yang telah dijawab oleh mahasiswa nim, meminta user memilih assignment.
    Tampilkan jawaban eksisting, lalu minta jawaban baru. Jika tidak jadi update cukup dikosongkan maka tidak dilakukan perubahan jawaban.
    '''
    print('----Fungsi "update_submission" dijalankan----')
    count = 0  # untuk ngeluarin angka sebelum title
    for i in range(len(list_topic)):
        count += 1
        print(str(count) + ': ' + list_topic[i]['Title'])

    cek_digit = True
    while cek_digit:
        x = input("Masukkan nomor topic: ")  # handle error inputan
        if x.isdigit() and int(x) - 1 >= 0 and int(x) <= len(list_topic):  # cek kalo digit dan gak out of range
            x = int(x)
            print()
            print("Berikut adalah list assignment:")
            print(" {:3} | {:30} | {:10} | {:25} ".format("ID", "Title", "Type", "Description"))
            print("-" * 80)
            cek_digit = False
            for j in list_topic[x - 1]['Activities']:  # nge akses yang di dalam activities sesuai topik
                if dict_activity[j]['Type'] == 'assignment':
                    if str(nim) in dict_submission[j]:
                        print(" {:3} | {:30} | {:10} | {:25} ".format(j, dict_activity[j]['Title'],
                                                                      dict_activity[j]['Type'],
                                                                      dict_activity[j]['Description']))
                        cek_digit = True
                        while cek_digit:
                            print()
                            y = input("Masukkan ID assignment: ")  # handle error inputan
                            if y.isdigit() and int(y) in dict_submission and int(y) in list_topic[x - 1]['Activities']:
                                # cek kalo digit, ada di submission, dan ada di activities sesuai topik
                                y = int(y)
                                print()
                                print("Jawaban sebelumnya:")
                                print(dict_submission[y][str(nim)])  # print jawaban sebelumnya
                                print()
                                cek_digit = False
                                z = input("Masukkan jawaban baru atau kosongkan jika batal update: ")
                                if z != "":
                                    dict_submission[y][str(nim)] = str(z)  # update submission jika tidak batal
                                    # print(dict_submission[y][str(nim)]) *test
                            else:
                                print("Input tidak valid")
                                print()
                    else:
                        print("Belum ada jawaban yang disubmit")

        else:
            print("Input tidak valid")
            print()

    print()
    print()
    input("Tekan Enter untuk kembali ke menu utama...")


if __name__ == "__main__":
    LAST_ID_ACTIVITY = 2
    NIM_LOGIN = ''
    ADMIN_LOGIN = False

    # key pada dict_mhs['data'] adalah NIM
    dict_mhs = {'field': [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                          ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                          ('Password', '^[a-zA-Z0-9]{8,12}$')],
                'data': {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                         '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                         '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                         }
                }

    # Value pada key 'Activities' berupa list berisi id_activity
    list_topic = [{'Title': 'Dummy Topic 1', 'Description': 'Ini deskripsi topic 1', 'Activities': [0, 1]},
                  {'Title': 'Dummy Topic 2', 'Description': 'Ini deskripsi topic 2', 'Activities': [2]}
                  ]

    # key pada dict_activity adalah id_activity
    dict_activity = {0: {'Title': 'Dummy Assignment 1', 'Type': 'assignment', 'Description': 'buatlah program Game'},
                     1: {'Title': 'Dummy material', 'Type': 'material', 'Description': 'slide minggu ini'},
                     2: {'Title': 'Dummy Assignment 2', 'Type': 'assignment', 'Description': 'buatlah program LMS'}
                     }

    # key pada dict_submission adalah id_activity
    dict_submission = {0: {'113': 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'},
                       2: {'113': 'Ini jawaban mahasiswa 113',
                           '114': 'Ini jawaban mahasiswa 114'}
                       }

    # key pada dict_grade adalah id_activity
    dict_grade = {0: {'113': 100}

                  }
    print("Dictionary sebelum fungsi dijalankan: ")
    print(dict_submission)
    print()
    update_submission(dict_submission, list_topic, dict_activity, 113)
    print()
    print("Dictionary setelah fungsi dijalankan: ")
    print(dict_submission)
