# Rock-Paper-Scissors
Play a game of Rock Paper Scissors with the computer using a camera!

##### The Introduction:

  I wanted to learn how to use machine learning but did not have any real application to use it in, so I decided to try to make a game out of it and to my delight it was really fun to make and share with my friends and family.

## The First Version:

  When I started reading about machine learning I understood the idea that I had to teach the computer using an already existing set of data. With the amount of given data being directly proportional to the accuracy of the program. So with that in mind I began by taking photos of myself doing rock paper and scissors then running it through the algorithm to generate a model that I can use. I was happy with the result. It wasn't perfectly accurate but for a first try it was good. I came back to it the next day with many ideas of ways I could use it but to my surprise it became less accurate, although I hadn’t changed anything yet, and then it hit me I only put images of myself with the same t-shirt in the same place. Realising this I knew I couldn’t just keep taking more pictures because there had to be a better way to do it.


##### First Version With Original Shirt:

https://user-images.githubusercontent.com/95291720/148114487-ce19c736-2c9b-44fe-9a6c-101a4361d171.mp4   

##### First Version With Diffrent Shirt:

https://user-images.githubusercontent.com/95291720/148114516-371efa9a-40fb-495a-bc12-b3c2043c49b4.mp4

The video that used a different shirt than the one used to train the model was less accurate than the one that used the original shirt, although the background was the same.


## The Improved version:

  ##### The Challenge:

   After researching for a while I found a hand tracking model online and decided to give it a try. My first challenge was to find a way to check what kind of gesture the user was doing using only the location of the points. 
   
   ###### Hand Landmarks:
   
   ![Hand Landmarks](https://user-images.githubusercontent.com/95291720/148080906-0c5803b5-2d22-4dd3-b445-b7bb69599dd7.PNG)

  ##### The Solution: 

  I decided that I would create 5 variables that would summaries the information I could get from all of the 21 landmarks. These variables were: thumb, indexFinger, middleFinger, ringFinger and pinkyFinger. If they were false it meant that the finger was closed and if it was true then the finger was open. I did this because to know if someone did rock, it's simple just see if all fingers are closed and if someone did scissors just see if they have their index finger and middle finger open and lastly if it is paper see if they have all fingers open.
  
  ```
  thumb = False
  indexFinger = False
  middleFinger = False
  ringFinger = False
  pinkyFinger = False
  ```
  
  ```
  if indexFinger and middleFinger and ringFinger and pinkyFinger:
      print("paper")
  ```
  
  ```
  if indexFinger and middleFinger and not ringFinger and not pinkyFinger:
      print("scissors")
  ```

  ##### The Implementation:

  To see if a finger was open or not I saved the y coordinate of the metacarpophalangeal joint[^1] and compared it to the current location of the proximal interphalangeal joint[^2] and the distal interphalangeal joint[^3] if both joints were below the metacarpophalangeal joint it meant that the finger was closed otherwise the finger is open.
  
  ###### Example for the Ring Finger:
  
  ```
  centerPoint = Y(14)
  if Y(15)<centerPoint and Y(16)<centerPoint:
      ringFinger = True
    else:
      ringFinger = False
  ```

  ##### The Game:

  The game starts by showing images of rock paper then scissors, after that it waits for the player to start moving and mimics his gesture so if he puts rock it shows an image of rock and if he does paper it shows an image of paper and so on.
  
  ##### Example:

https://user-images.githubusercontent.com/95291720/148115731-ceaeca91-4eee-448c-a334-6545e2367d02.mp4

## The Future version:


  ##### The Introduction:

  One of the things that excite me about attending MIT is that I get access to amazing resources like the ProtoWorkshop where I could try to build my wildest ideas. One of these ideas is to transform my rock paper scissors game from only working on a computer to a mechanical arm that can move on its own. Although its first application would be to play a game, the possibilities for reforming into a more useful tool is endless. An example of that could be to make home appliances react to hand gestures not voice commands since deaf people can’t use voice commands.

  ##### The Setup: 

  First, after printing the model and assembling it we can use multiple servos to control the finger movements. This allows us to have control over each finger individually instead of moving a set of fingers together. Next we connect the servos to a raspberry pi or an arduino so that we wouldn’t have to have the project directly connect to our computer when we are done. Finally, we connect the python script to the microcontroller and plug in the camera.






References: 

[^1]: Distal interphalangeal joint: the joint closest to the fingertip.

[^2]: Proximal interphalangeal joint: the joint in the middle of the finger.

[^3]: Metacarpophalangeal joint: the joint at the base of the finger.
