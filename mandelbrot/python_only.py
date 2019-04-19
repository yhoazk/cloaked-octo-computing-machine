
import sys
import datetime
# Area of space to investigate
x1, x2, y1, y2 = -2.13, 0.77, -1.3, 1.3

def calculate_z_serial_purepython(q, maxiter, z):
    """ pure python implementation """
    output = [0] * len(q)
    for i in range(len(q)):
      if i % 1000 == 0:
        # print progress
        print("{} complete".format(1.0/len(q) * i *100))
      for iteration in range(maxiter):
        z[i] = z[i] * z[i] + q[i]
        if abs(z[i]) > 2.0:
          output[i] = iteration
          break
    return output

def calc_pure_python(show_output):
  """ make a list of x and y values which will represent q
    xx and xx are the coordinates for the default configuration 

  """
  x_step = (float(x2 - x1) / float(w)) * 2
  y_step = (float(y1 - y2) / float(h)) * 2
  print("x step {} y step {}".format(x_step, y_step))
  x = []
  y = []
  q = []
  ycoord = y2
  while ycoord > y1:
    print("ycoord {} y1 {}".format(ycoord, y1))
    y.append(ycoord)
    ycoord += y_step
  xcoord = x1
  while xcoord < x2:
    x.append(xcoord)
    xcoord += x_step

  for ycoord in y:
    for xcoord in x:
      q.append(complex(xcoord, ycoord)) 
  
  z = [0+0j] * len(q)
  print("Total elements: {}".format(len(z)))

  start_time = datetime.datetime.now()
  output =  calculate_z_serial_purepython(q, maxiter, z)
  end_time = datetime.datetime.now()
  print("Main took {}s".format(end_time - start_time))
  validation_sum = sum(output)
  print("Total sum of elements (for validation):{}".format(validation_sum))

  if show_output:
    try:
      from PIL import Image
      import numpy as nm
      output = nm.array(output)
      output = (output + (265 * output) + (265* output)) * 8
      im = Image.new("RGB", (w//2, h//2))
      im.frombytes(output.tostring(), "raw", "RGBX", 0,-1)
      im.show()
    except ImportError as err:
      print("Could not import module")

if __name__ == "__main__":
    # get width height and max inter from cmd line
    w = int(sys.argv[1])
    h = w
    maxiter = int(sys.argv[2])
    calc_pure_python(True)


