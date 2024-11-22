
# Pip install helpers
echo "Apt installing Build Helpers ... "
sudo apt install build-essential libdbus-glib-1-dev libgirepository1.0-dev libpython3-dev libdbus-1-dev
echo "... Build Helpers Succeeded!"

# Audio Dependencies
echo "Apt installing Audio Dependencies ... "
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
echo "... Audio Dependencies Succeeded!"

# Create a venv with python3 if it doesn't exist 
if [ -d .venv ]; then
    echo ".venv detected, will not install another venv with python3"
else
    echo "Creating .venv with $(python3 -V)"
    python3 -m venv .venv    
fi

# Activate venv
echo "Activating venv"
source ./venv/bin/activate

# Installing Python Requirements
echo "Installing dependencies with $(which python)"
pip install -r requirements.txt

echo "Installation finished!"