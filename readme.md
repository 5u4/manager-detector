# Manager Detector

## Description

Hide specific window when faces other than you are been detected. Inspired by [weibo post](http://fx.weico.cc/share/24272383.html?weibo_id=4242250063517925).

*Works only in mac.*

## How to use

```bash
$ python3 detect
```

**Note**: [opencv](https://pypi.org/project/opencv-python/), [face_recognition](https://github.com/ageitgey/face_recognition),
and a camera are required 😋.

### Options

 - work: the name of the working app (default: Mail)
 - distraction: the name of the leisure app (default: Google Chrome)
 - show: display video capture and face found (default: False)
 - rest: the time (s) between switching work and distraction (default: 0.5)

**Example**

Start a detection with PyCharm as work app and Google Chrome as leisure app. Also show the video capture.

```bash
$ python detect --work=PyCharm --distraction="Google Chrome" --show=true
```
