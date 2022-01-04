from cv2 import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
thumb = False
indexFinger = False
middleFinger = False
ringFinger = False
pinkyFinger = False
first = False

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)
while cap.isOpened():
  success, image = cap.read()
  if not success:
    break

  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
  image.flags.writeable = False
  results = hands.process(image)

  # Draw the hand annotations on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  
  while not first:
      s=["RockP.png","PaperP.png","ScissorsP.png"]
      for i in range(3):
        cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("output",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)        # Create window with freedom of dimensions
        im = cv2.imread(s[i])                        # Read image
        #imS = cv2.resize(im, (100, 100))                    # Resize image
        cv2.imshow("output", im)                            # Show image

        cv2.waitKey(1000)
      cv2.destroyAllWindows()
      first = True

  if results.multi_hand_landmarks:
    #print(mp_hands.HAND_CONNECTIONS)
    def X(num):
      for hand_landmarks in results.multi_hand_landmarks:
        s = str(hand_landmarks)
        arr = list(find_all(s, 'x'))
      return float(s[arr[num]+3:arr[num]+10])
    def Y(num):
      for hand_landmarks in results.multi_hand_landmarks:
        s = str(hand_landmarks)
        arr = list(find_all(s, ' y:'))
      return float(s[arr[num]+4:arr[num]+11])
    #s = str(hand_landmarks)
    centerPoint = X(2)
    if Y(4)<Y(17):
      thumb = True
    else:
      thumb = False
    centerPoint = Y(6)
    if Y(7)<centerPoint and Y(8)<centerPoint:
      indexFinger = True
    else:
      indexFinger = False
    centerPoint = Y(10)
    if Y(11)<centerPoint and Y(12)<centerPoint:
      middleFinger = True
    else:
      middleFinger = False
    centerPoint = Y(14)
    if Y(15)<centerPoint and Y(16)<centerPoint:
      ringFinger = True
    else:
      ringFinger = False
    centerPoint = Y(18)
    if Y(19)<centerPoint and Y(20)<centerPoint:
      pinkyFinger = True
    else:
      pinkyFinger = False
    if indexFinger and middleFinger and not ringFinger and not pinkyFinger:
      print("scissors")
      cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
      cv2.setWindowProperty("output",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)        # Create window with freedom of dimensions
      im = cv2.imread("Scissors.png")                        # Read image
      imS = cv2.resize(im, (100, 100))                    # Resize image
      cv2.imshow("output", imS)                            # Show image

      #cv2.waitKey(0)
      pass
    if indexFinger and middleFinger and ringFinger and pinkyFinger:
      print("paper")
      cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
      cv2.setWindowProperty("output",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)        # Create window with freedom of dimensions
      im = cv2.imread("Paper.png")                        # Read image
      imS = cv2.resize(im, (100, 100))                    # Resize image
      cv2.imshow("output", imS)                            # Show image

      #cv2.waitKey(0)
      pass
    if not indexFinger and not middleFinger:
      print("rock")
      cv2.namedWindow("output", cv2.WND_PROP_FULLSCREEN)
      cv2.setWindowProperty("output",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)        # Create window with freedom of dimensions
      im = cv2.imread("Rock.png")                        # Read image
      imS = cv2.resize(im, (100, 100))                    # Resize image
      cv2.imshow("output", imS)                            # Show image

      #cv2.waitKey(0)
      pass
    if not indexFinger and middleFinger and not ringFinger and not pinkyFinger:
      print("That is a big nono")
      #hands.close()
      #cap.release()
      pass
    #print(indexFinger,middleFinger,ringFinger,pinkyFinger,thumb)
    

    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

      
  cv2.imshow('Hello MIT', image)
  #print(str(indexFinger + middleFinger+ringFinger+pinkyFinger+thumb))
  if cv2.waitKey(5) & 0xFF == 27:
    break
hands.close()
cap.release()
