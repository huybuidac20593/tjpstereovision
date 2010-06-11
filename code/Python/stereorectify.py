#!/usr/bin/python 
from stereoheader import *

def stereoRectify(calibdir="calib"):
  (CM1, CM2, D1, D2, R, T, E, F) = loadCalibration(calibdir)
  R1 = cv.CreateMat(3, 3, cv.CV_64F)
  R2 = cv.CreateMat(3, 3, cv.CV_64F)
  P1 = cv.CreateMat(3, 4, cv.CV_64F)
  P2 = cv.CreateMat(3, 4, cv.CV_64F)
  Q = cv.CreateMat(4, 4, cv.CV_64F)

  print "Running stereo rectification..."
  cv.StereoRectify(CM1, CM2, D1, D2, IMSIZE, R, T, R1, R2, P1, P2, Q)
  print "Done."
  return (R1, R2, P1, P2, Q)

def saveRectif(rect, dir="rect"):
  filenames = ("R1.txt", "R2.txt", "P1.txt", "P2.txt", "Q.txt")
  if not os.path.isdir(dir):
    print "Error: Dir {0} doesn't exist. Exiting.".format(dir)
    sys.exit(1)
  assert(len(filenames) == 5)
  (R1, R2, P1, P2, Q) = rect
  cv.Save("{0}/{1}".format(dir, filenames[0]), R1)
  cv.Save("{0}/{1}".format(dir, filenames[1]), R2)
  cv.Save("{0}/{1}".format(dir, filenames[2]), P1)
  cv.Save("{0}/{1}".format(dir, filenames[3]), P1)
  cv.Save("{0}/{1}".format(dir, filenames[4]), Q)
  print "Rectification parameters written to directory '{0}'.".format(dir)

def loadRectif(dir="rect"):
  filenames = ("R1.txt", "R2.txt", "P1.txt", "P2.txt", "Q.txt")
  for fn in ["{0}/{1}".format(dir, f) for f in filenames]:
    if not os.path.exists(fn):
      print "Error: File {0} doesn't exists. Exiting.".format(fn)
      sys.exit(1)
  R1 = cv.Load("{0}/{1}".format(dir, filenames[0]))
  R2 = cv.Load("{0}/{1}".format(dir, filenames[1]))
  P1 = cv.Load("{0}/{1}".format(dir, filenames[2]))
  P2 = cv.Load("{0}/{1}".format(dir, filenames[3]))
  Q = cv.Load("{0}/{1}".format(dir, filenames[4]))
  print "Rectification parameters loaded from dir '{0}'.".format(dir)
  return (R1, R2, P1, P2, Q)

if __name__ == "__main__":
  saveRectif(stereoRectify())
