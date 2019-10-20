import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32matau silahkan chat Whatshap athoor ")
7
print ("\033[1;32mwa081390962290 ")

username = 'SAY'      

password = 'KOJI'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mAlhmdllh sudah masuk juga..", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
