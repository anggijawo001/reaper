##  Copy the linux command from http://remotedesktop.google.com/headless  ##
CRP1 = 'DISPLAY= /opt/google/chrome-remote-desktop/start-host --code="4/0AX4XfWgWl4j8KnvSSnOMc55CQQrdV6ER_UhBr2hY9r3U-NKnnwZkFOjcnqJ7aR15q8wywg" --redirect-url="https://remotedesktop.google.com/_/oauthredirect" --name=$(hostname)'
Pin = 123456 ## rdp pin
Name = "RDP"    ## rdp name
import os,subprocess
username = "user" 
password = "root"
print("Creating User and Setting it up")
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
print("User Created and Configured")
CRP = CRP1.replace("$(hostname)",Name)
class CRD:
    def __init__(self):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        self.installingEdge()
        self.installingBrave()
        self.installingOBS()
        self.finish()
    @staticmethod
    def installCRD():
        print("Installing Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")

    @staticmethod
    def installGoogleChorme():
        print("Installing Google Chrome")
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
    
    @staticmethod
    def installingEdge():
        print("Installing edge Browser")
        subprocess.run(["wget", "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-dev/microsoft-edge-dev_93.0.926.1-1_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "microsoft-edge-dev_93.0.926.1-1_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
    
    @staticmethod
    def installingBrave():
        print("Installing Brave Browser")
        subprocess.run(["wget", "https://github.com/brave/brave-browser/releases/download/v1.28.31/brave-browser-nightly_1.28.31_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "brave-browser-nightly_1.28.31_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
        
    
    @staticmethod
    def installingOBS():
        print("Installing OBS-STUDIO")
        package = "obs-studio"
        ! apt --fix-broken install > /dev/null 2>&1
        ! killall apt > /dev/null 2>&1
        ! rm /var/lib/dpkg/lock-frontend
        ! dpkg --configure -a > /dev/null 2>&1
        ! apt-get  install -o Dpkg::Options::="--force-confold" --no-install-recommends -y $package
        ! dpkg --configure -a > /dev/null 2>&1
        ! apt  update > /dev/null 2>&1
        ! apt install $package > /dev/null 2>&1

    @staticmethod
    def finish():
        print("Finalizing")
        os.system(f"adduser {username} chrome-remote-desktop")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {username} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        print("Finished Succesfully")

try:
    if username:
        if CRP == "":
            print("Please enter authcode from the given link")
        elif len(str(Pin)) < 6:
            print("Enter a pin more or equal to 6 digits")
        else:
            CRD()
except NameError as e:
    print("username variable not found")
    print("Create a User First")





///////////////////////////////


package = "openvpn" ## Enter package name
! apt --fix-broken install > /dev/null 2>&1
! killall apt > /dev/null 2>&1
! rm /var/lib/dpkg/lock-frontend
! dpkg --configure -a > /dev/null 2>&1
! apt-get  install -o Dpkg::Options::="--force-confold" --no-install-recommends -y $package
! dpkg --configure -a > /dev/null 2>&1
! apt  update > /dev/null 2>&1
! apt install $package > /dev/null 2>&1




///////////////////////////////////
! wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
! sudo apt-get install ./nordvpn-release_1.0.0_all.deb

! sudo apt-get update
! sudo apt-get install nordvpn

//////////////////////////////////////

! cd /etc/openvpn/
! sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
! sudo unzip ovpn.zip
! sudo rm ovpn.zip
! cd /etc/openvpn/ovpn_tcp/
! ls -al

! sudo mv /notebooks/ovpn_tcp /etc/openvpn/
! sudo mv /notebooks/ovpn_udp /etc/openvpn/


! sudo printf 'adrianf41@gmail.com\nKanrad@10006' > /etc/openvpn/pass.txt


! sudo openvpn /etc/openvpn/ovpn_tcp/us9095.nordvpn.com.tcp.ovpn --auth-user-pass <(echo -e "adrianf41@gmail.com\Kanrad@10006")

! sudo openvpn /etc/openvpn/ovpn_tcp/us9095.nordvpn.com.tcp.ovpn --auth-user-pass /etc/openvpn/pass.txt

#rtry to create the text file pass.txt in openvpn folder


#move config file
! mv /etc/sysctl.conf /notebooks/sysctl.conf

#disable ipv6; add to the bottom of file
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv6.conf.tun0.disable_ipv6 = 1

#move file back
! mv /notebooks/sysctl.conf /etc/sysctl.conf


cd /etc/openvpn/
sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
sudo unzip ovpn.zip
sudo rm ovpn.zip
cd /etc/openvpn/ovpn_tcp/
ls -al





sudo apt install nvidia-cuda-toolkit

wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.29_Lin64.tar.gz
tar -xf lolMiner_v1.29_Lin64.tar.gz
cd 1.29
./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker4#5xer-nxch --ethstratum ETHPROXY

//144.202.18.5

wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.29_Lin64.tar.gz
tar -xf lolMiner_v1.29_Lin64.tar.gz
cd 1.29
./lolMiner --algo ETHASH --pool 144.202.18.5:5000 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker4#5xer-nxch --ethstratum ETHPROXY


//SSL

wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.29_Lin64.tar.gz
tar -xf lolMiner_v1.29_Lin64.tar.gz
cd 1.29
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker4#5xer-nxch --ethstratum ETHPROXY --tls on


wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.31_Lin64.tar.gz
tar -xf lolMiner_v1.29_Lin64.tar.gz
cd 1.29
./1.29/lolMiner --algo ETHASH --pool 144.202.18.5:5001 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker3 --tls on

./lolMiner --algo ETHASH --pool 144.202.18.5:5000 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker7#5xer-nxch --tls on


wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz
tar -xf lolMiner_v1.31_Lin64.tar.gz
cd 1.31
./lolMiner --algo ETHASH --pool 144.202.18.5:5001 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker3 --tls on

//us-eth.2miners.com:12020

wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz
tar -xf lolMiner_v1.31_Lin64.tar.gz
cd 1.31
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker6 --tls on

gsettings set org.gnome.desktop.session idle-delay 0
gsettings set org.gnome.settings-daemon.plugins.power idle-dim false
sudo systemctl mask sleep.target suspend hibernate.target hybrid-sleep.target



wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz
tar -xf lolMiner_v1.31_Lin64.tar.gz
cd 1.31
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker_$( date +%Y%m%d%H%M%S ) --tls on --ethstratum ETHPROXY

//Pipe to bash
wget -O - https://raw.githubusercontent.com/blitz2099/reaper/main/init.sh | bash

tail -f 1.31/nohup.out

if pgrep -x "lolMiner" > /dev/null
then
    wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz
    tar -xf lolMiner_v1.31_Lin64.tar.gz
    cd 1.31
    nohup ./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker_$( date +%Y%m%d%H%M%S ) --tls on --ethstratum ETHPROXY > nohup.out &
fi

if pgrep -x "lolMiner" > /dev/null
then
    echo "Running"
fi

if pgrep -x "lolMiner" > /dev/null
then
    echo "Already Running"
else
    wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz
    tar -xf lolMiner_v1.31_Lin64.tar.gz
    cd 1.31
    nohup ./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker_$( date +%Y%m%d%H%M%S ) --tls on --ethstratum ETHPROXY > nohup.out &
fi




./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker1 --tls on --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker2 --tls on --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker3 --tls on --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker4 --tls on --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker5 --tls on --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool us-eth.2miners.com:12020 --user 0x476241f016e207C4faf657687FcF553f51047030.Worker6 --tls on --ethstratum ETHPROXY



./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker1#5xer-nxch --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker2#5xer-nxch --ethstratum ETHPROXY
./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user ETH:0x476241f016e207C4faf657687FcF553f51047030.Worker3#5xer-nxch --ethstratum ETHPROXY




function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton,60000);

// Grab the run button
document.querySelectorAll(".cell-execution-container > colab-run-button")[3].shadowRoot.querySelector(".cell-execution-indicator")

// Show if the cell is currently running
document.querySelectorAll(".cell-execution-container > colab-run-button")[3].shadowRoot.querySelector(".cell-execution.running")

sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target



