import pyautogui
import time

# Começo
pyautogui.alert('Digite o pic que quer gravar e não mexa em nada!')
pic = input('Qual o pic que você quer gravar? (Não precisa colocar o nome pic) ')

#Minimizar as paginas
pyautogui.hotkey('winleft', 'd')

#Abrir o MPLABpic16f
pyautogui.doubleClick(45, 385)
time.sleep(10)

#Posição do Programmer (x=291, y=31)
#Select Programmer (x=310, y=49)
#Pick it 3(x=512, y=185)
pyautogui.click(291,31)
pyautogui.click(310,49)
pyautogui.click(512, 185)
time.sleep(2)
pyautogui.press('enter')

# Configure (x=405, y=32)
pyautogui.click(405, 32)
# Select device (x=432, y=51)
pyautogui.click(432, 51)
time.sleep(2)
pyautogui.write(f'pic{pic}')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(7)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('enter')

# Selecionar arquivo
pyautogui.click(x=39, y=32) #file
pyautogui.click(x=96, y=316)
time.sleep(1)
pyautogui.click(x=459, y=529, clicks=2)
time.sleep(1)
pyautogui.doubleClick(x=607, y=549)
time.sleep(1)
pyautogui.doubleClick(x=582, y=435)
time.sleep(1)
pyautogui.doubleClick(x=605, y=363)
time.sleep(1)
# Termina faltando escolher o arquivo

# Pics

def Autoclave():
    pyautogui.click(x=39, y=32)
    pyautogui.click(x=96, y=316)
    time.sleep(1)
    pyautogui.write('Autoclave.hex')
    pyautogui.press('enter')
    pyautogui.alert('Autoclave com sucesso!')

def Rec_Standard_Plus():
    pyautogui.click(x=39, y=32)
    pyautogui.click(x=96, y=316)
    time.sleep(1)
    pyautogui.write('Central Standard')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Standar Controle Plus')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Controle_6P20D_pic12f629.HEX')
    pyautogui.press('enter')
    
def plus():
    pyautogui.write('CENTRAL PLUS FERRTECH')
    pyautogui.press('enter')
    pyautogui.write('Centrak_FR_46k20.hex')
    pyautogui.press('enter')
    pyautogui.alert('Plus com secesso!')

def agir():
    pyautogui.write('Agir_Pic10F322.hex')
    pyautogui.press('enter')

def ivomac():
    pyautogui.write('Ap_Braco_Ivom_F684.hex')
    pyautogui.press('enter')

def economy():
    pyautogui.write('Central Economy V1.3')
    pyautogui.press('enter')
    pyautogui.write('Economy_V1.3')
    pyautogui.press('enter')

def controle_economy():
    pyautogui.write('Central Economy V1.3')
    pyautogui.press('enter')
    pyautogui.write('RF3b_629')
    pyautogui.press('enter')

def controle_plus():
    pass




# Escolhendo o arquivo de acordo com o pic

if pic == '18f46k20':
    plus()
elif pic == '18f25k22':
    Autoclave()
elif pic == '10f322':
    agir()
elif pic == '16f684':
    ivomac()
elif pic == '16f1518':
    economy()
elif pic == '12f629':
    pyautogui.hotkey('alt', 'tab')
    central = input('1 - Economy\n2 - Plus\n3 - Standard? ')
    if central == '3':
        std = input('3 saidas ou duas saindas? [3] ou [2] ')
        if std == '3':
            pyautogui.hotkey('alt', 'tab')
            Rec_Standard_Plus()
    elif central == '1':
        pyautogui.hotkey('alt', 'tab')
        controle_economy()


else:
    pyautogui.alert('Fim.')









