####<>
#MAIN LOOP#
while True :
    print('\n   =================\n   =====WELCOME=====\n   =================')
    print("  useless utilities script by ac_mg")
    fun = input('\n   Type the number of the utility you wish to use: \n  1. Calculator \n  2. Heritage Counter \n  3. Vowels counter \n  4. String reverting \n  5. Equations Solver\n  6. Function Installation\n  ')

#FUN_LOOP#
    while fun != '1' and fun != '2' and fun !='3' and fun !='4' and fun !='5' and fun !='6' and fun.lower() != 'jill' :
        fun = input('please enter a valid number: ')

    else:
#CALCULATOR#
        if fun == "1" :
            import math
            print('\n  =======================')
            print('  =Welcome to CALCULATOR=')
            print('  =======================')
            print('\n  enter first number:')
            n1 = input()
            print('  operation (+ ,* ,/ ,- ,^): ')
            op = input()
            print('  enter second number:')
            n2 = input()
            if op == "+":
                print('  ==============')
                print('  result is: ', int(n1) + int(n2))
                print('  ==============')
            elif op == "-":
                print('  ==============')
                print('  result is: ', int(n1) - int(n2))
                print('  ==============')
            elif op == "*":
                print('  ==============')
                print('  result is: ', int(n1) * int(n2))
                print('  ==============')
            elif op == "/":
                print('  ==============')
                print('  result is:', int(n1) / int(n2))
                print('  ==============')
            elif op == "^":
                print('  ==============')
                print('  result is:', pow(int(n1), int(n2)))
                print('  ==============')
            else:
                print('  wrong inputs please try again')
######################################
#HERITAGE_COUNTER#
        elif fun == '2' :
            print('\n   =============================')
            print('   =Welcome to HERITAGE COUNTER=')
            print('   =============================')

            #INPUTS#
            ttl = input('  total: ')
            mls = input('  males: ')
            fmls = input('  fmls: ')
            #OPERATIONS#
            mls_share = 0
            fmls_share = 0
            if mls == "0" :
                mls_share = 0
                fmls_share = int(ttl) / int(fmls)
            elif fmls == '0' :
                fmls_share = 0
                mls_share = int(ttl) / int(mls)
            else :
                fmls_share = int(ttl) / (int(fmls) + int(mls) * 2)
                mls_share = fmls_share * 2
            #OUTPUTS#
            print('\n   =============================')
            print('   =Males share is: ' , mls_share ,'=')
            print('   =============================')
            print('\n   =============================')
            print('   =Females share is: ' , fmls_share ,'=')
            print('   =============================')
######################################
#VOWELS COUNTER#
        elif fun == "3" :
            print('\n   ===========================')
            print('   =Welcome to VOWELS COUNTER=')
            print('   ===========================\n')
            sen = input('Type your sentence here: ')
            print('\nVowels are :')
            counter = []
            for index in sen :

                if index == 'a' or index == 'e' or index == 'u' or index == 'i' or index == 'o' or index == 'y':
                    counter.append(index)
                    print('=====')
                    print('=' ,index , '=')
                    print('=====')

            if len(counter) == 0:
                print('There is no vowels')
            else :
                print(len(counter))
######################################
#STRING REVERTING#
        elif fun == '4' :
            print('\n   ============================')
            print('   =Welcome to STRING RECERTING=')
            print('   ===========================\n')
            stri = input('Enter your string here: ')
            print('result : ',''.join(reversed(stri)))
######################################
#JILL#
        elif fun.lower() == 'jill' :
            print('\n======')
            print('=JILL=')
            print('======\n')
            print('Jill: Hello I am Jill, what is yout name?\n')
            name = input('User: My name is: ' )
            def bad():
                print("\nJill: I am sorry to hear that. Why what is wrong?")
                input()
                print('\nJill: That is not cool at all but I know ', name,' you can get throw it')
            def good():
                print('\nJill: Sounds like you are having a nice day. So is there something you wanna talk about?')

            #ZING#
            if name.lower() =='zhour' or name.lower() =='jiji' or name.lower() =='tajou' or name =='joujou' or name =='tidjania' or name =='tajo' :
                print('\nJill: OMG', name.upper() , 'How are you?')
                print(name.upper(), ': \n1. I am just fine thanks for asking\n2. I am not feeling good today')
                q1 = input()
                while q1 == '1' or q1 == '2':
                    if q1 == '2' :
                        bad()
                        break
                q1 = '1'
######################################
#EQUATONS SOLVER#
        elif fun == "5" :
            print('\n   =============================')
            print('   =Welcome to EQUATIONS SOLVER=')
            print('   =============================\n')
            print('\n Make sure your equation is in the form of "ax² + bx + c = 0"')
            a=input('a= ')
            b=input('b= ')
            c=input('c= ')
            #Counting Delta#
            import math
            D = float(b) **2 - 4 * float(a) * float(c)
            print( 'Delta is: ' ,D)
            if D > 0 :
                x1 = ( - float(b) + math.sqrt(D)) / (2 * float(a))
                x2 = ( - float(b) - math.sqrt(D)) / (2 * float(a))
                print('\n   ============================')
                print('   =  "S = {', x1 ,',' , x2 ,'}"   =')
                print('   ============================\n')
            elif D == 0 :
                x = (-1 * float(b)) / (2 * float(a))
                print('\n   ============================')
                print('   =  "S = {', x ,'}"   =')
                print('   ============================\n')
            elif D < 0 :
                print('\n   ==============================')
                print('   = D < 0 , NO SOLUTIONS IN |R =')
                print('   ==============================\n')
######################################
#Function Installation#
        elif fun == '6':
            print('\n   ==================================')
            print('   =Welcome to FUNCTION INSTALLATION=')
            print('   ==================================\n')
            print('input first function then second function')

##############################################################
            #METHODS#
            def one():
                print('F[G(x)] = ' , f.replace('x' , '(' +g+ ')'))

            def two():
                print('G[F(x)] = ' , g.replace('x' , '(' +f+ ')'))

            def three():
                print('F[F(x)] = ' , f.replace('x' , '(' +f+ ')'))

            def four():
                print('G[G(x)] = ' , g.replace('x' , '(' +g+ ')'))

            #LOOPING FUNCTION#
            def looping():
                method = input('   Installation method:\n   1. (F°G)(x)\n   2. (G°F)(x)\n   3. (F°F)(x)\n   4. (G°G)(x)\n')
                if method == '1' :
                    one()
                elif method == '2' :
                    two()
                elif method == '3' :
                    three()
                elif method == '4' :
                    four()
                else :
                    print('\n   =========')
                    print('   =WTF BRO=')
                    print('   =========\n')
##############################################################
            #INPUTS#
            f = input('F(x) = ')
            g = input('G(x) = ')
            loop = input('How many installions you wanna perform ? ')
            if loop =='1':
                looping()



            elif int(loop) > 1 :
                current =
                while current < int(loop):
                    looping()
                    current += 1