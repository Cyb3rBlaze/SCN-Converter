# Instructions for use

In order to effectively use this script, there are a couple steps you have to follow in order to download the right modules and tools for the API client script to work properly.

The PMA.start API is used for .scn file interpreting. It is connected to a conversion pipeline that is in the script that creates a .jpg image from the .scn file.

## Step 1: Install the PMA.start application to use the API

Go to [PMA's website](https://free.pathomation.com/download/) and install the corresponding application for your operating system. Continue with the installation process and make sure you place it somewhere on your disk where you can easily access it (applications for macOS for example because you can easily open it using launchpad).

## Step 2: Download the script

Clone this repository and move it to somewhere you can easily recall to make sure you remember where your files are located. Download the .zip file or open terminal, navigate to your desired localtion and type in the following command

```bash
git clone https://github.com/Cyb3rBlaze/ScnConverter.git
```

The previous script assumes you have git command line tools installed. If you don't, just download the .zip file, extract the contents, and move the folder to the desired location.

## Step 3: Install the dependencies

Go to your cloned folder and type in the following commands

```bash
#Creating a virtual enviornment
virtualenv env --python=python3

#Activating the enviornment
source env/bin/activate

#Installing dependencies
pip install -r requirements.txt
```

It may take a couple minutes to install the dependencis so be prepared to wait for a bit.

## Step 4: Configure your script

In order to properly configure your script, you must set the directory for all of your .scn files. You can do this very QUICKLY by opening up the PMA.start application you downloaded from step 1 and navigating to your directory.

(Most of the time, your directory will start with Root/Users/...)

Ex: If my folder that contains all my .scn files is in the Desktop directory of the "John" user, the directory would probably be

Root/Users/John/Desktop/data


Once you have set the directory, you must set the slide index. The slide index corresponds to the specific image that you want to convert into a .jpg. If you don't know what the index of your file is, run the script and type Ctl+c or Cmd+c based on how your keyboard is setup after you see a list of all the files in the directory. The first file in the list has an index of 0, the second has an index of 1, and so on.

Ex: If my file structure is setup as shown below

dir/
    slide1.scn
    slide2.scn
    slide3.scn

the first couple lines outputed by the script would be

[Root/Users/John/Desktop/dir/slide1.scn, Root/Users/John/Desktop/dir/slide2.scn, Root/Users/John/Desktop/dir/slide3.scn]


After you set the index of the image you want converted, set the scale to whatever number is desired. As you increase the scale, the resolution of the image is enhanced until it reaches the original resolution of the actual .scn image.

Note: As you increase the scale, the amount of time it takes increases exponentially so be aware that it will take a long time to produce very large images. You may want to start off with a scale of about 5 and increase from their based on your desired resolution.

## Step 5: Run your script

Once everything is configured, open your terminal again and navigate back to your cloned directory. If your virtual enviornment is not activated, activate it again.

Run the following command:

```bash
python main.py
```

If everything has been set up properly, you will see the image being created. Wait until the program stops running and you can view your converted high resolution file in your directory.

## IMPORTANT: Make sure you credit PMA for the use of their API

Sucaet Yves, Pappas Angelos and Wim Waelput. “Free Whole Slide Image Viewer – PMA.Start | Universal Digital Microscopy Software”. http://free.pathomation.com/ . 2017. Web. {DD-MMM-YYYY}.