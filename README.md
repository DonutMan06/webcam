# webcam

This is a very simple python script that run several filters over a webcam flow

It can be use in addition of any virtual cam driver (for instance in Linux, [v4l2loopback](https://github.com/v4l2loopback/v4l2loopback)) to be plugged into external software such as VLC or Zoom.

![Webcam image](https://github.com/DonutMan06/DonutMan06/blob/main/wc2.png)

More information about the program [on my blog](https://donutblog.fr/gnu-linux/webcam/) (in french)


## Dependencies

- OpenCV2
- pyvirtualcam
- numpy

## Usage

```bash
$ python webcam.py

```

The script uses the first webcam found on the system.

If you do not want to use virtual cam as an output, just change the `VIRTUAL_CAM` variable from `True` to `False`

Currently, four real-time filters have been implemented :
- one with coloured filters, as presented by [Giovanni Code](https://www.youtube.com/watch?v=3N7fRURLz4A) YouTube channel
- one with green circle of various radii (the radius is proportionnal at the luminosity)
- one with ASCII letters
- one, which I wanted to create for a long time, with a sort of time delay between the different lines of a given frame

## Virtual cam usage

The updated flow can be piped to a virtual cam using pyvirtualcam python package.

Currently, it was only tested under Linux with v4l2loopback apt package but I guess it should work the same way with any other solutions (such as [ObsProject](https://obsproject.com/) for MacOS and, yuk, Windows)

I experienced some issues installing v4l2loopback on my computed, more information on my blog about how I solved this. Hopefully, this issue should be corrected in the latest Linux ditribution release.


```bash
$ sudo apt-get install v4l2loopback-dkms
$ sudo modprobe v4l2loopback devices=1
$ python webcam.py

```


