import RPi.GPIO as G
import smbus2
import time
from RPLCD.i2c import CharLCD
import sys
sys.modules [ ' smbus'] = smbus2
lcd = CharLCD( 'PCF8574' ,address = 0x27, port = 1,backlight_enabled = True)
G.setmode(G.BOARD)


MATRIX = [ [1, 2, 3, 'A'],[4, 5, 6, 'B'],[7, 8, 9,'C'],['*',0,'#', 'D'] ]
ROW_PIN = [7, 11, 13, 15]
COL_PIN = [12, 16, 18, 36]
Cur_File = 'None'
Cur_i = 0
Cur_j = 0

'''def LCD_show(input_string1, input_string2) :
    lcd.clear()
    if (len(input_string1) <= 16):
        lcd.cursor_pos = (0,0)
        lcd.write_string(input_string1)
    else:
        starter_1 = 0
        while True:
            lcd.cursor_pos = (0,0)
            str_ = input_string1[starter_1:starter_1+16]
            lcd.write_string(str_)
            time.sleep(0.3)
            starter_1 += 1
            starter_1 = starter%16 '''

def LCD_show(input_string1, input_string2) :
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string(input_string1)
    lcd.cursor_pos = (1,0)
    lcd.write_string(input_string2)

def Kb_Reset():
    Cur_i = 0
    Cur_j = 0


def Kb_Detect() :
    for j in range(4):
        G.output(COL_PIN[j], 0)
        for i in range(4):            
            if G.input(ROW_PIN[i]) == 0:
                Cur_i = i
                Cur_j = j
                print(str(i) + ',' + str(j))
                time.sleep(0.5)
                return True
    return False         
                

for j in range (4):
    G.setup(COL_PIN[j], G.OUT)
    G.output(COL_PIN[j], 1)
for i in range(4):
    G.setup(ROW_PIN[i], G.IN, pull_up_down = G.PUD_UP)

try:
    RECORD = 0
    LCD_show( 'Select mode.','A:Food B:Clothe C:Living D:Vehicle')
    while(True):
        if( Kb_Detect() ):
            if( Cur_j == 3 ):
                if ( Cur_i == 0 ):
                    Cur_File = "Food_Cost"
                    LCD_show('A mode selected' , 'Next please enter your cost on food.')
                    Kb_Reset()
                    while(True):
                        if( Kb_Detect() ):
                            if (Cur_i < 3 and Cur_j < 3) or (Cur_i == 3 and Cur_j == 1):
                                RECORD = RECORD*10 + MATRIX[i][j]
                                LCD_show( 'Enter your cost: ' ,str(RECORD))
                                G.output(COL_PIN[j], 1)                                    
                            elif ( i == 3 and j == 2 ) :                                        
                                file = open( Cur_File +'.txt', 'a')
                                file.write(str(RECORD)+'In')
                                file.close()
                                LCD_show(' Cost saved. ' , 'Congratulations! ')
                                RECORD = 0
                                time.sleep(2)
                                G.output(COL_PIN[j], 1)
                                break
                            else :
                                LCD_show( 'Please enter the amount. ' ,'(0~9)')
                if ( Cur_i == 1 ):
                    Cur_File = "Clothe_Cost"
                    LCD_show('B mode selected' , 'Next please enter your cost on clothe.')
                    Kb_Reset()
                    while(True):
                        if( Kb_Detect() ):
                            if (Cur_i < 3 and Cur_j < 3) or (Cur_i == 3 and Cur_j == 1):
                                RECORD = RECORD*10 + MATRIX[i][j]
                                LCD_show( 'Enter your cost: ' ,str(RECORD))
                                G.output(COL_PIN[j], 1)                                    
                            elif ( i == 3 and j == 2 ) :                                        
                                file = open( Cur_File +'.txt', 'a')
                                file.write(str(RECORD)+'In')
                                file.close()
                                LCD_show(' Cost saved. ' , 'Congratulations! ')
                                RECORD = 0
                                time.sleep(2)
                                G.output(COL_PIN[j], 1)
                                break
                            else :
                                LCD_show( 'Please enter the amount. ' ,'(0~9)')

                if ( Cur_i == 2 ):
                    Cur_File = "Living_Cost"
                    LCD_show('C mode selected' , 'Next please enter your cost on living.')
                    Kb_Reset()
                    while(True):
                        if( Kb_Detect() ):
                            if (Cur_i < 3 and Cur_j < 3) or (Cur_i == 3 and Cur_j == 1):
                                RECORD = RECORD*10 + MATRIX[i][j]
                                LCD_show( 'Enter your cost: ' ,str(RECORD))
                                G.output(COL_PIN[j], 1)                                    
                            elif ( i == 3 and j == 2 ) :                                        
                                file = open( Cur_File +'.txt', 'a')
                                file.write(str(RECORD)+'In')
                                file.close()
                                LCD_show(' Cost saved. ' , 'Congratulations! ')
                                RECORD = 0
                                time.sleep(2)
                                G.output(COL_PIN[j], 1)
                                break
                            else :
                                LCD_show( 'Please enter the amount. ' ,'(0~9)')                    
                if ( Cur_i == 3 ):
                    Cur_File = "Vehicle_Cost"
                    LCD_show('D mode selected' , 'Next please enter your cost on vehicle.')
                    Kb_Reset()
                    while(True):
                        if( Kb_Detect() ):
                            if (Cur_i < 3 and Cur_j < 3) or (Cur_i == 3 and Cur_j == 1):
                                RECORD = RECORD*10 + MATRIX[i][j]
                                LCD_show( 'Enter your cost: ' ,str(RECORD))
                                G.output(COL_PIN[j], 1)                                    
                            elif ( i == 3 and j == 2 ) :                                        
                                file = open( Cur_File +'.txt', 'a')
                                file.write(str(RECORD)+'In')
                                file.close()
                                LCD_show(' Cost saved. ' , 'Congratulations! ')
                                RECORD = 0
                                time.sleep(2)
                                G.output(COL_PIN[j], 1)
                                break
                            else:
                                LCD_show( 'Please enter the amount. ' ,'(0~9)')                          
            else:
                LCD_show( 'Select mode :','Good luck!')

except KeyboardInterrupt:
    G.cleanup()
