echo "Downloading eclipse-get..."
mkdir eclipse-get
wget -qO- https://github.com/adambrenecki/eclipse-get/tarball/master | tar zx -C eclipse-get/ --strip-components 1
cd eclipse-get
echo "Installing eclipse-get. You'll probably be asked for your root password."
sudo make install
cd ..
rm -r eclipse-get
