import subprocess
import os
import pwd

commands = [
	'sudo apt install i3 -y',
	'sudo apt install pulseaudio-utils -y',
	'sudo apt install playerctl -y',
	'sudo apt install feh -y',
	'sudo apt install lxappearance',
	'wget -O ~/Pictures/wallpaper.jpg https://images.hdqwalls.com/wallpapers/yosemite-valley-4k-hd.jpg',
	'sudo apt install rofi -y',
	'sudo apt install compton -y',
	'sudo apt install i3blocks -y',
	'mkdir ~/.i3',
	'cp /etc/i3blocks.conf ~/.i3'
]

def run_commands(commands):

	print('Installing the required packages...')

	for command in commands:
		proc_run = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		print(proc_run.stdout.decode() + proc_run.stderr.decode())

	print('Packages installed successfully...')


def config_00(rf_path, wf_path):

	with open(rf_path, 'r') as read_file:
		f_contents = read_file.read()

	with open(wf_path, 'w') as write_file:
		write_file.write(f_contents)

comp_uname = pwd.getpwuid(os.getuid()).pw_name

run_commands(commands)

print('Reading custom config files and writing to official config files...\n')

config_00('config_files/i3blocks.conf', '/home/' + comp_uname + '/.i3/i3blocks.conf')
config_00('config_files/config', '/home/' + comp_uname + '/.config/i3/config')
