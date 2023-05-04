import cv2
import numpy as np

class hsv_values():
    def __init__(self):
        self.color_dict = {
            "1":{#blue
                "L_limit":[98,50,50],
                "U_limit":[139,255,255]
                
            },
            "2":{#red
                "L_limit":[0,100,200],
                "U_limit":[10,255,255]
                
            },
             "3":{#green
                "L_limit":[40,50,50],
                "U_limit":[75,255,255]
                
            },
              "4":{#orange
                "L_limit":[10,150,20],
                "U_limit":[25,255,255]
                
            },
              "5":{#black
                "L_limit":[0,0,0],
                "U_limit":[350,55,100]
                  
              },
              "6":{#pink
                "L_limit":[148,100,100],
                "U_limit":[158,255,255]
                  
              },
              "7":{#magenta
                  "L_limit":[165,150,100],
                  "U_limit":[180,255,255]
                  
              },
              "8":{#yellow
                  "L_limit":[22,50,20],
                  "U_limit":[32,255,255]
                  
              },
              "9":{#white
                "L_limit":[0,0,100],
                "U_limit":[180,25,255]
                  
              }
        }
        
    def main(self):
        clr = input("Which color do you want to detect?\n\n1:BLUE \n2:RED \n3:GREEN\n4:ORANGE \n5:BLACK \n6:PINK \n7:MAGENTA \n8:YELLOW \n9:WHITE \n\n")
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            b_mask = cv2.inRange(
                cv2.cvtColor(frame,cv2.COLOR_BGR2HSV),
                np.array(self.color_dict[clr]["L_limit"]),
                np.array(self.color_dict[clr]["U_limit"])
            )
            filter = cv2.bitwise_and(frame,frame,mask=b_mask)
            cv2.imshow("Original Feed", frame)
            cv2.imshow("Filtered Feed", filter)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        
        cap.release()
        cv2.destroyAllWindows()

hsv_values().main() 